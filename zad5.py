import requests
################
class EmissisionsApi:
    def __init__(self, method, url, endpoint, headers, path_param = None, path = None, params = None):
        self.__method = method
        self.__url = url
        self.__endpoint = endpoint
        self.__headers = headers
        self.__path_param = path_param
        self.__path = path
        self.__params = params
        
    def request_no_body(self):
        url = f'{self.__url}{self.__endpoint}'
        method = self.__method
        if not isinstance(self.__headers, dict):
            raise Exception(f'Headers are not valid.')
        response = self.__method(url=url, headers=self.__headers)
        print(response.status_code)
        return response.json()
        
    def request_with_parameters(self):
        url = f'{self.__url}{self.__endpoint}{self.__path_param}{self.__path}'
        if not isinstance(self.__headers, dict):
            raise Exception(f'Headers are not valid.')
        print(self.__params)
        if not isinstance(self.__params, dict):
            raise Exception(f'Parameters are not valid.')
        response = self.__method(url=url, headers=self.__headers, params=self.__params)
        print(response.status_code)
        return response.json()
        
        
headers = {
    'Accept': 'application/json'
}
endpoint_1 = EmissisionsApi(
    requests.get ,'https://api.v2.emissions-api.org', '/api/v2/countries.json', headers, None)
endpoint_1.request_no_body()

endpoint_2 = EmissisionsApi(
    requests.get ,'https://api.v2.emissions-api.org', '/api/v2/products.json', headers, None)
endpoint_2.request_no_body()

endpoint_3 = EmissisionsApi(
    requests.get ,'https://api.v2.emissions-api.org', '/api/v2/', headers, 'methane', '/average.json', {'country:': 'MKD', 'limit': 5})
print(endpoint_3.request_with_parameters())
