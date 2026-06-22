import pandas as pd
import joblib
import streamlit as st

model=joblib.load('project_model.pkl')

temperature=st.number_input('Enter todays temberature: ')
humidity=st.number_input('enter humidity: ')
wind_speed=st.number_input('enter wind speed: ')

if st.button('submit'):
    dt=pd.DataFrame({
    'temperature':[temperature],
    'humidity':[humidity],
    'wind_speed':[wind_speed]
    })
    result=model.predict(dt)
    if result>=0.5:
        st.success('There will be rain today')
    else:
        st.success('There will be no rain')
