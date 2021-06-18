import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("UU3Cw72rpp+TpqXKvOj+XyZaMkF93Jo6GMe1iBdLF7XBeQsZI8oMPID/BODP/LbpU6X29okGw6/7jDb6YBPksFn+CUMbGWqKxvgjvlRYLGeecL/PYw0GrRVageJbm4llIs1EzrJww3J9ZRlJ8rXjxwdB04t89/1O/w1cDnyilFU="))
handler = WebhookHandler(os.environ.get("1207d0dac98fa0fd9f96d3e6f63d4645T"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    line_bot_api.reply_message(event.reply_token, reply)
