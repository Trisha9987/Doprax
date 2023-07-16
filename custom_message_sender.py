import time
import requests

def send_custom_message():
    bot_id = "6135924880:AAH7jJQtLpnyTENBTqeAdgDMBtzbvaK07vw"
    chat_username = "publictestbottc"
    message = "Custom message!"
    url = f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id=@{chat_username}&text={message}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message.")

while True:
    send_custom_message()
    time.sleep(60)
