import streamlit as st
import json
import requests
from datetime import datetime, timedelta

def check_weather(api_key, city):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.write('Currently unavailable')


st.title('Weather app')

api_key = 'cfe52b143bc7463fb6fbbc20bdfe1baa'

city= st.text_input('Weather in: ')

if st.button('Check Weather'):
    weather_data = check_weather(api_key, city)
    if weather_data:
        timestamp = weather_data['dt']
        timezone_offset = timedelta(seconds=weather_data['timezone'])
        dt_object = datetime.utcfromtimestamp(timestamp) + timezone_offset

        st.write('Current temperature: ', weather_data['main']['temp'], '°C', 'feels like: ', weather_data['main']['feels_like'], '°C')
        st.write('Weather conditions: ', weather_data['weather'][0]['description'])
        st.write('Humidity: ', weather_data['main']['humidity'], '%')
        st.write('Current date and time: ', dt_object.strftime('%d-%m-%Y %H:%M:%S'))
    else:
        st.write('Currently unavailable')