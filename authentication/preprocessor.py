# preprocessing.py

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd, os
import joblib
from django.conf import settings


# Load the fitted preprocessor
preprocessor_path = os.path.join(settings.BASE_DIR, 'preprocessor.pkl')
preprocessor = joblib.load(preprocessor_path)


def preprocess_data(data, preprocessor=preprocessor):
    # Preprocessing
    data['Login Timestamp'] = pd.to_datetime(data['Login Timestamp'])
    data['hour'] = data['Login Timestamp'].dt.hour
    data['day_of_week'] = data['Login Timestamp'].dt.dayofweek
    data['is_weekend'] = data['Login Timestamp'].dt.weekday >= 5

    # New feature: Number of unique IP addresses per user
    data['unique_ips'] = data.groupby('User ID')['IP Address'].transform('nunique')

    features = [
        'User ID', 'Round-Trip Time [ms]', 'unique_ips', 'Country', 'Region', 
        'City', 'ASN', 'User Agent String', 'Browser Name and Version', 
        'OS Name and Version', 'Device Type', 'Is Attack IP', 'Is Account Takeover',
        'hour', 'day_of_week', 'is_weekend'
    ]

    X = data[features]

    # Preprocess the data
    X_preprocessed = preprocessor.transform(X)
    print(X_preprocessed)
    
    # Convert sparse matrix to dense if necessary
    if hasattr(X_preprocessed, 'toarray'):
        X_preprocessed = X_preprocessed.toarray()
    
    return X_preprocessed
