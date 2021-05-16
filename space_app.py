import streamlit as st
import requests
import json
import matplotlib.pyplot as plt
import cartopy.crs as ccrs


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
x = float(data_location["iss_position"]["latitude"])
y = float(data_location["iss_position"]["longitude"])
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())
ax.set_global()
ax.stock_img()
ax.coastlines()
ax.plot(x, y, color ='red', marker ='o', transform=ccrs.PlateCarree())
plt.show()
st.pyplot(fig)

#Descritpion
'''
This map shows the _current location_ of the _International Space Station_ (ISS). As the location keeps changing,
_refresh the page_ to make sure you are seeing the updated location.
'''