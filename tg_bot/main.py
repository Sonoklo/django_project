import aiogram 
import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from db import get_admin, change_tg_active, get_admins, get_all_not_checked, change_tg_check

bot = Bot(token="Your token")
dp = Dispatcher()
router = Router()

async def send_new_orders():
    while True:
        orders = get_all_not_checked()
        if orders:
            admins = get_admins()
            if admins:
                for order in orders:
                    id = order[0]
                    name = order[1]
                    date = order[4]
                    time = order[5]
                    for admin in admins:    
                        await bot.send_message(chat_id=admin[1], text=f"Id:{id}\nname:{name}\ndate:{date}\ntime:{time}")
                        change_tg_check(id)
        await asyncio.sleep(30)
        
@router.message(CommandStart)
async def active_admin_tg(message: types.Message):
    user_id = message.from_user.id
    print("User ID:", user_id)
    
    admin = get_admin(user_id)
    print(admin)
    if admin:
        change_tg_active(user_id)
        await message.answer("Аккаунт активирован")


dp.include_router(router)


async def main():
    print(1)
    asyncio.create_task(send_new_orders())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
