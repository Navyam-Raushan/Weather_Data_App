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
graph_label = f"{option} for the next {days} days in {place}."
# use f11 to bookmark it.
st.subheader(graph_label)

d, t = get_data(place, days, option)
# x and y take list of arrays.
figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperatures (C}"})

# It will take a figure created by plotly.
st.plotly_chart(figure)
