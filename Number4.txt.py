from telethon import TelegramClient , events
from telethon.tl.functions.channels import JoinChannelRequest
import time
from telethon.sync import TelegramClient
from telethon import functions, types 
from telethon.sessions import StringSession
api_id = 8163559
api_hash = '01787ddb0f23a6ebfc24b57b9542ddf9'
string = '1BVtsOHIBu3RiiWj45E5Y8peeRjrsjMG6Ble8VBDeHLDo5Gfrgl3TUtny7Z7D5MuqfzRqEnn4D1mMhxTswLKszrtgm2ZF5LzXlE8ze0geUfslSHQGKcMfq8L6YqDlQr6okD6jwmuY6kr6qs_uB5UD_V30B3eXwNb_sO6sLADAsWMXU28bMftYqwie9Aw6_F42X3V7oxYS81J_m7MRndbcvWUl2xYIaDgT9KHIsBeOOz1SVUH1uwDLRzACvHRuPSVBiAIky_gWql7DWO3ySY7ZBayjpvy8dsLPjDstPOuZE70B6JXeOKDmQyiWEDEP5e3VzEmZfnFh8pubCWosApvsmmExH4Z-SXA='
with TelegramClient(StringSession(string), api_id, api_hash) as client:
 try:
  channel = client.get_entity('t.me/CryptoWizardsChat')
  client(JoinChannelRequest(channel))
 except Exception as e:
  print(e)
  pass
 while True :
  result = client(functions.account.UpdateStatusRequest(offline=False))