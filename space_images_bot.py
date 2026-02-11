import os

import telegram
from dotenv import load_dotenv

def main():
    bot = telegram.Bot(token='8477642139:AAFNTj_ybZgT4SGfYEFasnLRb00zrOYGsWo')
    load_dotenv()
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    bot.send_message(chat_id=chat_id, text="Проверка отправки сообщений")


if __name__ == '__main__':
    main()