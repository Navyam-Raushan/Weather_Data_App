import streamlit as st
import plotly.express as px

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

dates = ["2022-12-10", "2022-12-11", "2022-12-12"]
temperatures = [10, 11, 20]
# x and y take list of arrays.
figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperatures (C}"})

# It will take a figure created by plotly.
st.plotly_chart(figure)
