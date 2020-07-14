import requests
import re
import random
from random import choice
import csv
import urllib3
urllib3.disable_warnings()

  
import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("mottomorning").sheet1
sheet_morningwisdom=client.open("morningwisdom").sheet1
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
  
  

  
def test_news():
    target_url = 'https://www.ettoday.net/news/realtime-hot.htm'
    print('Start parsing ptt hot....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = []
    for data in soup.select('div.part_pictxt_3 div.piece.clearfix h3 a'):
        title = data.text
        link = data['href']
        news='{}\n{}\n\n'.format(title, link)
        content.append(news)
    return content

def healthnews():
    target_url = 'https://www.edh.tw/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content= []
    for data in soup.select('div.title a'):
        title=data.text
        link = data['href']
        news='{}\n{}\n\n'.format(title, link)
        content.append(news)
    return content
  
def panx():
    target_url = 'https://panx.asia/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content= []
    for data in soup.select('div.container div.row div.desc_wrap h2 a'):
        title = data.text
        link = data['href']
        news='{}\n{}\n\n'.format(title, link)
        content.append(news)
    return content
  
def storm():
    target_url = 'https://www.storm.mg/category/k11813'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content= []
    for data in soup.select('div.category_card.card_thumbs_left a.card_link.link_title '):
        title = data.text
        link = data['href']
        news='{}{}\n\n'.format(title, link)
        content.append(news)
    return content

# 處理訊息

@handler.add(MessageEvent, message=TextMessage)
    
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    
    if event.message.text == "早安慢慢的":
        client = ImgurClient('18f064544f219ac', 'b17f2b3ef24f98c4e3cce9424ef0b1b7173ef642')
        images = client.get_album_images('qpPMzY9')
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message2 = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message3 = ImageSendMessage(
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
            event.reply_token, [image_message, image_message2, image_message3, TextSendMessage(text=早安祝福)])
        
        
 
                                                        
        return 0
  
    if event.message.text == "早安":
        client = ImgurClient('18f064544f219ac', 'b17f2b3ef24f98c4e3cce9424ef0b1b7173ef642')
        images = client.get_album_images('qpPMzY9')
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message2 = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message3 = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        
        
        早安_list=["早安","早上好","晨安","早晨好","太陽公公起來囉","晨曦多美好","旭日東昇","早上安好","早安呀","多美的太陽呀",
                 "早起多美好","早","早安朋友","晨安朋友","佛安"]
        認同分享_list=["認同請分享","分享是做功德","按讚是美德，分享是功德!","每天都要傳遞正能量","每天都要道聲早安"]
        逗點1_list=["！","！！","~","~~","~~!","~！","！！！"]
        逗點2_list=["，","！","！！","~","~~","~~!","~!","！！！","。"]
        逗點3_list=["！","！！","~","~~","~~~","~！","。"]
        
        早安 = random.choice(早安_list)
        逗點1= random.choice(逗點1_list)
        祝福 = random.choice(sheet.col_values(3))
        逗點2= random.choice(逗點2_list)
        認同分享=random.choice(認同分享_list)
        逗點3= random.choice(逗點3_list)
        
        
        早安祝福="{}{}{}{}{}{}".format(早安,逗點1,祝福,逗點2,認同分享,逗點3)
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
        
        午安_list=["午安","下午好","午安呀","美好的下午","大家午安","朋友午安"]
        認同分享_list=["認同請分享","分享是做功德","按讚是美德，分享是功德!","每天都要傳遞正能量","每天都要道聲午安"]
        逗點1_list=["！","！！","~","~~","~~!","~！","！！！"]
        逗點2_list=["，","！","！！","~","~~","~~!","~!","！！！","。"]
        逗點3_list=["！","！！","~","~~","~~~","~！","。"]
        
        午安 = random.choice(午安_list)
        逗點1= random.choice(逗點1_list)
        祝福 = random.choice(sheet.col_values(9))
        逗點2= random.choice(逗點2_list)
        認同分享=random.choice(認同分享_list)
        逗點3= random.choice(逗點3_list)
        午安祝福="{}{}{}{}{}{}".format(午安,逗點1,祝福,逗點2,認同分享,逗點3)
        
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
        
        
        晚安_list=["晚安","晚上好","朋友晚安","晚安親愛的","晚安呀","好美的夜晚","看!那繁星點綴的夜空","寂寥的夜晚，吹著孤寂的夜風"]
        認同分享_list=["認同請分享","分享是做功德","按讚是美德，分享是功德!","每天都要傳遞正能量","每天都要道聲晚安"]
        逗點1_list=["！","！！","~","~~","~~!","~！","！！！"]
        逗點2_list=["，","！","！！","~","~~","~~!","~!","！！！","。"]
        逗點3_list=["！","！！","~","~~","~~~","~！","。"]
        
        晚安 = random.choice(晚安_list)
        逗點1= random.choice(逗點1_list)
        祝福 = random.choice(sheet.col_values(13))
        逗點2= random.choice(逗點2_list)
        認同分享=random.choice(認同分享_list)
        逗點3= random.choice(逗點3_list)
        晚安祝福="{}{}{}{}{}{}".format(晚安,逗點1,祝福,逗點2,認同分享,逗點3)
        
        line_bot_api.reply_message(
            event.reply_token, [image_message, TextSendMessage(text=晚安祝福)])
                                                        
        return 0
    
    if event.message.text == "週末愉快":
        client = ImgurClient('18f064544f219ac', 'b17f2b3ef24f98c4e3cce9424ef0b1b7173ef642')
        images = client.get_album_images('hyoRqLE')
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        
        
        週末安_list=["週末快樂","週末愉快","美好週末","朋友!祝福你有個美好週末","週末心情真美麗","週末愉悅","週末也不能忘了問候朋友","朋友，週末快樂"]
        認同分享_list=["認同請分享","分享是做功德","按讚是美德，分享是功德!","每天都要傳遞正能量","每天都別忘了問候"]
        逗點1_list=["！","！！","~","~~","~~!","~！","！！！"]
        逗點2_list=["，","！","！！","~","~~","~~!","~!","！！！","。"]
        逗點3_list=["！","！！","~","~~","~~~","~！","。"]
        
        週末安 = random.choice(週末安_list)
        逗點1= random.choice(逗點1_list)
        祝福 = random.choice(sheet.col_values(17))
        逗點2= random.choice(逗點2_list)
        認同分享=random.choice(認同分享_list)
        逗點3= random.choice(逗點3_list)
        週末祝福="{}{}{}{}{}{}".format(週末安,逗點1,祝福,逗點2,認同分享,逗點3)
        line_bot_api.reply_message(
            event.reply_token, [image_message, TextSendMessage(text=週末祝福)])
                                                        
        return 0      
      
    if event.message.text == "每日一笑":
        client = ImgurClient('18f064544f219ac', 'b17f2b3ef24f98c4e3cce9424ef0b1b7173ef642')
        images = client.get_album_images('VOX4l2Y')
        index = random.randint(0, len(images) - 1)
        first5 = random.randint(len(images) - 7, len(images) - 3)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
                                                        
        return 0
      
    if event.message.text == "我要問安圖!":
        message = ImagemapSendMessage(
            base_url='https://i.imgur.com/SvEVQRQ.png',
            alt_text='this is an imagemap',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                MessageImagemapAction(
                    text='早安',
                    area=ImagemapArea(
                        x=0, y=0, width=520, height=520
                    )
                ),
                MessageImagemapAction(
                    text='午安',
                    area=ImagemapArea(
                        x=520, y=0, width=520, height=520
                    )
                ),
                MessageImagemapAction(
                    text='晚安',
                    area=ImagemapArea(
                        x=0, y=520, width=520, height=520
                    )
                ),
                MessageImagemapAction(
                    text='週末愉快',
                    area=ImagemapArea(
                        x=520, y=520, width=520, height=520
                    )
                )
            ]
        )
        line_bot_api.reply_message(event.reply_token, message)
        
        return 0

    if event.message.text == "活到老，學到老，知識就是我的糧食!":
        buttons_template = TemplateSendMessage(
            alt_text='新知',
            template=ButtonsTemplate(
                title='新聞類型',
                text='永遠求知若渴，知識就是力量!',
                thumbnail_image_url='https://i.imgur.com/qAD7YYn.png',
                actions=[
                    MessageTemplateAction(
                        label='每日新知',
                        text='每日新知'
                    ),
                    MessageTemplateAction(
                        label='健康新知',
                        text='健康新知'
                    ),
                    MessageTemplateAction(
                        label='關鍵大事',
                        text='關鍵大事'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
      
    if event.message.text == "格言":
        buttons_template = TemplateSendMessage(
            alt_text='格言',
            template=ButtonsTemplate(
                title='早安格言',
                text='充實你的內涵，內涵是最好的化粧品',
                thumbnail_image_url='https://i.imgur.com/GUdL3yV.png',
                actions=[
                    MessageTemplateAction(
                        label='早安格言',
                        text='早安格言'
                    ),
                    MessageTemplateAction(
                        label='英文格言',
                        text='英文格言'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
#ettoday      
    if event.message.text == "每日新知":
        content="".join(random.sample(test_news(),k=3))
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
#早安健康      
    if event.message.text == "健康新知":
        content="".join(random.sample(healthnews(),k=3))
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
#泛科技      
    if event.message.text == "關鍵大事":
        content="".join(random.sample(storm(),k=3))
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
      
    if event.message.text == "早安哲學":
        article = random.choice(sheet_morningwisdom.col_values(1))
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=article))
        return 0
    if event.message.text == "早安格言":
        motto = random.choice(sheet.col_values(19))
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=motto))
        return 0
    if event.message.text == "英文格言":
        mottoeng = random.choice(sheet.col_values(20))
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=mottoeng))
        return 0

      
 

@app.route('/')

def index():

    return 'Hello World'



import os

if __name__ == "__main__":

    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port)
