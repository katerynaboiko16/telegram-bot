import asyncio
from aiogram import Bot, Dispatcher, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import os

# Get credentials from Railway environment variables
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()

# First Poll Function (09:00 AM)
async def send_first_poll():
    await bot.send_poll(
        chat_id=CHAT_ID,
        question="Щоденні практики",
        options=[
            "🌱 медитація Махамудра",
            "🌱 медитація Wonder Money",
            "🌱 конверт КП",
            "🌱 конверт Свобода від фін боргів/Марнотратства",
            "🌱 конверт Фін подушка"
        ],
        allows_multiple_answers=True,
        is_anonymous=False
    )

# Second Poll Function (09:10 AM)
async def send_second_poll():
    await bot.send_poll(
        chat_id=CHAT_ID,
        question="Наступні практики, ви чергуєте, і робите мінімум 1 практику в день зі списку 👇",
        options=[
            "💎 практика Fake it until you make it",
            "💎 практика Кармічний інвестор",
            "💎 практика відбілювання людей з чорного списку",
            "💎 практика Присвята",
            "💎 практика Ізобілія",
            "💎 Тонг Ленг собі, інших, та миттєвий Тонг Ленг"
        ],
        allows_multiple_answers=True,
        is_anonymous=False
    )

# Schedule First Poll (09:00 AM)
@scheduler.scheduled_job("cron", hour=9, minute=0)
async def scheduled_task_first_poll():
    await send_first_poll()

# Schedule Second Poll (09:10 AM)
@scheduler.scheduled_job("cron", hour=9, minute=10)
async def scheduled_task_second_poll():
    await send_second_poll()

async def on_startup(_):
    scheduler.start()
    print("Bot is running...")

async def main():
    await on_startup(None)
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
