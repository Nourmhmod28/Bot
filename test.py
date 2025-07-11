from pyrogram import Client

api_id =  28602152
api_hash = 'eaa59761120559fa3e3655578bbb9128'
app = Client('sessions/aeoenzbxsx', api_id=api_id, api_hash=api_hash)
app.connect()

app.send_message('@alhumsi', 'hello')

app.disconnect()