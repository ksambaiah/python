import requests
from requests.exceptions import HTTPError

for url in ['https://www.google.com', 'https://www.google.com/abcd']:
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
        print(f'Error for url  {url}') 
    except Exception as err:
        print(f'Other error occurred: {err}') 
    else:
        print('Success! for url ', url)
        print('Content \n', response.content)
        print('Content \n', response.text)
        response.encoding = 'utf-8'
        print('Content \n', response.text)
        print('Content \n', response.json)
