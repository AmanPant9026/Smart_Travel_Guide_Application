# get the location of POI

from googleplaces import GooglePlaces
import googlemaps


class GoogleMaps(object):

    def __init__(self, password):

        self._GOOGLE_MAPS_KEY = password
        self._Google_Places = GooglePlaces(self._GOOGLE_MAPS_KEY)
        self._Google_Geocod = googlemaps.Client(key=self._GOOGLE_MAPS_KEY)

    def _text_search(self, query, language=None, location=None):
        text_query_result = self._Google_Places.text_search(query=query, language=language, location=location)
        return text_query_result.places

    def _reverse_geocode(self, lat, lng, language=None):
        list_reverse_geocode_result = self._Google_Geocod.reverse_geocode((lat, lng), language=language)
        return list_reverse_geocode_result

    def _return_reverse_geocode_info(self, lat, lng, language=None):
        list_reverse_geocode = self._reverse_geocode(lat, lng, language=language)
        if list_reverse_geocode:
            city = ''
            pincode = ''
            route = ''
            neighborhood = ''
            sublocality = ''
            administrative_area_level_1 = ''
            country = ''
            street_number = ''
            
            formatted_address = list_reverse_geocode[0]['formatted_address']
            for address_info in list_reverse_geocode[0]['address_components']:
                if 'locality' in address_info['types']:
                    city = address_info['long_name']
                elif 'postal_code' in address_info['types']:
                    pincode = address_info['long_name']
                elif 'route' in address_info['types']:
                    route = address_info['long_name']
                elif 'neighborhood' in address_info['types']:
                    neighborhood = address_info['long_name']
                elif 'sublocality' in address_info['types']:
                    sublocality = address_info['long_name']
                elif 'administrative_area_level_1' in address_info['types']:
                    administrative_area_level_1 = address_info['long_name']
                elif 'country' in address_info['types']:
                    country = address_info['long_name']
                elif 'street_number' in address_info['types']:
                    street_number = address_info['long_name']
            return {'city': city, 'pincode': pincode, 'route': route, 'neighborhood': neighborhood,
                    'sublocality': sublocality, 'administrative_area_level_1': administrative_area_level_1,
                    'country': country, 'formatted_address': formatted_address, 'street_number': street_number}
        else:
            return None

    def get_pincode_city(self, lat, lng, language=None):
        reverse_geocode_info = self._return_reverse_geocode_info(lat, lng, language=language)
        if reverse_geocode_info:
            return {'city': reverse_geocode_info['city'], 'pincode': reverse_geocode_info['pincode']}
        else:
            return None

    def get_address_recommendation(self, query, language=None, location=None):
        return_size = 1 # 5
        list_return_info = list()
        list_places_text_search_result = self._text_search(query=query, language=language, location=location)
        
        if len(list_places_text_search_result) > return_size:
            list_places_text_search_result = list_places_text_search_result[:return_size]
        for place in list_places_text_search_result:
            result_geocode = self._return_reverse_geocode_info(place.geo_location['lat'], place.geo_location['lng'], language=language)
            if result_geocode:
                result_geocode['formatted_address'] = '{} {}'.format(place.name, result_geocode['formatted_address'])
                result_geocode['place_name'] = place.name
                result_geocode['lat'] = '{}'.format(place.geo_location['lat'])
                result_geocode['lng'] = '{}'.format(place.geo_location['lng'])
                list_return_info.append(result_geocode)
        return list_return_info