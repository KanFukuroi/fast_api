import streamlit as st
import random
import requests
import json


st.title("APIテスト画面(ユーザー)")

with st.form(key="user"):
    user_id: int = random.randint(1, 10)
    user_name: str = st.text_input("ユーザー名", max_chars=12)
    data = {"user_id": user_id, "user_name": user_name}
    submit_button = st.form_submit_button(label="リクエスト送信")

if submit_button:
    st.write("## リクエストデータ")
    st.json(data)
    st.write("## レスポンスデータ")
    url = "http://127.0.0.1:8000/users"
    res = requests.post(url, data=json.dumps(data))
    st.write(res.status_code)
    st.json(res.json())