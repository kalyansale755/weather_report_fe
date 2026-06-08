import streamlit as st
import requests as rq

backend_url = st.secrets["server_url"]

st.write("Backend URL =", backend_url)

st.title("AI_weather_forecasting")

city = st.text_input("enter city")
question = st.text_input("ask your question")

if st.button("ask ai"):
    try:
        res = rq.post(
            f"{backend_url}/get_weather",
            params={
                "city": city,
                "question": question
            },
            timeout=60
        )

        st.write("Status:", res.status_code)
        st.json(res.json())

    except Exception as e:
        st.error(repr(e))