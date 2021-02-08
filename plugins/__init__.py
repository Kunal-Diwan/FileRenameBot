from telethon import events, Button
from .. import *
import requests
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest

async def check_user(id):
    if CHANNEL is None:     
        return True
    ok = True
    try:
        await done(GetParticipantRequest(channel=CHANNEL, user_id=id))
        ok = True
    except UserNotParticipantError:
        ok = False
    return ok

if CHANNEL.startswith('@'):
    x = CHANNEL.split('@')[1]
    Mai_bOTs = f"https://t.me/{x}"
else:
    Mai_bOTs = CHANNEL
