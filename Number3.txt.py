from telethon import TelegramClient , events
from telethon.tl.functions.channels import JoinChannelRequest
import time
from telethon.sync import TelegramClient
from telethon import functions, types 
from telethon.sessions import StringSession
api_id = 8163559
api_hash = '01787ddb0f23a6ebfc24b57b9542ddf9'
string = '1BVtsOHIBu8BAclKavS2QVWArwLkklNWRAAOJ944cdX-GeNWWKivVtxN-AapBUt3oMle8mxJBCrdrRu3LRCt9PB-x9Cjlhgn0Z160rTQxvnuvzBfbIHq-7LaV5G9h1Q06hCLvVkjthDxH8tGCQRoEJlz8FNimhUyjq2PsgZeXgsFWIWgw5S4W4O96tsx7DVtBe2SdXfGtHgeh3icHLYU7LKdivKtdycQWrLmDtwQ1Li4uLvRHN1yiWZfDo3OOH2jSteFz8UKUaji9qxWU0DjtXni_u9Z9H6H61zceiGvF8uGFdNAiDKgHNNEM7DduO_5c6de9z1zmbPPJEwaV6uCqM0596bvpuWY='
with TelegramClient(StringSession(string), api_id, api_hash) as client:
 try:
  channel = client.get_entity('t.me/CryptoWizardsChat')
  client(JoinChannelRequest(channel))
 except Exception as e:
  print(e)
  pass
 while True :
  result = client(functions.account.UpdateStatusRequest(offline=False))