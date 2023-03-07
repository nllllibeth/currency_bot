# Currency_bot

***
## Description

Written in Python using Aiogram, a tool that provides a user with updated crypto-currency data such as current price, average price, and shows a chart with price dynamics for the last week using Binance API.  

***

## GIF demo


![IMG_0237-1](https://user-images.githubusercontent.com/73400470/223402835-4acf643d-d3a1-4a99-b233-e69636d41e05.gif)


***

## Installation Guide

#### Local Setup
> The setup given here is for a linux environment (Debian/Ubuntu)

- Clone to the local machine 

        $ git clone https://github.com/nllllibeth/currency_bot.git
        $ cd currency_bot

- Create and activate virtual environment 

        $ python3 -m venv venv
        $ source venv/bin/activate

- Install dependencies 

        $ pip3 install -U -r requirements.txt


#### Environment Variables

For proper running  `config.py` set your own environment variables, that may contain sensetive and secret data from the list below

- `TOKEN` - Get your bot token from [Bot Father](https://t.me/BotFather)
- `API_KEY` - Get your api key from [Binance API](https://www.binance.com/en/binance-api)
- `SECRET_KEY` - With api key from [Binance API](https://www.binance.com/en/binance-api) you will be provided with secret key

#### Run bot
        $ python3 -m bot
After this command go to bot in [Telegram](https://t.me/currency_nllllibeth_bot), and run `/start` command. You will see welcome message. 

*** 

## Supported commands and functions 

#### Commands
- `/start` - Command to start bot or check whether the bot is working or not
- `/help` - Command with the same purpose as `/start`

#### Functions

After selecting a crupto-currency you will see the output from following functions:

- `Get price` - Get current price for selected symbol in USDT
- `Get average price` - Get average price for selected symbol in USDT
- `Get chart` - Show a graph with price dynamics for selected symbol in USDT for last week

***

## Contact 

You can contact me [@nllllibeth](https://t.me/nllllibeth)
