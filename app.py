import requests
import re
import random
from random import choice
import csv
with open('motto.csv','r',encoding="utf-8") as  csv_file:
        csv_reader = csv.reader(csv_file)
        my_list = list(csv_reader)
        
        
import configparser
from bs4 import BeautifulSoup


from imgurpython import ImgurClient

from flask import Flask, request, abort



from linebot import (

    LineBotApi, WebhookHandler

)

from linebot.exceptions import (

    InvalidSignatureError

)

from linebot.models import *



app = Flask(__name__)

config = configparser.ConfigParser()
config.read("config.ini")

# Channel Access Token

line_bot_api = LineBotApi('E9zSBfdSPaI8E76QVVHWp8slQvhT+H/5DlVp5bgwGZGksMV9A5fQFJ1W6sa0dHUDpQ4m11+DXMFppMIzmv02ze/uNf1GICPGvWEXhUbrv86hFIijndwfusSKIfRKXN7BzPlr/Zl8aYur9xl96uUjqwdB04t89/1O/w1cDnyilFU=')

# Channel Secret

handler = WebhookHandler('b56c198b7f81f9a15b1c33efcbeac68b')

client = ImgurClient('18f064544f219ac', 'b17f2b3ef24f98c4e3cce9424ef0b1b7173ef642')




# 監聽所有來自 /callback 的 Post Request

@app.route("/callback", methods=['POST'])

def callback():

    # get X-Line-Signature header value

    signature = request.headers['X-Line-Signature']

    # get request body as text

    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)

    # handle webhook body

    try:

        handler.handle(body, signature)

    except InvalidSignatureError:

        abort(400)

    return 'OK'



# 處理訊息

@handler.add(MessageEvent, message=TextMessage)
    
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    
    if event.message.text == "早安":
        client = ImgurClient('18f064544f219ac', 'b17f2b3ef24f98c4e3cce9424ef0b1b7173ef642')
        images = client.get_album_images('qpPMzY9')
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        
       
        
        
        
        morning=random.choice(my_list[0])
        morningpun1=random.choice(my_list[1])
        morningwish=random.choice(my_list[2])
        morningpun2=random.choice(my_list[3])
        share=random.choice(my_list[4])
        morningpun3=random.choice(my_list[5])
        morning_motto= "{morning}{punct1}{wish}{punct2}{share}{punct3}".format(morning=morning,punct1=morningpun1,
                                                                   wish=morningwish,punct2=morningpun2,share=share,
                                                                               punct3=morningpun3)
        line_bot_api.reply_message(
            event.reply_token, [image_message, TextSendMessage(text=morning_motto)])
        
        
 
                                                        
        return 0
    
    if event.message.text == "午安":
        client = ImgurClient('18f064544f219ac', 'b17f2b3ef24f98c4e3cce9424ef0b1b7173ef642')
        images = client.get_album_images('k7Z38KG')
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        
        line_bot_api.reply_message(
            event.reply_token, image_message)
                                                        
        return 0
    
    if event.message.text == "晚安":
        client = ImgurClient('18f064544f219ac', 'b17f2b3ef24f98c4e3cce9424ef0b1b7173ef642')
        images = client.get_album_images('daOzv5n')
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        
        line_bot_api.reply_message(
            event.reply_token, image_message)
                                                        
        return 0
    
    
    
    
        
 

@app.route('/')

def index():

    return 'Hello World'



import os

if __name__ == "__main__":

    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port)
