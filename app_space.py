import streamlit as st
import requests
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np




# Draw a title and some text to the app:
'''
# People in Space

This app gives information about people who are in _space_ righ now.
'''

#people in space
space = requests.get("http://api.open-notify.org/astros.json/")
data = json.loads(space.text)
nr = data["number"]

st.write("Number of people in space right now is" + " " + str(nr) + ".")
st.write("The names of these peoples' are:")

for item in data["people"]:
    st.write((item["name"]))

#current location
location = requests.get("http://api.open-notify.org/iss-now.json")
data_location = json.loads(location.text)
print(data_location)

#map
lat = float(data_location["iss_position"]["latitude"])
lon = float(data_location["iss_position"]["longitude"])

map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})


st.map(map_data) 

#Descritpion
'''
This map shows the _current location_ of the _International Space Station_ (ISS). As the location keeps changing,
_refresh the page_ to make sure you are seeing the updated location.
'''