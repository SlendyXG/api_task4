import os
import requests


def fetch_epic_photos():
    url = "https://epic.gsfc.nasa.gov/api/natural"
    params = {
        'api_key': 'DEMO_KEY',
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()

    os.makedirs('images', exist_ok=True)

    for image_number, image in enumerate(images[:5], start=1):
        image_name = image['image']
        date_parts = image['date'].split()[0].replace('-', '/')
        image_url = (f"https://epic.gsfc.nasa.gov/archive/natural/{date_parts}/png/{image_name}.png")
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        filename = 'epic' + str(image_number) + '.png'
        file_path = os.path.join('images', filename)
        with open(file_path, 'wb') as file:
            file.write(image_response.content)

def main():
    fetch_epic_photos()

if __name__ == '__main__':
    main()