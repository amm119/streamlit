import streamlit as st
import requests
import pandas as pd
import telegram
import asyncio


def send_noti(content_noti):
    r = requests.post("https://api.pushover.net/1/messages.json", data={
        "token": st.secrets["DB_token"],
        "user": st.secrets["DB_user"],
        "message": content_noti
    })


BOT_TOKEN = '6649978795:AAG-FQ7EXkWuYI7V8nk1NevXinwMCPBtpLs'
bot = telegram.Bot(token=BOT_TOKEN)
chat_id_ab = 831373504


async def send_noti_tele(text_noti, file_noti=None):
    await bot.send_message(chat_id=chat_id_ab, text=text_noti)
    st.write(file_noti)
    if file_noti != None:
        try:
            await bot.send_photo(chat_id=chat_id_ab, photo=file_noti)
        except:
            await bot.send_video(chat_id=chat_id_ab, video=file_noti)


action_op = st.sidebar.selectbox(
    'Hôm nay em muốn làm gì nè',
    ('Gửi thông báo cho anh',
     'Làm nhiệm vụ (Coming soon)',
     'Đổi quà (Coming soon)',
     'Tích điểm bida'))
if action_op == 'Gửi thông báo cho anh':
    st.header('Gửi thông báo cho anh')
    mess_noti = st.text_input("Ghi vô đây nè")
    file_upload = None
    option = st.selectbox(
        'Em muốn gửi hình/vid hong',
        ('Hong', 'Có'))
    if option == 'Có':
        file_upload = st.file_uploader("Up file ở đây nè")
    if file_upload != None:
        try:
            st.image(file_upload)
        except:
            st.video(file_upload)
    if st.button('Gửi 💀'):
        send_noti(mess_noti)
        try:
            asyncio.run(send_noti_tele(mess_noti, file_upload))
        except RuntimeError as e:
            if "Event loop is closed" in str(e):
                pass  # do something here, like log the error
        # asyncio.run(send_noti_tele(mess_noti, img_upload))
        st.write('Thông báo đã được gửi')
if action_op == 'Tích điểm bida':
    st.header('Tích điểm bida')
    ta_point = 1410
    plus_point = 50
    url = 'https://docs.google.com/spreadsheets/d/1-OI7UEA36GsO_B5dV3k73peypSW0dFjbB98QeNCzzUs/gviz/tq?tqx=out:csv&sheet=bida'
    csv_sheet = pd.read_csv(url)
    now_point = csv_sheet.iloc[:, 1].sum()
    progress_per = (now_point+plus_point)/ta_point
    cost = csv_sheet.iloc[:, 4].str.extract(
        '(^\d*)').fillna(0).astype(int).sum()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('Còn lại : ', str(ta_point-plus_point-now_point))
    with col2:
        st.write(str(now_point), "/", str(ta_point-plus_point))
    with col3:
        st.write("Đã chơi hết : ", str(cost[0]), "K")
    st.progress(progress_per)
    st.write(csv_sheet)
