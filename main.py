import time
from telethon import TelegramClient, events
from tgtwitterforwarder import config, notifications, log_utils, twitterhandler

client = TelegramClient('session_name', config.general_params['API_ID'], config.general_params['API_HASH'])

@client.on(events.NewMessage)
async def my_event_handler(event):
    if bool(config.general_params['LOG_RECEIVED_MESSAGES_TO_CONSOLE']):
        print(f"Message {event.message.id} in chat {event.message.chat_id} with content: {event.message.text}")

    if event.message.chat_id in config.general_params['CHAT_IDS_FILTER']:
        success = twitterhandler.send_tweet(event.message.text)
        if not success:
            error_message = f'Tweet with message {event.message.text} was not sent successfully'
            log_utils.logging.error(error_message)
            notifications.send_telegram_message(error_message)


if __name__ == '__main__':

    twitterhandler.start_driver()

    while True:
        try:
            client.start()
            client.run_until_disconnected()
        except Exception as e:
            notifications.send_telegram_message("TTS: client disconnected or exception occured, attempt restart")
            log_utils.logging.error(f'Exception caught in main-loop: {e}')
            time.sleep(60)