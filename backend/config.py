from flask import Flask
import os
from telebot import TeleBot
from flask_socketio import SocketIO
from datetime import timedelta

NOWPAYMENTS_BASE_URL = "https://api.nowpayments.io/v1"

# 1. Dapatkan path folder utama (WBEENGINE)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 2. Beritahu Flask di mana letak folder templates dan static
app = Flask(__name__, 
            template_folder=os.path.join(BASE_DIR, 'templates'),
            static_folder=os.path.join(BASE_DIR, 'static'))

app.secret_key = os.urandom(24)
app.config['SOCKETIO_ASYNC_MODE'] = 'threading'

# 3. Perbaiki path database agar tidak error
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 4. Perbaiki path folder upload agar file bisa tersimpan
app.config['UPLOADS_FOLDER'] = os.path.join(BASE_DIR, 'static', 'uploads')
app.config['SOURCES_FOLDER'] = os.path.join(BASE_DIR, 'static', 'sources')

app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
app.config['TELEGRAM_BOT'] = "8448593508:AAGnn44__Cdtp9zJKAqLDEjZAcqSWf_sTZY"
app.config['TELEGRAM_CHAT_ID'] = -4842379499
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(minutes=1)
app.config['HTML_VERSION'] = 2.2

bot = TeleBot(token=app.config['TELEGRAM_BOT'])
socketio = SocketIO(app, cors_allowed_origins="*")
