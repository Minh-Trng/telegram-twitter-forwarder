## Telegram-Twitter-Forwarder

Simple program to monitor incoming messages on selected telegram chats and post them on twitter. This program does not use the official Twitter API but rather simulates a user on a browser via Selenium.

### Installation

After setting up a virtual environment, execute the following command:
> pip install -r requirements.txt

### Setup and usage

Copy `general_template.yml` as `general.yml` and fill it out. Information on how to get the telegram ID and hash can be found in the [Telethon docs](https://docs.telethon.dev/en/stable/basic/signing-in.html)

### Known issues

Sometimes twitter will show popup windows that prevent tweets from being sent. Have not yet found a generic working solution.