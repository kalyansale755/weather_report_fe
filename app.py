import streamlit as st
import requests as rq
backend_url =st.secrets("server_url")
st.title("AI_weather_forecasting")
city = st.text_input("enter city")
question = st.text_input("ask your question")
if st.button("ask ai"):
    res = rq.post(f"{backend_url}/get_weather",params={
        "city":city,
        "question":question
    })
    
    st.success(res.json()["messages"][-1]["content"])

    

    
