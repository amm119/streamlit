import streamlit as st
import requests
def send_noti(content_noti):
     r = requests.post("https://api.pushover.net/1/messages.json", data = {
       "token": "at71jcurvvpgp9otn212xbkmkpebto",
       "user": "utrpuktmbuiix9oe7a957od99t45jk",
       "message": content_noti
     })
def send_noti_img(content_noti,img):
    r = requests.post("https://api.pushover.net/1/messages.json", data={
        "token": "at71jcurvvpgp9otn212xbkmkpebto",
        "user": "utrpuktmbuiix9oe7a957od99t45jk",
        "message": content_noti
    },
    files={
        "attachment": ('image.jpg', open(img, "rb"), "image/jpeg")
    })
action_op = st.sidebar.selectbox('Hôm nay em muốn làm gì nè',('Gửi thông báo cho anh','Làm nhiệm vụ (Coming soon)','Đổi quà (Coming soon)', 'Tiến Trình tích điểm bida (400đ để mở khóa)'))
if action_op == 'Gửi thông báo cho anh':
    st.header('Gửi thông báo cho anh')
    option = st.selectbox(
         'Em muốn gửi hình/vid hong',
         ('Hong', 'Có'))
    if option == 'Có':
        img_upload = st.file_uploader("Up file ở đây nè")
    if st.button('Gửi 💀'):
        if option == 'hong':
            send_noti('iuuu em ')
        else:
            send_noti_img('iuu em',img_upload)
        st.write('Thông báo đã được gửi')
    else:
        st.write('Mún gì ghi vô nè 😼')
