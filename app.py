
from config import Config
from pyrofork.errors import *
from pyrofork import Client, filters
from pyrofork.types import InlineKeyboardButton, InlineKeyboardMarkup
import json
from functools import partial
import random,asyncio
import os,sqlite3

bot = Client("my_bot", api_id=Config.APP_ID, api_hash=Config.API_HASH,bot_token=Config.BOT_TOKEN)

class database:
    def __init__(self) :
        if not os.path.isfile("database/data.db"):
            with sqlite3.connect("database/data.db") as connection:
                cursor = connection.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS accounts (ses TEXT,number TEXT,id TEXT)")
                connection.commit()
                
    def AddAcount(self,ses,numbers,id):
        with sqlite3.connect("database/data.db") as connection:
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO accounts VALUES ('{ses}','{numbers}','{id}')")
            connection.commit()

    def RemoveAllAccounts(self):
        with sqlite3.connect("database/data.db") as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM accounts")
            connection.commit()

    def RemoveAccount(self, numbers):
        with sqlite3.connect("database/data.db") as connection:
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM accounts WHERE number = '{numbers}' ")
            connection.commit()
    
    def accounts(self):
        list = []
        with sqlite3.connect("database/data.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM accounts")	
            entry = cursor.fetchall()
            for i in entry:
                list.append([i[0],i[1]])
        return list
    def AddBackupAcount(self,ses,numbers,id):
        with sqlite3.connect("database/data.db") as connection:
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO accounts VALUES ('{ses}','{numbers}','{id}')")
            connection.commit()
    def backupaccounts(self):
        list = []
        with sqlite3.connect("database/data.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM accounts")	
            entry = cursor.fetchall()
            for i in entry:
                list.append(i)
        return list


class Custem :
    async def ADDuserhide(slef,data,inGRob,grop2,bot,nmcount):
        list = database().accounts()
        random.shuffle(list)
        inGRob = inGRob.split("/")[3]
        count = 0
        administrators = []
        async for ms in bot.get_chat_members(inGRob):
            try:
                administrators.append(ms.user.username)
            except:
                print("rrrrrr")
                pass
        maxnum = 50
        for name in list :
            xx = 0
            xx1 = 0
            num =0
            if int(count) >= int(nmcount)  :
                break
            async with Client("::memory::", Config.APP_ID, Config.API_HASH,no_updates=True,in_memory=True,lang_code="ar",session_string=name[0]) as app:
                try:
                    await app.join_chat(inGRob)
                    await app.join_chat(grop2)
                except:
                    pass
                xx = (await app.get_chat(inGRob)).members_count  
                for msg in data:
                    await asyncio.sleep(2)
                    if  msg in administrators :
                        continue
                    else:
                        try: 
                            await app.add_chat_members(inGRob, msg)
                            num +=1
                        except PeerFlood as e :
                            if "PEER_FLOOD" in  str(e) or "The method can't be used because your account is currently limited" in  str(e):
                                break
                        except Exception as e:
                            if "FLOOD_WAIT_X" in  str(e) :
                                break
                            pass
                    if int(num) == int(maxnum)  :
                        x = (await app.get_chat(inGRob)).members_count
                        if (x - xx ) == int(nmcount) :
                            break
                        else:
                            num = x - xx
                xx1 = (await app.get_chat(inGRob)).members_count
            totalxx= xx1 - xx
            count += totalxx
            await bot.send_message(Config.OWNER_ID, f"🎉 تم إضافة {totalxx} عضو من حساب {name[1]} بنجاح! 🎉")
        await bot.send_message(Config.OWNER_ID, f"✅ تم إضافة {count} عضو إجماليًا بنجاح! 🥳")

            
    async def ADDuser(slef,inGRob,grop2,bot,nmcount):
        list = database().accounts()
        random.shuffle(list)
        inGRob = inGRob.split("/")[3]
        count = 0
        administrators = []
        async for m in bot.get_chat_members(inGRob):
            try:
                administrators.append(m.user.id)
            except:
                print("rrrrrr")
        
                pass
        maxnum = 50
        for name in list :
            xx = 0
            xx1 = 0
            num =0
            if int(count) >= int(nmcount)  :
                break
            async with Client("::memory::", Config.APP_ID, Config.API_HASH,no_updates=True,in_memory=True,lang_code="ar",session_string=name[0]) as app:
                try:
                    await app.join_chat(inGRob)
                    await app.join_chat(grop2)
                except:
                    pass
                xx = (await app.get_chat(inGRob)).members_count  
                print(xx)
                async for m in app.get_chat_members(grop2,limit=10000) : 
                    await asyncio.sleep(2)
                    if m.user.id in administrators:
                        continue
                    else:
                        try: 
                            await app.add_chat_members(inGRob, m.user.id)
                            num +=1
                            print(num)
                        except PeerFlood as e :
                            print("PeerFlood",e)
                            if "PEER_FLOOD" in  str(e) or "The method can't be used because your account is currently limited" in  str(e):
                                break
                        except Exception as e:
                            print(e)
                            if "FLOOD_WAIT_X" in  str(e) :
                                break
                            pass
                    if int(num) == int(maxnum)  :
                        x = (await app.get_chat(inGRob)).members_count
                        print(x - xx)
                        if (x - xx ) == int(nmcount) :
                            break
                        else:
                            num = x - xx
                xx1 = (await app.get_chat(inGRob)).members_count
            totalxx= xx1 - xx
            count += totalxx
            await bot.send_message(Config.OWNER_ID, f"🎉 تم إضافة {totalxx} عضو من حساب {name[1]} بنجاح! 🎉")
        await bot.send_message(Config.OWNER_ID, f"✅ تم إضافة {count} عضو إجماليًا بنجاح! 🥳")
    
        
    async def GETuser(slef,GrobUser): 
        list = database().accounts()
        random.shuffle(list)
        GrobUser = GrobUser.split("/")[-1] 
        name = random.choice(list)
        print(name)
        administrators = []
        async with Client("::memory::", Config.APP_ID, Config.API_HASH,no_updates=True,in_memory=True,lang_code="ar",session_string=name[0]) as app:      
            await app.join_chat(GrobUser)
            async for m in app.get_chat_members(GrobUser,limit=10000):
                try:
                    administrators.append(m.user.id)
                except:
                    print("rrrrrr")
                    pass
        return administrators
    
    async def GETuserhide(slef,GrobUser): 
        list = database().accounts()
        random.shuffle(list)
        GrobUser = GrobUser.split("/")[-1] 
        name = random.choice(list)
        administrators = []
        async with Client("::memory::", Config.APP_ID, Config.API_HASH,no_updates=True,in_memory=True,lang_code="ar",session_string=name[0]) as app:      
            await app.join_chat(GrobUser)
            async for msg in app.get_chat_history(GrobUser,limit=10000):
                try:
                    if msg.from_user.username != None:
                        administrators.append(msg.from_user.username)
                except:
                    pass
        return administrators
        
        
    async def joinbar(self, client, message):
        accounts = database().accounts()
        inGRob = message.text.split("/")[-1]
        if not accounts:
            return await message.reply("❌ لا يوجد حسابات متاحة للانضمام!")
        success, failed = 0, 0
        for session_string in accounts:
            try:
                async with Client("::memory::", Config.APP_ID, Config.API_HASH,no_updates=True,in_memory=True,lang_code="ar",session_string=name[0]) as app:      
                    await app.join_chat(inGRob)
                    success += 1
            except Exception as e:
                print(f"⚠️ خطأ في الحساب {session_string}: {e}")
                failed += 1
        await message.reply(f"✅ تم انضمام {success} حساب بنجاح! 🚀\n❌ فشل {failed} حساب.")

    async def leavebar(self, client, message):
        accounts = database().accounts()
        inGRob = message.text.split("/")[-1]
        if not accounts:
            return await message.reply("❌ لا يوجد حسابات متاحة للمغادرة!")
        success, failed = 0, 0
        for session_string in accounts:
            try:
                async with Client("::memory::", Config.APP_ID, Config.API_HASH, no_updates=True) as app:
                    await app.leave_chat(inGRob)
                    success += 1
            except Exception as e:
                print(f"⚠️ خطأ في الحساب {session_string}: {e}")
                failed += 1
        await message.reply(f"👋 تم مغادرة {success} حساب بنجاح!\n❌ فشل {failed} حساب.")   
        
    
    
@bot.on_message(filters.command('start'))
async def admin(client, message):
    if message.from_user.id == Config.OWNER_ID or message.from_user.id in Config.Devs:
        buttons = [
            [InlineKeyboardButton("إضافة حساب جديد 🆕", callback_data="AddAccount"), InlineKeyboardButton("حذف حساب 🗑️", callback_data="RemoveAccount")],
            [InlineKeyboardButton("انضمام للجروب 🛎", callback_data="joinGroup"), InlineKeyboardButton("مغادرة جروب 🛑", callback_data="leaveGroup")],
            [InlineKeyboardButton("حساباتك المسجلة 📋", callback_data="Accounts")],
            [InlineKeyboardButton("نقل الأعضاء 👤", callback_data="addshow"),
            InlineKeyboardButton("نقل اعضاء مخفيين 👤", callback_data="addhide")],
            [InlineKeyboardButton("نسخة احتياطية  📂", callback_data="BackupAccounts"),
            InlineKeyboardButton("رفع نسخة احتياطية  📤", callback_data="AddBackupAccounts")],
            [InlineKeyboardButton("حذف كل الحسابات", callback_data="del_all_accounts")]
        ]
        
        # تهيئة لوحة المفاتيح
        inline_keyboard = InlineKeyboardMarkup(buttons)

        # إرسال رسالة الترحيب مع الأزرار
        await client.send_message(message.chat.id, "*أهلاً وسهلاً بك في بوتنا الرائع! 🌟\nاختَر الخيار الذي يناسبك من الأزرار أدناه وسنبدأ معًا رحلتنا المليئة بالخيارات الرائعة 🔥*", reply_markup=inline_keyboard)




@bot.on_callback_query()
async def call_handler(client, call):
    #زر الرجوع
    if call.data == "back":
        buttons = [
            [InlineKeyboardButton("إضافة حساب جديد 🆕", callback_data="AddAccount"), InlineKeyboardButton("حذف حساب 🗑️", callback_data="RemoveAccount")],
            [InlineKeyboardButton("انضمام للجروب 🛎", callback_data="joinGroup"), InlineKeyboardButton("مغادرة جروب 🛑", callback_data="leaveGroup")],
            [InlineKeyboardButton("حساباتك المسجلة 📋", callback_data="Accounts")],
            [InlineKeyboardButton("نقل الأعضاء 👤", callback_data="addshow"),
            InlineKeyboardButton("نقل اعضاء مخفيين 👤", callback_data="addhide")],
            [InlineKeyboardButton("نسخة احتياطية  📂", callback_data="BackupAccounts"),
            InlineKeyboardButton("رفع نسخة احتياطية  📤", callback_data="AddBackupAccounts")],
            [InlineKeyboardButton("حذف كل الحسابات", callback_data="del_all_accounts")]
         ]
        inline_keyboard = InlineKeyboardMarkup(buttons)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="*مرحبًا بك في قائمة الخيارات! اختر ما يناسبك 👇*", reply_markup=inline_keyboard)
    
    # إضافة حساب
    elif call.data == "AddAccount":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text="*أرسل الرقم الذي تريد تسليمه مع رمز الدولة الآن 📞🎩*",
        )
        bot.register_next_step_handler(AddAccount)

    elif call.data == "del_all_accounts":
        database().RemoveAllAccounts()
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text="✅ تم حذف جميع الحسابات بنجاح!",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع 🛎", callback_data="back")]])
        )
    #انضمام حسابات
    elif call.data == "joinGroup":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text="*أرسل رابط الجروب للانضمام إليه 📲*",
        )
        bot.register_next_step_handler(Custem().joinbar)
    #مغادرة حسابات
    elif call.data == "leaveGroup":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text="*أرسل رابط الجروب للمغادرة منه 🛑*",
        )
        bot.register_next_step_handler(Custem().leavebar)
        
    # حذف حساب
    elif call.data == "RemoveAccount":
        await show_accounts_as_buttons(call, 0,"RemoveAccount")
    #عرض الحسابات   
    elif call.data == "Accounts":
        await show_accounts_as_buttons(call, 0,"Accounts")
        
    elif call.data.startswith("page_"):
        data = call.data.split("_")[1]  # استخراج رقم الصفحة
        pross = data.split("-")[0]
        current_page = int(data.split("-")[1])
        await show_accounts_as_buttons(call, current_page,pross)  # عرض الحسابات في الصفحة الحالية
    
    elif call.data.startswith("delaccount_"):
        del_number = call.data.split("_")[1]  # استخراج رقم الحساب
        database().RemoveAccount(del_number)
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=f"✅ تم حذف الرقم: {del_number} بنجاح!",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع 🛎", callback_data="back")],]))
        
    #باك اب حسابات
    elif call.data == "BackupAccounts":
        accounts = database().backupaccounts()
        with open('./FR3ONBackUp.json', 'w', encoding='utf-8') as f:
            json.dump(accounts, f, ensure_ascii=False, indent=4)
        await bot.send_document(chat_id=call.message.chat.id,document='./FR3ONBackUp.json',caption="📂 النسخة الاحتياطية من الحسابات")
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text="✨ تم حفظ البيانات في ملف FR3ONBackUp.json بنجاح. استمتع بالإدارة المنظمة! 📁",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع 🛎", callback_data="back")],])
        )
        os.remove('./FR3ONBackUp.json')

    # رفع النسخة الاحتياطية
    elif call.data == "AddBackupAccounts":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text="🔄 يرجى إرسال النسخة الاحتياطية لتتمكن من رفع الحسابات!",
        )
        bot.register_next_step_handler(AddBackupAccounts)

    # نقل الأعضاء
    elif call.data == "addshow":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text="🎯 قم بإرسال العدد الذي ترغب في إضافته من الأعضاء إلى الجروب.",      
        )
        bot.register_next_step_handler(statement)

    # نقل اعضاء مخفيين
    elif call.data == "addhide":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text="🎯 قم بإرسال العدد الذي ترغب في إضافته من الأعضاء إلى الجروب.",      
        )
        bot.register_next_step_handler(statementhide)


###################################################################
####################################################################
#اضافه حساب
async def AddAccount(client, message):    
    if "+" in message.text:
        await bot.send_message(message.chat.id,"*انتظر قليلاً... جاري الفحص ⏱*",)
        _client = Client("::memory::", in_memory=True,api_id=Config.APP_ID, api_hash=Config.API_HASH,lang_code="ar")
        await _client.connect()
        SendCode = await _client.send_code(message.text)
        await bot.send_message(message.chat.id,"*أدخل الرمز المرسل إليك 🔏*",)
        user_info = {
        "client":_client,
        "phone":message.text,
        "hash":SendCode.phone_code_hash,
        "name":message.text
                    }
        bot.register_next_step_handler(partial(sigin_up,user_info=user_info))	
    else:
        await bot.send_message(message.chat.id,"*انتظر قليلاً... جاري الفحص ⏱*")
        
async def sigin_up(client,message, user_info: dict):
    try:
        await bot.send_message(message.chat.id,"*انتظر قليلا ⏱*",)
        await user_info['client'].sign_in(user_info['phone'], user_info['hash'], phone_code=' '.join(str(message.text)))
        await bot.send_message(message.chat.id,"*تم تاكيد الحساب بنجاح ✅ *",)
        ses= await user_info['client'].export_session_string()
        database().AddAcount(ses,user_info['name'],message.chat.id)
    except SessionPasswordNeeded:
        await bot.send_message(message.chat.id,"*أدخل كلمة المرور الخاصة بحسابك 🔐*",)
        bot.register_next_step_handler( partial(AddPassword,user_info=user_info))

async def AddPassword(client,message, user_info: dict):
    try:
        await user_info['client'].check_password(message.text) 
        ses= await user_info['client'].export_session_string()
        database().AddAcount(ses,user_info['name'],message.chat.id)
        try:
            await user_info['client'].stop()
        except:
            pass
        await bot.send_message(message.chat.id,"*تم تاكيد الحساب بنجاح ✅ *",)
    except Exception as e:
        print(e)
        try:
            await user_info['client'].stop()
        except:
            pass
        await bot.send_message(message.chat.id,f"⚠️ حدث خطأ أثناء التأكيد: {e}")


#################################################
#نقل الاعضاء      
async def statement(client, message):
    num = message.text
    await bot.send_message(chat_id=message.chat.id,text="*قوم بارسال رابط الجروب المراد النقل منه*🛎",)
    Fromgrob_info = {"num":num,}
    bot.register_next_step_handler(partial(statement1,user_info=Fromgrob_info))	
    
async def statement1(client, message, user_info: dict):
    Fromgrob = message.text
    await bot.send_message(chat_id=message.chat.id,text="*قوم بارسال رابط الجروب المراد النقل له*🛎",)
    Fromgrob_info = {"Fromgrob":Fromgrob,"num":user_info['num']}
    bot.register_next_step_handler(partial(statement2,user_info=Fromgrob_info))	
    
async def statement2(client, message, user_info: dict):
    Ingrob = message.text
    await bot.send_message(chat_id=message.chat.id,text="*انتظر قليلا ⏱*",)
    getuser =await Custem().GETuser(user_info['Fromgrob']) 
    numUser = len(getuser)
    await bot.send_message(message.chat.id,f"""*تم حفظ جميع الاعضاء المتاحه بنجاح *✅

*معلومات عملية النقل 🥸😇

 الاعضاء المتاحه : {numUser} عضو 😋
النقل من  : {user_info['Fromgrob']} 🎒
النقل الي : {Ingrob} 🧳
مده الفحص : 1 ثانية ⏱

انتظر الي ان تتم العملية 🎩* """ ,)
    await Custem().ADDuser(Ingrob,user_info['Fromgrob'],bot,user_info['num'])
#################################################
async def statementhide(client, message):
    num = message.text
    await bot.send_message(chat_id=message.chat.id,text="*قوم بارسال رابط الجروب المراد النقل منه*🛎",)
    Fromgrob_info = {"num":num,}
    bot.register_next_step_handler(partial(statement1hide,user_info=Fromgrob_info))	
    
async def statement1hide(client, message, user_info: dict):
    Fromgrob = message.text
    await bot.send_message(chat_id=message.chat.id,text="*قوم بارسال رابط الجروب المراد النقل له*🛎",)
    Fromgrob_info = {"Fromgrob":Fromgrob,"num":user_info['num']}
    bot.register_next_step_handler(partial(statement2hide,user_info=Fromgrob_info))	
    
async def statement2hide(client, message, user_info: dict):
    Ingrob = message.text
    await bot.send_message(chat_id=message.chat.id,text="*انتظر قليلا ⏱*",)
    getuser =await Custem().GETuserhide(user_info['Fromgrob']) 
    numUser = len(getuser)
    await bot.send_message(message.chat.id,f"""*تم حفظ جميع الاعضاء المتاحه بنجاح *✅

*معلومات عملية النقل 🥸😇

 الاعضاء المتاحه : {numUser} عضو 😋
النقل من  : {user_info['Fromgrob']} 🎒
النقل الي : {Ingrob} 🧳
مده الفحص : 1 ثانية ⏱

انتظر الي ان تتم العملية 🎩* """ ,)
    await Custem().ADDuserhide(getuser,Ingrob,user_info['Fromgrob'],bot,user_info['num'])
#################################################
#رفع النسخه الحسابات 
async def AddBackupAccounts(client, message):
    # تأكد من أن هناك وثيقة مرفقة مع الرسالة
    if message.document.file_name.endswith("json"):
        await message.download("./FR3ONBackUp.json")
        with open("./FR3ONBackUp.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
        k = 0
        for account in data:
            try:
                # إضافة الحسابات إلى قاعدة البيانات
                database().AddAcount(account[0], account[1], account[2])
                k += 1
            except Exception as e:
                print(f"Error processing account: {e}")
                pass

        # تحديث الرسالة مع عدد الحسابات المضافة
        await client.send_message(
            chat_id=message.chat.id,
            text=f"تم رفع النسخة الاحتياطية بنجاح. حساباتك: {k} حساب.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع 🛎", callback_data="back")]])
        )
        os.remove("./FR3ONBackUp.json")
    else:
        # إذا لم يكن هناك مستند مرفق
        await client.send_message(
            chat_id=message.chat.id,
            text="*لم يتم العثور على مستند مرفق. يُرجى إرسال النسخة الاحتياطية بصيغة JSON.*",
        )
#####################################
#عرض الحسابات وحذف الحسابات
async def show_accounts_as_buttons(call, current_page, pross):
    accounts = database().backupaccounts()  # جلب الحسابات من قاعدة البيانات
    buttons_per_page = 16  # عدد الأزرار في كل صفحة
    buttons = []

    # تقسيم الحسابات إلى أزرار
    for account in accounts:
        if pross == "RemoveAccount":
            buttons.append(InlineKeyboardButton(f"الرقم: {account[1]}", callback_data=f"delaccount_{account[1]}"))
        else:
            buttons.append(InlineKeyboardButton(f"الرقم: {account[1]}", callback_data="no_action"))

    # تقسيم الأزرار إلى صفحات (4 أزرار في كل صف)
    pages = [buttons[i:i + 4] for i in range(0, len(buttons), 4)]  # عرض 4 أزرار في كل صف

    # إضافة زر التنقل بين الصفحات (التالي / السابق)
    page_buttons = []
    if current_page > 0:
        page_buttons.append(InlineKeyboardButton("السابق ◀️", callback_data=f"page_{pross}-{current_page - 1}"))
    if current_page < len(pages) - 1:
        page_buttons.append(InlineKeyboardButton("التالي ▶️", callback_data=f"page_{pross}-{current_page + 1}"))
    page_buttons.append(InlineKeyboardButton("رجوع 🛎", callback_data="back"))

    if current_page < 0 or current_page >= len(pages):
        return await call.message.edit_text(
            "*لا توجد حسابات حالياً.*",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع 🛎", callback_data="back")]])  # تعديل هنا
        )
    keyboard = [pages[current_page]]  # الصفحة الحالية
    if page_buttons:
        keyboard.append(page_buttons)  # إضافة أزرار التنقل إذا كانت موجودة

    # إرسال الرسالة مع الأزرار
    await call.message.edit_text(
        "*حساباتك المسجلة بالكامل:*",
        reply_markup=InlineKeyboardMarkup(keyboard)  # تعديل هنا
    )
######################################################################


if __name__ == "__main__":
    bot.run()