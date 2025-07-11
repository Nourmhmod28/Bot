import logging
from datetime import datetime, timedelta
import pytz
from pyrogram import Client
from prayer_times_calculator import PrayerTimesCalculator
from apscheduler.schedulers.background import BackgroundScheduler

#Dev. MD 🇸🇾
#Ramadan_Karem

API_TOKEN = '8174742142:AAHraz-UFR--f4JNNFLwsASEYxtyDAmFT0U'

YOUR_API_ID = 28602152
YOUR_API_HASH = 'eaa59761120559fa3e3655578bbb9128'

CHAT_ID = 'الشات يلي تريد ترسله الرسائل'

logging.basicConfig(level=logging.INFO)

syria = Client('prayer_times_bot', api_id=YOUR_API_ID, api_hash=YOUR_API_HASH, bot_token=API_TOKEN)

ARAB_COUNTRIES = {
    'syria': {'latitude': 35.0, 'longitude': 38.0, 'timezone': 'Asia/Damascus'},
    #حط دولتك والموقع الجغرافي
}

def send_prayer_notification(country, prayer_time):
    notification_text = f"It's time for Maghrib prayer in {country.capitalize()}."
    syria.send_message(chat_id=CHAT_ID, text=notification_text)

def check_maghrib_times():
    current_time = datetime.now(pytz.UTC)
    for country, location in ARAB_COUNTRIES.items():
        calculator = PrayerTimesCalculator(
            latitude=location['latitude'],
            longitude=location['longitude'],
            timezone=location['timezone']
        )
        prayer_times = calculator.fetch_prayer_times_for_date(current_time)
        maghrib_time = prayer_times['maghrib'].replace(tzinfo=pytz.UTC)
        
        if current_time >= maghrib_time and current_time <= (maghrib_time + timedelta(minutes=1)):
            send_prayer_notification(country, maghrib_time)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_maghrib_times, 'interval', minutes=1)
    scheduler.start()

if __name__ == "__main__":
    start_scheduler()
    syria.run()