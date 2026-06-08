import streamlit as st
import requests as rq
backend_url = "http://127.0.0.1:8000"
st.title("AI_weather_forecasting")
city = st.text_input("enter city")
question = st.text_input("ask your question")
if st.button("ask ai"):
    res = rq.post(f"{backend_url}/get_weather",params={
        "city":city,
        "question":question
    })
    
    st.success(res.json()["messages"][-1]["content"])

    

    
