import os
from telethon import TelegramClient, events, Button
import requests
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "")
   
async def check_user(id):
    if AUTH_CHANNEL is None:     
        return True
    ok = True
    try:
        await TelegramClient(GetParticipantRequest(channel=AUTH_CHANNEL, user_id=id))
        ok = True
    except UserNotParticipantError:
        ok = False
    return ok

if AUTH_CHANNEL.startswith('@'):
    x = AUTH_CHANNEL.split('@')[1]
    Mai_bOTs = f"https://t.me/{x}"
else:
    Mai_bOTs = AUTH_CHANNEL
