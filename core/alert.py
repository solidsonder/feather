from telethon import TelegramClient, events
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument,InputPeerChat
import smtplib
from email.message import EmailMessage
import asyncio
import os
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.photos import GetUserPhotosRequest
import warnings
import json
import sys
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="s")
parser.add_argument("path", type=Path, help="s")
args = parser.parse_args()
sys.path.append(str(args.path)+"\\lib")

from html9 import site
axx = ""
with open('lib\\logh.txt', 'r') as f:
    axx = f.read()
 

with open('lib\\config.json', 'r') as f:
    config = json.load(f)


operation = ""
with open('lib\\operation.txt','r') as f:
    operation = f.read().strip().lower()

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

def send_email(kratos,ronaldo):
    msg = EmailMessage()
    msg['Subject'] = "telegram"
    msg['From'] = email_api
    msg['To'] = to_email
    msg.set_content(kratos)

    #image + text
    if ronaldo == 0:
        msg.add_alternative(site.format(inf_list[0],inf_list[3],inf_list[2],inf_list[0],inf_list[1],str(inf_list[4])+str(inf_list[5]),inf_list[6],inf_list[7]).replace("$","{").replace("&","}"), subtype='html')

        with open(str(args.path)+"\\saved\\group_photo.jpg", 'rb') as img:
            msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg', cid='image1')
        with open(str(args.path)+"\\saved\\pp.jpg", 'rb') as img:
            msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg', cid='image2')
        with open(str(args.path)+"\\saved\\photo.jpg", 'rb') as img:
            msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg', cid='image3')

        os.remove(str(args.path)+"\\saved\\group_photo.jpg")
        os.remove(str(args.path)+"\\saved\\pp.jpg")
        os.remove(str(args.path)+"\\saved\\photo.jpg")

    elif ronaldo == 1:
        msg.add_alternative(site.format(inf_list[0],inf_list[3],inf_list[2],inf_list[0],inf_list[1],str(inf_list[4])+str(inf_list[5]),inf_list[6],inf_list[7]).replace("$","{").replace("&","}"), subtype='html')


        with open(doc_file_name, 'rb') as file:
            file_data = file.read()
            file_name = file.name
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        with open(str(args.path)+"\\saved\\group_photo.jpg", 'rb') as img:
            msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg', cid='image1')
        with open(str(args.path)+"\\saved\\pp.jpg", 'rb') as img:
            msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg', cid='image2')
        os.remove(doc_file_name)
        os.remove(str(args.path)+"\\saved\\group_photo.jpg")
        os.remove(str(args.path)+"\\saved\\pp.jpg")

    #text
    else:
        msg.add_alternative(site.format(inf_list[0],inf_list[3],inf_list[2],inf_list[0],inf_list[1],str(inf_list[4])+str(inf_list[5]),inf_list[6],inf_list[7]).replace("$","{").replace("&","}"), subtype='html')
        with open(str(args.path)+"\\saved\\group_photo.jpg", 'rb') as img:
            msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg', cid='image1')
        with open(str(args.path)+"\\saved\\pp.jpg", 'rb') as img:
            msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg', cid='image2')
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email_api, email_api_passwd)
        server.send_message(msg)

client = TelegramClient('session_name', api_id, api_hash)

async def download_user_list(channel_id):
    async with client:
        try:
            participants = []
            async for user in client.iter_participants(channel_id, search=ChannelParticipantsSearch('')):
                participants.append(user)

            with open(str(args.path)+'\\saved\\user_list.txt', 'w', encoding='utf-8') as file:
                for user in participants:
                    file.write(f"{user.id}: {user.username if user.username else 'No Username'}\n")

        except Exception as e:
            print(f'Error: {e}')

async def main(): 

    doc_exist = 0
    await client.start(phone=lambda: tel_num)
    full_channel = await client(GetFullChannelRequest(group_id))
    chat_photo = full_channel.full_chat.chat_photo
    description = full_channel.full_chat.about+" "+str(full_channel.full_chat.participants_count)
    group = await client.get_entity(group_id)
    inf_list.append(group.title)
    inf_list.append(group_id)

    invite_link = full_channel.full_chat.exported_invite.link
    with open(str(args.path)+'\\saved\\group_description.txt', 'w', encoding='utf-8') as file:
        file.write(description)
    with open(str(args.path)+'\\saved\\invite.txt', 'w', encoding='utf-8') as file:
        file.write(invite_link)

    await client.download_media(chat_photo, file=str(args.path)+'\\saved\\group_photo.jpg')
    @client.on(events.NewMessage(chats=group_id))
    async def handler(event):
        global doc_file_name
        akd = f"New message in group [{event.chat_id}]: {event.text}"
        print(akd)
        if len(operation) > 0:
            os.system(operation.replace("*&*",event.text))
        if axx == "1":
            with open(str(args.path)+'\\lib\\logs.txt', 'a', encoding='utf-8') as f:
                f.write(akd+"\n")
                f.close()
        inf_list.append(event.text)
        user = await client(GetFullUserRequest(event.sender_id))

        inf_list.append(user.users[0].username)
        inf_list.append(user.users[0].first_name)
        inf_list.append(user.users[0].last_name)
        inf_list.append(event.sender_id)
        #inf_list.append(user.full_user.about)
        inf_list.append(user.users[0].phone)
        photo_path = await client.download_profile_photo(event.sender_id, file=str(args.path)+'\\saved\\pp.jpg')

        if event.media:
            if isinstance(event.media, (MessageMediaPhoto, MessageMediaDocument)):
                try:
                    for i in event.document.attributes:
                        
                        doc_file_name = str(args.path)+"\\"+i.file_name
                        doc_exist = 1
                        await event.download_media(file=doc_file_name)

                except:
                    await event.download_media(file=str(args.path)+"\\saved\\photo.jpg")
                    doc_exist = 0


                send_email(event.text,doc_exist)
        else:
            send_email(event.text,2)                        
    print("Bot is now running...")
    await client.run_until_disconnected()


if True:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=DeprecationWarning)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())


