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
    if result>=0.8:
        st.success('There will be heavy rainfall today')
    elif result>=0.4:
        st.success('There will be moderate rainfall today')
    elif result>=0.1:
        st.success('There will be light rainfall today')
    else:
        st.success('There will be no rainfall today')
