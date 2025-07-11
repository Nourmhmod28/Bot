import re
from telethon.sync import TelegramClient
from telethon import events, Button
import configparser
from t import *
import sys
import json
import os

config = configparser.ConfigParser() 
config.read("config.ini")

api_id = config['App']['28602152']
api_hash = config['App']['eaa59761120559fa3e3655578bbb9128']
client = TelegramClient('ownsession/add_user', api_id, api_hash)

token = config['8174742142:AAHraz-UFR--f4JNNFLwsASEYxtyDAmFT0U']['mybot']
#channel = config['App']['channel']
idbot =  int(token.split(':')[0])

client.start(bot_token=token)
dev = json.loads(config['App']['dev'])

arg = sys.argv

start = [
            [Button.inline('بدء عملية نقل جديدة', "start")],
            [Button.inline('بدء رسائل إزعاج', "ms")],
    ]
back = [
            [Button.inline('إلغاء ورجوع', "back")]
    ]

sub = [
            [Button.inline('بدء', "sub")]
]
sub2 = [
            [Button.inline('بدء', "sub2")]
]
sub.append(back[0])


@client.on(events.NewMessage())
async def main(event):
    chattt = await event.get_chat()
    if chattt.__class__.__name__ != 'User':
        return
        
    try:
        b = event.message.peer_id.channel_id
        b = f"-100{b}"
    except:
        pass

    ms_id = event.message.id
    text = event.raw_text.split("\n")[0]
    cleantext = event.raw_text
    fid = event.sender_id
    chat = event.chat_id
    ex_text = text.split("_")
    try:
        sql_data = get(str(fid))
        ex = sql_data.split('|')
    except:
        ex = [None, None]
    if fid == idbot:
        return

    if fid not in dev:
        return
    
    if text == '/start':
        put(str(fid), 'None|None')
        await event.reply('أهلا بك', buttons=start)
        return
    #command|url1|num of account|url2|time|num of members

    if text and ex[0] == 'start':
        if is_urls(text):
            if is_tele(text):
                put(str(fid), 'start2|'+text)
                c = len(os.listdir('sessions'))
                await event.reply(f'ارسل عدد الحسابات.. \n\n عدد الحسابات الحالي تقريبا : {c}', buttons=back)
            else:
                await event.reply('أرسل روابط تليجرام حصرا..', buttons=back)
        else:
            await event.reply('أرسل روابط حصرا..', buttons=back)
            return
    
    if text and ex[0] == 'start2':
        if is_int(text):
            put(str(fid), 'start3|'+ex[1]+'|'+text)
            await event.reply('أرسل رابط القروب للنقل إليه', buttons=back)
            return
        else:
            await event.reply('أرسل أرقاما حصرا..', buttons=back)
            return


    if text and ex[0] == 'start3':
        if is_urls(text):
            if is_tele(text):
                put(str(fid), 'start4|'+ex[1]+'|'+ex[2]+'|'+text)
                await event.reply(f'أرسل التوقيت بين الإضافة والأخرى بالثواني حصرا\n\nتجنب الأرقام العشرية : 0.2', buttons=back)
            else:
                await event.reply('أرسل روابط تليجرام حصرا..', buttons=back)
        else:
            await event.reply('أرسل روابط حصرا..', buttons=back)
            return
    

    if text and ex[0] == 'start4':
        if is_int(text):
            put(str(fid), 'start5|'+ex[1]+'|'+ex[2]+'|'+ex[3]+'|'+text)
            await event.reply("""
أرسل عدد الأعضاء التي تريد نقلها..

من أجل الحد الأقصى أرسل عددا كبيرا: 1000000
            """, buttons=back)
        else:
            await event.reply('أرسل أرقاما حصرا..', buttons=back)
            return

    #command|url1|num of account|url2|time|num of members
    if text and ex[0] == 'start5':
        if is_int(text):
            put(str(fid), 'sub|'+ex[1]+'|'+ex[2]+'|'+ex[3]+'|'+ex[4]+'|'+text)
            await event.reply(f"""
هل تريد بدء اشتراك الحسابات..؟؟

نقل من : {ex[1]}
نقل إلى : {ex[3]}
عدد الحسابات : {ex[2]}
وقت الإضافة : {ex[4]}
عدد الأعضاء المراد نقلها : {text}
            """, buttons=sub)
        else:
            await event.reply('أرسل أرقاما حصرا..', buttons=back)
            return
    
    if text == '/check':
        await event.reply('جار التحقق من الحسابات..')
        send_shell('python3', 'cmd.py', 'check', str(fid))

        return
    if ex_text[0] == '/left':
        send_shell('python3', 'cmd.py', 'left', str(fid), ex_text[1])
        await event.reply('جار المغادرة..')
        return
    
    if ex_text[0] == '/begin':
        send_shell('python3', 'cmd.py', 'begin', str(fid), ex_text[1])
        await event.reply('ok_>>')
        return

    if ex_text[0] == '/beginsend':
        send_shell('python3', 'cmd.py', 'beginsend', str(fid), ex_text[1])
        await event.reply('ok_>>')
        return


    if text and ex[0] == 'ms':
        if is_urls(text):
            if is_tele(text):
                put(str(fid), 'ms2|'+text)
                c = len(os.listdir('sessions'))
                await event.reply(f'ارسل عدد الحسابات.. \n\n عدد الحسابات الحالي تقريبا : {c}', buttons=back)
            else:
                await event.reply('أرسل روابط تليجرام حصرا..', buttons=back)
        else:
            await event.reply('أرسل روابط حصرا..', buttons=back)
            return

    if text and ex[0] == 'ms2':
        if is_int(text):
            put(str(fid), 'ms3|'+ex[1]+'|'+text)
            await event.reply('أرسل عدد الثواني sleep', buttons=back)
            return
        else:
            await event.reply('أرسل أرقاما حصرا..', buttons=back)
            return

    if text and ex[0] == 'ms3':
        if is_int(text):
            put(str(fid), 'ms4|'+ex[1]+'|'+ex[2]+'|'+text)
            await event.reply('أرسل عدد الأعضاء لإرسال الرسالة لهم', buttons=back)
            return
        else:
            await event.reply('أرسل أرقاما حصرا..', buttons=back)
            return

    if text and ex[0] == 'ms4':
        if is_int(text):
            put(str(fid), 'ms5|'+ex[1]+'|'+ex[2]+'|'+ex[3]+'|'+text)
            await event.reply('ارسل الإعلان ، نص فقط', buttons=back)
            return
        else:
            await event.reply('أرسل أرقاما حصرا..', buttons=back)
            return

    if text and ex[0] == 'ms5':
        put(str(fid), 'sub2|'+ex[1]+'|'+ex[2]+'|'+ex[3]+'|'+ex[4]+'|'+cleantext)
        await event.reply(f'''
هل تريد بدء اشتراك الحسابات..؟؟

الرابط: {ex[1]}
عدد الحسابات: {ex[2]} 
عدد الثواني: {ex[3]}
عدد الأعضاء: {ex[4]}
الرسالة : {cleantext}

        ''', buttons=sub2)
        return


@client.on(events.CallbackQuery)
async def callback(event):

    try:
        chat = event.original_update.peer.user_id
        dataa = event.data
        data = dataa.decode("utf-8")
        ex = data.split("-")
    except:
        data = False
    fid = event.sender_id

    try:
        sql_data = get(str(fid))
        print(sql_data)
        ex = sql_data.split('|')
    except Exception as es:
        print(es)
        ex = [None, None]

    

    if data == 'back':
        put(str(fid), 'None|None')
        await event.edit('أهلا بك', buttons=start)

    if data == 'start':
        put(str(fid), 'start|')
        await event.edit('أرسل رابط القروب للنقل منه..', buttons=back)

    if data == 'sub' and ex[0] == 'sub':
        #command|url1|num of account|url2|time|num of members
        url1 = ex[1]
        num_of_ac = ex[5]
        url2 = ex[3]
        times = ex[4]
        num = ex[2]
        await event.answer('جار دخول الحسابات', alert=True, cache_time=100)
        send_shell('python3', 'cmd.py', 'join', num, str(fid), url1, url2, num_of_ac, times)
        pass

    if data == 'sub' and ex[0] != 'sub':
        await event.answer('بيانات خاطئة', alert=True)
        pass



    if data == 'sub2' and ex[0] == 'sub2':
        #command | url1 | num of ac | sec | num numbers | ad
        url1 = ex[1]
        num_of_ac = ex[4]
        url2 = url1
        times = ex[3]
        num = ex[2]
        ad = randtext(5)
        put(ad, ex[5])
        await event.answer('جار دخول الحسابات', alert=True, cache_time=100)
        send_shell('python3', 'cmd.py', 'join2', num, str(fid), url1, url2, num_of_ac, times, ad)
        pass

    if data == 'sub2' and ex[0] != 'sub':
        await event.answer('بيانات خاطئة', alert=True)
        pass

    
    if data == 'ms':
        put(str(fid), 'ms|')
        await event.edit('أرسل رابط القروب..', buttons=back)
    

client.run_until_disconnected()