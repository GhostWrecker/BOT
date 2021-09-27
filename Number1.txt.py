from telethon.tl.functions.channels import JoinChannelRequest
from telethon.sync import TelegramClient
from telethon import functions
from telethon.sessions import StringSession
api_id = 8115520
api_hash = 'b2e9a876c71f752e33790e4e9281a096'
string = '1BVtsOHIBu7JNyhof_E4-4bE-kHj2hfIwcZZvxaYihmspoHwsiVRv9Pj4rD9yMF0pOwS4yzQHRtF4knu-VERl9qk8n_xpDajDFm1yrU1p9Hl5wua8LBBCws0xxh_73o-lhBWTSnZ7VCJxiRC-QoFsYMlvq32cfENI93ZDAD5fxYU0c9NPIDf3M7wNo41m_g27Tx6odqCXgSMz6fCI21moLvVKD0m8NdStwV5-NydphEYPWpoByE4LafmJaD4eoypeU_PE28ZvqZEua5cg2ScM6u0wwBic5nQOjhpiC5RuQDGv59caMVnsjuG_sKgUV9yBySK_JD-BTVg-vbjE0ngn_tqhNY-6jMo='
with TelegramClient(StringSession(string), api_id, api_hash) as client:
 try:
  channel = client.get_entity('t.me/CryptoWizardsChat')
  client(JoinChannelRequest(channel))
 except:
  pass
 while True :
  result = client(functions.account.UpdateStatusRequest(offline=False))