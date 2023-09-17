import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
# Put dynamic things into variable (Rules)
place = st.text_input("Place: ")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select number of forecasted days.")

option = st.selectbox("Select data to view",
                      options=("Temperature", "Sky"))

# Error handling for invalid place
try:
    if place:
        filtered_data = get_data(place, days, option)
        graph_label = f"{option} for the next {days} days in {place}."
        # use f11 to bookmark it.
        st.subheader(graph_label)

        if option == "Temperature":
            date = [d["dt_txt"] for d in filtered_data]
            temperature = [int(t["main"]["temp"]) / 10 for t in filtered_data]
            # x and y take list of arrays.
            figure = px.line(x=date, y=temperature, labels={"x": "Dates", "y": "Temperatures (C}"})

            # It will take a figure created by plotly.
            st.plotly_chart(figure)

        if option == "Sky":
            sky_condition = [s["weather"][0]["main"] for s in filtered_data]
            # Now we need to translate image paths
            # """ Different ways for translating data into image we will use dictionary
            #     and list comprehension for doing all of this (this is new)
            # """

            # MAKING A DICTIONARY FOR ALL PATHS.
            img_map = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                       "Rain": "images/rain.png", "Snow": "images/snow.png"}

            # ADDING LABELS TO SKY CONDITION AS PER DATE/TIME.
            filtered_data = get_data(place, days, option)
            date = [d["dt_txt"] for d in filtered_data]
            label_map = date

            # MAPPING IMAGES WITH KEY PAIRS AS PER CONDITION IN img_map
            images = [img_map[conditions] for conditions in sky_condition]

            st.image(images, width=115, caption=date)
except KeyError:
    st.info("Please enter a valid place")
    print("Error: Not a valid place")
