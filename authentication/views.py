# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import pandas as pd
from datetime import datetime
from ipware import get_client_ip
from django.conf import settings
import user_agents
from .apps import AuthenticationConfig
from .utils import get_geoip_data
from .models import LoginRecord, CustomUser as User
from .preprocessor import preprocess_data

@csrf_protect
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Collect additional data
            login_timestamp = datetime.now()

            ip_address, is_routable = get_client_ip(request)

            # Override IP address in development if it's not routable
            if not is_routable and settings.DEBUG:
                ip_address = '8.8.8.8'

            ua_string = request.META.get('HTTP_USER_AGENT', '')
            user_agent = user_agents.parse(ua_string)
            
            # Get geographical and ASN data
            geo_data = get_geoip_data(ip_address)

            # Calculate number of unique IPs for the user
            user_obj = User.objects.get(email=username)
            user_id = user_obj.id
            user_login_records = LoginRecord.objects.filter(user=user_obj)

            # Collect all features in a DataFrame
            input_data = pd.DataFrame([{
                'User ID': user_id,
                'IP Address': ip_address,
                'Round-Trip Time [ms]': 0,  # Placeholder, replace with actual value if available
                #'unique_ips': unique_ips,
                'Country': geo_data['Country'],
                'Region': geo_data['Region'],
                'City': geo_data['City'],
                'Login Successful': False,
                'ASN': geo_data['ASN'],
                'User Agent String': ua_string,
                'Browser Name and Version': user_agent.browser.family + ' ' + user_agent.browser.version_string,
                'OS Name and Version': user_agent.os.family + ' ' + user_agent.os.version_string,
                'Device Type': user_agent.device.family,
                'Is Attack IP': False,  # Placeholder, use a method to check if IP is known for attacks
                'Is Account Takeover': False,  # Placeholder, define logic to determine account takeover if needed
                'Login Timestamp': login_timestamp
            }])



            try:
                # preprocess data
                preprocess_data_input = preprocess_data(input_data)

                # Make prediction using the loaded model
                model = AuthenticationConfig.model
                prediction = model.predict(preprocess_data_input)

                # Check if login is predicted to be suspicious
                if prediction[0]:
                    # Handle suspicious login attempt
                    return JsonResponse({'error': 'Suspicious login detected'}, status=403)

                # Record successful login for tracking
                LoginRecord.objects.create(user=user_obj, ip_address=ip_address, timestamp=login_timestamp)

                # Login the user
                login(request, user)

                return JsonResponse({'prediction': prediction.tolist()})
            except Exception as e:
                return JsonResponse({'error_st': str(e)}, status=500)

        else:
            return JsonResponse({'error': 'Invalid login credentials'}, status=401)

    return render(request, 'login.html')



def index_view(request):
    return render(request, "index.html")

