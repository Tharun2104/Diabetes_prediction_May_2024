import streamlit as st
import json
import requests

st.title('Diabetes Prediction Web App')
with open('input_options.json') as f:
    side_bar_options = json.load(f)
    options = {}
    for key, value in side_bar_options.items():
        min_val, max_val = value
        current_value = (min_val + max_val)/2
        # current_value = int(current_value)
        options[key] = st.sidebar.slider(key, min_val, max_val, value=(current_value))

st.write(options)

if st.button('Diabetes Test Result'): 
    print('IN button')

    payload = json.dumps({'inputs': options})
    response = requests.post(
        url=f"http://localhost:5000/invocations",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    
    prediction = response.json().get('predictions')[0]
    if(round(prediction) == 1):
        st.write('The person is diabetic')
    else:
        st.write('The person is not diabetic')