import streamlit as st
import requests as rq

backend_url = st.secrets["server_url"]

st.title("AI Weather Forecasting")

city = st.text_input("Enter City")
question = st.text_input("Ask your Question")

if st.button("Ask AI"):
    try:
        res = rq.post(
            f"{backend_url}/get_weather",
            params={
                "city": city,
                "question": question
            },
            timeout=60
        )

        data = res.json()

        answer = data["messages"][-1]["content"]

        st.success(answer)

    except Exception as e:
        st.error(f"Error: {e}")