import streamlit as st
from database import Database
import plotly.express as px

st.sidebar.title("Flight's analytics")

user_choice = st.sidebar.selectbox('Menu', ['Select one', 'Check flights', 'Analytics'])

db = Database()

if user_choice == 'Check flights':

    c1, c2 = st.columns(2)

    cities = db.get_cities()

    with c1:

        source = st.selectbox('Select source', cities)

    with c2:

        destination = st.selectbox('Select destination', cities)

    button_1 = st.button('confirm')

    if button_1:

        if source == destination:

            st.write('enter a valid input')

        else:

            flight_data = db.get_flight_data(source, destination)

            st.dataframe(flight_data)

elif user_choice == 'Analytics':

    cities, frequency = db.get_flight_frequency()

    fig = px.pie(names = cities, values = frequency, title='flight frequency')

    st.plotly_chart(fig)

    cities, frequency = db.get_busiest_airports()

    fig = px.bar(x = cities, y = frequency, title='busiest airports data')

    st.plotly_chart(fig)

    date, frequency = db.daily_flights()

    fig = px.line(x=date, y=frequency, title='datewise flight frequency data')

    st.plotly_chart(fig)

else:

    st.header('Information about this particular analysis')