from telethon import TelegramClient , events
from telethon.tl.functions.channels import JoinChannelRequest
import time
from telethon.sync import TelegramClient
from telethon import functions, types 
from telethon.sessions import StringSession
api_id = 8795009
api_hash = '6996a9e98e7b6af68e0bab747b4a6b55'
string = '1BVtsOHYBu1b0z94MLoexQUtwZOnwcY5v4cRVIT5kU3ZCpmhg9YTVlERzews-MjaUPr7rgYD3TeaS9HeSnRTgy9REdCttJvZUjwuLve23k7o-CkV3DzK5NqEz0tZKR5oDmwVJwyvYWiRc06Q5J3ApaMN1ferNJJ847Xr_5RnO0M31TgFQJfscFPIIWRQwbdXy32U6OLHPJ0lsWYiMKjZCDFdP8u91UwoJvyYGS-pIsgazjEwP1l9LOP2EcX0iPiFbosLJ-o1awoRK29s0BaAtndFUqg0UaBh3qRtZPzFeZaPgr-1LLgHh_mUD8zIHGHTN02r_WR4HdEbgzO_NtTTjMGnfnXgTFgs='
with TelegramClient(StringSession(string), api_id, api_hash) as client:
 try:
  channel = client.get_entity('t.me/CryptoWizardsChat')
  client(JoinChannelRequest(channel))
 except Exception as e:
  print(e)
  pass
 while True :
  result = client(functions.account.UpdateStatusRequest(offline=False))