import os
import random
import time
import argparse
from pathlib import Path

import telegram
from dotenv import load_dotenv


def publish_images(bot, chat_id, interval_hours):
    all_images = []
    for image in Path('images').iterdir():
        all_images.append(str(image))

    images_to_publish = all_images.copy()
    random.shuffle(images_to_publish)

    while True:
        if not images_to_publish:
            images_to_publish = all_images.copy()
            random.shuffle(images_to_publish)

        image_path = images_to_publish.pop(0)
        image_name = os.path.basename(image_path)
        with open(image_path, 'rb') as image:
            bot.send_photo(
                chat_id=chat_id,
                photo=image,
                timeout=30,
                parse_mode='HTML'
            )

        if images_to_publish:
            wait_seconds = interval_hours * 3600
            time.sleep(wait_seconds)


def main():
    load_dotenv()
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    bot = telegram.Bot(token=telegram_bot_token)
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    parser = argparse.ArgumentParser(
        description='Публикация фотографий из директории в Telegram с заданным интервалом'
    )

    parser.add_argument(
        '--interval', '-i',
        type=float,
        default=1,
        help='Интервал между публикациями в часах'
    )
    args = parser.parse_args()
    publish_images(bot, chat_id, args.interval)


if __name__ == '__main__':
    main()
