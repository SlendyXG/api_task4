import argparse
import os

import requests

from download_image import download_image


def fetch_spacex_launch(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    launch_data = response.json()
    image_links = launch_data['links']['flickr']['original']
    os.makedirs('images', exist_ok=True)

    for image_number, image_url in enumerate(image_links, start=1):
        filename = f'spacex_{image_number}.png'
        download_image(image_url, filename)


def main():
    parser = argparse.ArgumentParser(
        description='Скачивание фотографий с запусков SpaceX'
    )
    parser.add_argument(
        '--id',
        type=str,
        help='ID запуска SpaceX (если не указан, скачивается последний запуск)',
        default='latest'
    )
    args = parser.parse_args()
    fetch_spacex_launch(args.id)


if __name__ == '__main__':
    main()