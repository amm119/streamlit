import streamlit as st
import requests
def send_noti(content_noti):
     r = requests.post("https://api.pushover.net/1/messages.json", data = {
        "token": st.secrets["DB_token"],
        "user": st.secrets["DB_user"],
       "message": content_noti
     })
action_op = st.sidebar.selectbox('Hôm nay em muốn làm gì nè',('Gửi thông báo cho anh','Làm nhiệm vụ (Coming soon)','Đổi quà (Coming soon)', 'Tích điểm bida (400đ unlock)'))
if action_op == 'Gửi thông báo cho anh':
    st.header('Gửi thông báo cho anh')
    option = st.selectbox(
         'Em muốn gửi hình/vid hong',
         ('Hong', 'Có'))
    if option == 'Có':
        img_upload = st.file_uploader("Up file ở đây nè")
    if st.button('Gửi 💀'):
        send_noti('iuuu em ')
        st.write('Thông báo đã được gửi')
    else:
        st.write('Mún gì ghi vô nè 😼')
