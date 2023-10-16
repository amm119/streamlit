import streamlit as st
import requests
def send_noti(content_noti):
     r = requests.post("https://api.pushover.net/1/messages.json", data = {
       "token": "at71jcurvvpgp9otn212xbkmkpebto",
       "user": "utrpuktmbuiix9oe7a957od99t45jk",
       "message": content_noti
     })
st.header('st.button')

if st.button('Gửi 💀'):
     send_noti('iuuu em ')
     st.write('Thông báo đã được gửi')
else:
     st.write('Mún gì ghi vô nè 😼')
