import streamlit as st

st.title("Weather Forecast for the Next Days")
# Put dynamic things into variable (Rules)
place = st.text_input("Place: ")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select number of forecasted days.")

option = st.selectbox("Select data to view",
                      options=("Temperature", "Sky"))
graph_label = f"{option} for the next {days} days in {place}."
st.title(graph_label)
