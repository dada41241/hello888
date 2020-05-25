import requests
import re
import random
from random import choice
import csv


  
import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("mottomorning").sheet1
data=sheet.get_all_records()        
        
       

        
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
        
       
        
        
        
        早安 = random.choice(sheet.col_values(1))
        標點1 = random.choice(sheet.col_values(2))
        祝福 = random.choice(sheet.col_values(3))
        標點2 = random.choice(sheet.col_values(4))
        分享= random.choice(sheet.col_values(5))
        標點3= random.choice(sheet.col_values(6))
        早安祝福="{早安}{標點1}{祝福}{標點2}{分享}{標點3}".format(早安=早安,標點1=標點1,祝福=祝福,標點2=標點2,分享=分享,標點3=標點3)
        line_bot_api.reply_message(
            event.reply_token, [image_message, TextSendMessage(text=早安祝福)])
        
        
 
                                                        
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
        
        
        
        午安 = random.choice(sheet.col_values(8))
        標點1 = random.choice(sheet.col_values(2))
        祝福 = random.choice(sheet.col_values(9))
        標點2 = random.choice(sheet.col_values(4))
        分享= random.choice(sheet.col_values(10))
        標點3= random.choice(sheet.col_values(6))
        午安祝福="{午安}{標點1}{祝福}{標點2}{分享}{標點3}".format(午安=午安,標點1=標點1,祝福=祝福,標點2=標點2,分享=分享,標點3=標點3)
        
        line_bot_api.reply_message(
            event.reply_token, [image_message, TextSendMessage(text=午安祝福)])
                                                        
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
        
        
        晚安 = random.choice(sheet.col_values(12))
        標點1 = random.choice(sheet.col_values(2))
        祝福 = random.choice(sheet.col_values(13))
        標點2 = random.choice(sheet.col_values(4))
        分享= random.choice(sheet.col_values(14))
        標點3= random.choice(sheet.col_values(6))
        晚安祝福="{晚安}{標點1}{祝福}{標點2}{分享}{標點3}".format(晚安=晚安,標點1=標點1,祝福=祝福,標點2=標點2,分享=分享,標點3=標點3)
        
        line_bot_api.reply_message(
            event.reply_token, [image_message, TextSendMessage(text=晚安祝福)])
                                                        
        return 0
    
    
    
    
        
 

@app.route('/')

def index():

    return 'Hello World'



import os

if __name__ == "__main__":

    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port)
