# Space Telegram


The program downloads photos from NASA, spaceX, EPIC and publishes them to a Telegram channel. If the interval between photo publications is not specified, photos will be published once per hour. If all photos have been published, photos will start to be published again in random order.

## How to install
### Obtaining API Keys
The program requires the following keys to function:

#### NASA API Key
1. Go to api.nasa.gov
2. Fill out the form (name, email)
3. Get a free API key (looks like DEMO_KEY or a string of characters)

#### Telegram Bot Token
1. Message @BotFather on Telegram
2. Send the /newbot command and follow the instructions
3. Get your bot token (looks like 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz)
4. Create a channel and add your bot as an administrator

#### Telegram Chat ID
1. After adding the bot to your channel, send any message
2. Get the Chat ID via @userinfobot or run this script:

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

## Launch
### Scripts Usage Examples
#### Download SpaceX Launch Photos
```
# Download photos from the latest SpaceX launch
python fetch_spacex_images.py

# Download photos from a specific SpaceX launch by ID
python fetch_spacex_images.py --id 5eb87d47ffd86e000604b38a
```
#### Download NASA APOD
```
# Download 30 random APOD photos (default)
python fetch_nasa_images.py

# Download 50 random APOD photos
python fetch_nasa_images.py --count 50

# Download APOD photo for a specific date
python fetch_nasa_images.py --date 2024-01-15
```
#### Download NASA EPIC
```
# Download the 5 most recent EPIC photos
python fetch_epic_images.py
```
#### Publish Single Photo to Telegram
```
# Publish a random photo from the 'images' folder
python publish_one_photo.py

# Publish a specific photo
python publish_one_photo.py --photo images/spacex_1.png
# or
python publish_one_photo.py -p images/nasa_apod_1.jpg
```
#### Publish Photos on a Schedule
```
# Publish photos every hour (default interval)
python publish_photos.py

# Publish photos every 2 hours
python publish_photos.py --interval 2
# or
python publish_photos.py -i 2

# Publish photos every 30 minutes
python publish_photos.py -i 0.5

# Publish photos every 4 hours
python publish_photos.py -i 4
```
## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).