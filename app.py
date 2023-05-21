# 鸚鵡機器人
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import(
    InvalidSignatureError
)

from linebot.models import(
    MessageEvent, TextMessage, TextSendMessage,
)

import json


app = Flask(__name__)

line_bot_api = LineBotApi("KIwrkQkj3J//EISKpQIzpfo/tBCAueUIFcXc6efHEzsM8m4G20AVR9zfZhxXkICKg9DHWwenccvfwMxu5191l2BGGESBFiGmXd9bcEhRtIdQwZwABM6yK+PKuQeZyHoiqa3FUqLA1ZudEZoBsEVOcwdB04t89/1O/w1cDnyilFU=")

handler = WebhookHandler("67658dfb77b908b5665c45310caa8df2")

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    json_str = json.dumps(json_data, indent=4)
    print(json_str)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
        
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    json_data = json.loads(str(event))
    json_str = json.dumps(json_data, indent=4)
    print(json_str)    
    # 獲得使用者傳來的訊息
    msg = event.message.text
    # 回覆訊息
    line_bot_api.reply_message(event.reply_token, TextSendMessage(msg))
    
if __name__== "__main__":
    app.run(port=3202)
