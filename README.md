# Space Telegram


The program downloads photos from NASA, spaceX, EPIC and publishes them to a Telegram channel.

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

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).