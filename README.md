# Channel Musics Caption Adder Bot



## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Soebb/channel-musics-caption-adder)



## How to use it ?

Add the bot in your channel as admin,     
Then send musics to the bot,                 
Bot will post them with a dynamic caption in your channel as soon as they be received(in private).

The added caption will be in this format :

```
✏️ Title: <title>
👤 Artist: <artist>
```


## Deploy locally
1. Install dependencies
```bash
git clone https://github.com/samadii/channel-musics-caption-adder
cd channel-musics-caption-adder
pipenv install
```
2. Enter vars

```
BOT_TOKEN -> The bot's token
CHANNEL_ID = -> The channel you want to be forwarded to. (Format: -xxxxxxxx)
```

3. Run!
```bash
pipenv run python main.py
```
