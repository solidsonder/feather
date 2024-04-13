from telethon import TelegramClient
from telethon.tl.types import ChannelParticipantsSearch
import asyncio
import os
import warnings
import json

with open('lib/config.json', 'r') as f:
    config = json.load(f)

#basic
doc_file_name = ""
inf_list = []

#Telegram
api_id = config.get("api_id")
api_hash = config.get("api_hash")
tel_num = config.get("phone_number")
group_id = int(config.get("group_id"))

#SMTP
email_api = config.get("sender_mail")
email_api_passwd = config.get("app_passwd").replace("-"," ")
api_subject = config.get("recipient_mail")
to_email = config.get("recipient_mail")

client = TelegramClient('session_name', api_id, api_hash)

async def download_user_list(channel_id):
    async with client:
        try:
            b = 'lib/user_list.txt'
            participants = await client.get_participants(group_id)

            with open(b, 'w', encoding='utf-8') as file:
                for user in participants:
                    file.write(f"{user.id}: {user.username if user.username else 'No Username'}\n")

            print("saved: "+b)

        except Exception as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=DeprecationWarning)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(download_user_list(group_id))
