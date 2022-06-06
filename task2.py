import os
import requests

from requests.exceptions import Timeout

HOST = 'https://api.openweathermap.org/data/2.5'

DEFAULT_CITY_NAME = "Kyiv"
DEFAULT_LANG = 'ua'
DEFAULT_UNITS = 'metric'


def show_weather() -> None:
    api_key = os.environ.get('OPENWEATHERMAP_API_KEY')
    if not api_key:
        print('You have trouble with api_key')
        exit()

    url = (
        f'{HOST}/weather?q={DEFAULT_CITY_NAME}&appid={api_key}'
        f'&lang={DEFAULT_LANG}&units={DEFAULT_UNITS}'
    )

    try:
        print('Loading weather...')
        response = requests.get(url, timeout=6)
    except Timeout:
        print('Timeout waiting for weather')
        exit()
    except Exception as e:
        print(f'Something wrong with getting weather: {str(e)}')
        exit()

    print(f'Info about weather in {DEFAULT_CITY_NAME}:')
    print(response.json())


if __name__ == '__main__':
    show_weather()
