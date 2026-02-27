import os
import random
import argparse
from pathlib import Path

import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    chat_id = os.environ['TELEGRAM_CHAT_ID']

    parser = argparse.ArgumentParser(
        description='Публикация одного фото'
    )
    parser.add_argument(
        '--photo',
        '-p',
        help='Конкретное фото (если не указано - случайное)'
    )
    args = parser.parse_args()

    if args.photo and os.path.exists(args.photo):
        photo_path = args.photo
    else:
        photos = [str(f) for f in Path('images').iterdir()
                  if f.suffix.lower() in ['.jpg', '.jpeg', '.png']]
        if not photos:
            return
        photo_path = random.choice(photos)

    with open(photo_path, 'rb') as f:
        bot.send_photo(chat_id=chat_id, photo=f, timeout=60)


if __name__ == '__main__':
    main()