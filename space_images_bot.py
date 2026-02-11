import os

import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    bot = telegram.Bot(token=telegram_bot_token)
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    bot.send_message(chat_id=chat_id, text="Проверка отправки сообщений")


if __name__ == '__main__':
    main()
