import asyncio
import paramiko
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import keyboards as kb
import config
from database import Users

DELAY = 180

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if Users.get_or_none(number=message.from_user.id) is None:
        Users.create(number=message.from_user.id)
    await message.answer('Добро пожаловать\nИспользуйте подсказки по команде /help')


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer('/status - Статус серверов\n/restart - Перезагрузить сервер')


@dp.message_handler(commands=['restart'])
async def process_hi5_command(message: types.Message):
    await message.reply("Что будем перезагружать?", reply_markup=kb.markup)


@dp.message_handler(commands=['re_Workdirect'])
async def restart_cleex_back(message: types.Message):
    await message.answer('перезагружаю Workdirect...\nПодожди 5 минут и вызови /status')


@dp.message_handler(commands=['re_Cleex_back'])
async def restart_cleex_back(message: types.Message):
    await message.answer('перезагружаю Cleex back...\nПодожди 5 минут и вызови /status')


@dp.message_handler(commands=['re_Cleex_image'])
async def restart_cleex_back(message: types.Message):
    cmd_list = ['cd .', 'ls', 'cd /var/www/cleex_image/', 'ls', 'sudo kill -9 $(sudo lsof -t -i:7050)', '']
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect('192.168.8.111', username='vitaly', password='2262')
        print('connected')
        for command in cmd_list:
            await message.answer("> " + command)
            stdin, stdout, stderr = ssh.exec_command('ls -l')
            opt = stdout.readlines()
            opt = "".join(opt)
            print(opt)
        await message.answer('Готово, вызови /status')
    except Exception:
        await message.answer('Не удалось подключиться к SSH \U0001F631')


@dp.message_handler(commands=['re_Kvik_next'])
async def restart_cleex_back(message: types.Message):
    await message.answer('перезагружаю Kvik next...\nПодожди 5-10 минут и вызови /status')


@dp.message_handler(commands=['re_Kvik_image'])
async def restart_cleex_back(message: types.Message):
    cmd_list = ['cd /var/www/kvik_image/', 'sudo kill -9 $(sudo lsof -t -i:6001)', 'uwsgi --socket 192.168.8.111:6001 --processes 4 --threads 2 --stats 192.168.8.111:7001 --protocol=http -w wsgi:app']
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect('192.168.8.111', username='vitaly', password='2262')
        print('connected')
        for command in cmd_list:
            await message.answer("> " + command)
            stdin, stdout, stderr = ssh.exec_command(command)
            opt = stdout.readlines()
            opt = "".join(opt)
            print(opt)
        await message.answer('Готово, вызови /status')
    except Exception:
        await message.answer('Не удалось подключиться к SSH \U0001F631')


@dp.message_handler(commands=['status'])
async def start(message: types.Message):
    if Users.get_or_none(number=message.from_user.id) is None:
        Users.create(number=message.from_user.id)
    try:
        response1 = requests.get("http://192.168.8.111:3070")
        if response1.status_code != 200:
            status1 = '\U0001F4A4\U0001F4A4\U0001F4A4'
        else:
            status1 = '\U00002714\U00002714\U00002714'
    except Exception:
        status1 = '\U0001F4A4\U0001F4A4\U0001F4A4'
    try:
        response2 = requests.get("http://192.168.8.111:6011")
        if response2.status_code != 200:
            status2 = '\U0001F4A4\U0001F4A4\U0001F4A4'
        else:
            status2 = '\U00002714\U00002714\U00002714'
    except Exception:
        status2 = '\U0001F4A4\U0001F4A4\U0001F4A4'
    try:
        response3 = requests.get("http://192.168.8.111:7050")
        if response3.status_code != 200:
            status3 = '\U0001F4A4\U0001F4A4\U0001F4A4'
        else:
            status3 = '\U00002714\U00002714\U00002714'
    except Exception:
        status3 = '\U0001F4A4\U0001F4A4\U0001F4A4'
    try:
        response4 = requests.get("http://192.168.8.111:3000")
        if response4.status_code != 200:
            status4 = '\U0001F4A4\U0001F4A4\U0001F4A4'
        else:
            status4 = '\U00002714\U00002714\U00002714'
    except Exception:
        status4 = '\U0001F4A4\U0001F4A4\U0001F4A4'
    try:
        response5 = requests.get("http://192.168.8.111:6001")
        if response5.status_code != 200:
            status5 = '\U0001F4A4\U0001F4A4\U0001F4A4'
        else:
            status5 = '\U00002714\U00002714\U00002714'
    except Exception:
        status5 = '\U0001F4A4\U0001F4A4\U0001F4A4'
    len1 = 13
    len2 = 10
    len3 = 8
    len4 = 14
    len5 = 11
    await message.answer('\U000026AA Workdirect' + ' ' * len1 + status1 + '\n\U000026AA Cleex (back)' + ' ' * len2 + status2 + '\n\U000026AA Cleex (image)' + ' ' * len3 + status3 + '\n\U000026AA Kvik (next)' + ' ' * len4 + status4 + '\n\U000026AA Kvik (image)' + ' ' * len5 + status5)


# async def listen():
#     users_selected = (Users.select()).dicts().execute()
#     for user in users_selected:
#         message = '123456'
#         send_text = 'https://api.telegram.org/bot' + config.TOKEN + '/sendMessage?chat_id=' + str(user['number']) + '&text=' + message
#         response = requests.get(send_text)
#         print(response.json())

def repeat(coro, loop):
    asyncio.ensure_future(coro(), loop=loop)
    loop.call_later(DELAY, repeat, coro, loop)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_later(DELAY, repeat, listen, loop)
    executor.start_polling(dp, loop=loop, skip_updates=True)