import argparse
import os

import requests


def fetch_spacex_launch(launch_id=None):
    if launch_id:
        url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    else:
        url = 'https://api.spacexdata.com/v5/launches/latest'

    response = requests.get(url)
    response.raise_for_status()
    launch_data = response.json()

    image_links = launch_data['links']['flickr']['original']
    os.makedirs('images', exist_ok=True)

    for image_number, url in enumerate(image_links, start=1):
        image_response = requests.get(url)
        image_response.raise_for_status()
        filename = f'spacex_{image_number}.png'
        file_path = os.path.join('images', filename)
        with open(file_path, 'wb') as file:
            file.write(image_response.content)


def main():
    parser = argparse.ArgumentParser(
        description='Скачивание фотографий с запусков SpaceX'
    )
    parser.add_argument(
        '--id',
        type=str,
        help='ID запуска SpaceX (если не указан, скачивается последний запуск)'
    )
    args = parser.parse_args()
    fetch_spacex_launch(args.id)


if __name__ == "__main__":
    main()