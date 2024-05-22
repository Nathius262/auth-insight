import os
from django.conf import settings
import geoip2.database
import geoip2.errors


def get_geoip_data(ip_address):
    geoip_path = settings.GEOIP_PATH
    city_db_path = os.path.join(geoip_path, 'GeoLite2-City.mmdb')
    asn_db_path = os.path.join(geoip_path, 'GeoLite2-ASN.mmdb')

    # Initialize readers for the databases
    city_reader = geoip2.database.Reader(city_db_path)
    asn_reader = geoip2.database.Reader(asn_db_path)

    try:
        city_response = city_reader.city(ip_address)
        asn_response = asn_reader.asn(ip_address)

        # Check and assign values or defaults
        country = city_response.country.name if city_response.country.name else 'Unknown'
        region = city_response.subdivisions.most_specific.name if city_response.subdivisions.most_specific.name else 'Unknown'
        city = city_response.city.name if city_response.city.name else 'Unknown'
        asn = asn_response.autonomous_system_number if asn_response.autonomous_system_number else 0

        geo_data = {
            'Country': country,
            'Region': region,
            'City': city,
            'ASN': asn,
        }

    except geoip2.errors.AddressNotFoundError:
        geo_data = {
            'Country': 'Unknown',
            'Region': 'Unknown',
            'City': 'Unknown',
            'ASN': 0,
        }

    finally:
        city_reader.close()
        asn_reader.close()

    #print(geo_data)
    return geo_data
