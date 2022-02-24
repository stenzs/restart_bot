import asyncio
import paramiko
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import keyboards as kb
import config
from database import Users
import time


DELAY = 1800
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
server_host = config.server_host


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if Users.get_or_none(number=message.from_user.id) is None:
        if int(message.from_user.id) not in config.users_security:
            await message.answer('Вас нет в вайт-листе, передайде администратору свой идентификатор: ' +
                                 str(message.from_user.id))
        else:
            Users.create(number=message.from_user.id)
            await message.answer('Добро пожаловать\nИспользуйте подсказки по команде /help')
    else:
        await message.answer('Используйте подсказки по команде /help')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    if int(message.from_user.id) not in config.users_security:
        await message.answer(
            'Вас нет в вайт-листе, передайде администратору свой идентификатор: ' + str(message.from_user.id))
    else:
        await message.answer('/status - Статус серверов\n/restart - Перезагрузить сервер')


@dp.message_handler(commands=['restart'])
async def restart(message: types.Message):
    if int(message.from_user.id) not in config.users_security:
        await message.answer(
            'Вас нет в вайт-листе, передайде администратору свой идентификатор: ' + str(message.from_user.id))
    else:
        await message.reply("Что будем перезагружать?", reply_markup=kb.markup)


@dp.message_handler(commands=['re_Kvik_chat'])
async def restart_kvik_chat(message: types.Message):
    if int(message.from_user.id) not in config.users_security:
        await message.answer(
            'Вас нет в вайт-листе, передайде администратору свой идентификатор: ' + str(message.from_user.id))
    else:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(server_host, username='vitaly', password='2262')
            await message.answer('Это ненадолго \U0000231B\U000023F3')
            try:
                stdin, stdout, stderr = ssh.exec_command('cd /var/www/kvik_chat/\nkill -9 $(lsof -t -i:6066)\necho '
                                                         '2262 | sudo -S git pull '
                                                         'https://github.com/stenzs/kvik_chat.git\nuwsgi '
                                                         '--http :6066 --gevent 1000 --http-websockets --master '
                                                         '--wsgi-file main.py --callable app')
                opt = stdout.readlines()
                opt = "".join(opt)
                opt2 = stderr.readlines()
                opt2 = "".join(opt2)
                if len(opt.strip()) != 0:
                    if len(opt) > 4000:
                        for x in range(0, len(opt), 4000):
                            await message.answer(opt[x:x + 4096])
                    else:
                        await message.answer(opt)
                if len(opt2.strip()) != 0:
                    if len(opt2) > 4000:
                        for z in range(0, len(opt2), 4000):
                            await message.answer(opt2[z:z + 4000])
                    else:
                        await message.answer(opt2)
                await message.answer('Готово\U0001F921 вызови /status')
            except Exception:
                await message.answer('При выполнении команд по SSH что-то пошло не так \U0001F631\nНо срвер мог '
                                     'перезапуститься, проверь /status')
        except Exception:
            await message.answer('Не удалось подключиться к SSH \U0001F631')


@dp.message_handler(commands=['re_Workdirect'])
async def restart_workdirect(message: types.Message):
    if int(message.from_user.id) not in config.users_security:
        await message.answer(
            'Вас нет в вайт-листе, передайде администратору свой идентификатор: ' + str(message.from_user.id))
    else:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(server_host, username='vitaly', password='2262')
            await message.answer('Минуту терпения \U0000231B\U000023F3')
            try:
                stdin, stdout, stderr = ssh.exec_command('rm -r -f /var/www/workdirect.ru/\ncd /var/www/\ngit clone '
                                                         'https://github.com/INDEX-GG/WorkDirect.git\ncd '
                                                         'WorkDirect/\nmv project-root/ /var/www/\nrm -r -f '
                                                         '/var/www/WorkDirect/\ncd /var/www/\nmv project-root/ '
                                                         'workdirect.ru\ncd /var/www/\nchmod -R 777 workdirect.ru\ncd '
                                                         '/var/www/workdirect.ru/\ncomposer update\ny')
                opt = stdout.readlines()
                opt = "".join(opt)
                opt2 = stderr.readlines()
                opt2 = "".join(opt2)
                if len(opt.strip()) != 0:
                    if len(opt) > 4000:
                        for x in range(0, len(opt), 4000):
                            await message.answer(opt[x:x + 4096])
                    else:
                        await message.answer(opt)
                if len(opt2.strip()) != 0:
                    if len(opt2) > 4000:
                        for z in range(0, len(opt2), 4000):
                            await message.answer(opt2[z:z + 4000])
                    else:
                        await message.answer(opt2)
                await message.answer('Готово\U0001F60E вызови /status')
            except Exception:
                await message.answer('При выполнении команд по SSH что-то пошло не так \U0001F631\nНо срвер мог '
                                     'перезапуститься, проверь /status')
        except Exception:
            await message.answer('Не удалось подключиться к SSH \U0001F631')


@dp.message_handler(commands=['re_Cleex_back'])
async def restart_cleex_back(message: types.Message):
    if int(message.from_user.id) not in config.users_security:
        await message.answer(
            'Вас нет в вайт-листе, передайде администратору свой идентификатор: ' + str(message.from_user.id))
    else:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(server_host, username='vitaly', password='2262')
            await message.answer('Минуту терпения \U0000231B\U000023F3')
            try:
                stdin, stdout, stderr = ssh.exec_command('cd /var/www/cleex.ru/CLEEX_back\necho 2262 | sudo -S git '
                                                         'pull --ff-only\necho 2262 | sudo -S docker build -t '
                                                         'cleex_back .\necho 2262 | sudo -S docker-compose up -d\necho '
                                                         'y | docker image prune -a')
                opt = stdout.readlines()
                opt = "".join(opt)
                opt2 = stderr.readlines()
                opt2 = "".join(opt2)
                if len(opt.strip()) != 0:
                    if len(opt) > 4000:
                        for x in range(0, len(opt), 4000):
                            await message.answer(opt[x:x + 4096])
                    else:
                        await message.answer(opt)
                if len(opt2.strip()) != 0:
                    if len(opt2) > 4000:
                        for z in range(0, len(opt2), 4000):
                            await message.answer(opt2[z:z + 4000])
                    else:
                        await message.answer(opt2)
                await message.answer('Готово\U0001F37E вызови /status')
            except Exception:
                await message.answer(
                    'При выполнении команд по SSH что-то пошло не так \U0001F631\nНо срвер мог перезапуститься, '
                    'проверь /status')
        except Exception:
            await message.answer('Не удалось подключиться к SSH \U0001F631')


@dp.message_handler(commands=['re_Kvik_search'])
async def restart_kvik_search(message: types.Message):
    if int(message.from_user.id) not in config.users_security:
        await message.answer(
            'Вас нет в вайт-листе, передайде администратору свой идентификатор: ' + str(message.from_user.id))
    else:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(server_host, username='vitaly', password='2262')
            await message.answer('Минуту терпения \U0000231B\U000023F3')
            try:
                stdin, stdout, stderr = ssh.exec_command('cd /var/www/kvik_search_engine\necho 2262 | sudo -S git '
                                                         'pull --ff-only\necho 2262 | sudo -S docker build -t '
                                                         'kvik_search .\necho 2262 | sudo -S docker-compose up '
                                                         '-d\necho y | docker image prune -a')
                opt = stdout.readlines()
                opt = "".join(opt)
                opt2 = stderr.readlines()
                opt2 = "".join(opt2)
                if len(opt.strip()) != 0:
                    if len(opt) > 4000:
                        for x in range(0, len(opt), 4000):
                            await message.answer(opt[x:x + 4096])
                    else:
                        await message.answer(opt)
                if len(opt2.strip()) != 0:
                    if len(opt2) > 4000:
                        for z in range(0, len(opt2), 4000):
                            await message.answer(opt2[z:z + 4000])
                    else:
                        await message.answer(opt2)
                await message.answer('Готово\U0001F37E вызови /status')
            except Exception:
                await message.answer(
                    'При выполнении команд по SSH что-то пошло не так \U0001F631\nНо срвер мог перезапуститься, '
                    'проверь /status')
        except Exception:
            await message.answer('Не удалось подключиться к SSH \U0001F631')


@dp.message_handler(commands=['re_Kvik_prod'])
async def restart_kvik_next(message: types.Message):
    if int(message.from_user.id) not in config.users_security:
        await message.answer(
            'Вас нет в вайт-листе, передайде администратору свой идентификатор: ' + str(message.from_user.id))
    else:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(server_host, username='vitaly', password='2262')
            await message.answer('Это минут на 10-15, тебе придет уведомление, как я закончу \U0000231B\U000023F3')
            try:
                stdin, stdout, stderr = ssh.exec_command('cd /var/www/kvik.ru/kvik_destkop\necho 2262 | sudo -S git '
                                                         'pull https://github.com/INDEX-GG/kvik_destkop.git '
                                                         'production\necho 2262 | sudo -S docker build --no-cache -t '
                                                         'kvik_production .\necho 2262 | sudo -S docker-compose up '
                                                         '-d\necho y | docker image prune -a')
                opt = stdout.readlines()
                opt = "".join(opt)
                opt2 = stderr.readlines()
                opt2 = "".join(opt2)
                if len(opt.strip()) != 0:
                    if len(opt) > 4000:
                        for x in range(0, len(opt), 4000):
                            await message.answer(opt[x:x + 4096])
                    else:
                        await message.answer(opt)
                if len(opt2.strip()) != 0:
                    if len(opt2) > 4000:
                        for z in range(0, len(opt2), 4000):
                            await message.answer(opt2[z:z + 4000])
                    else:
                        await message.answer(opt2)
                await message.answer('Готово\U0001F917 вызови /status')
            except Exception:
                await message.answer('При выполнении команд по SSH что-то пошло не так \U0001F631\nНо срвер мог'
                                     ' перезапуститься, проверь /status')
        except Exception:
            await message.answer('Не удалось подключиться к SSH \U0001F631')


@dp.message_handler(commands=['re_Kvik_dev'])
async def restart_kvik_next(message: types.Message):
    if int(message.from_user.id) not in config.users_security:
        await message.answer(
            'Вас нет в вайт-листе, передайде администратору свой идентификатор: ' + str(message.from_user.id))
    else:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(server_host, username='vitaly', password='2262')
            await message.answer('Придется немного подождать, тебе придет уведомление, '
                                 'как я закончу \U0000231B\U000023F3')
            try:
                stdin, stdout, stderr = ssh.exec_command('cd /var/www/kvik_dev_test/kvik_test\necho 2262 | sudo -S git '
                                                         'pull --ff-only\necho 2262 | sudo -S docker build --no-cache '
                                                         '-t kvik_dev_test .\necho 2262 | sudo -S docker-compose up '
                                                         '-d\necho y | docker image prune -a')
                opt = stdout.readlines()
                opt = "".join(opt)
                opt2 = stderr.readlines()
                opt2 = "".join(opt2)
                if len(opt.strip()) != 0:
                    if len(opt) > 4000:
                        for x in range(0, len(opt), 4000):
                            await message.answer(opt[x:x + 4096])
                    else:
                        await message.answer(opt)
                if len(opt2.strip()) != 0:
                    if len(opt2) > 4000:
                        for z in range(0, len(opt2), 4000):
                            await message.answer(opt2[z:z + 4000])
                    else:
                        await message.answer(opt2)
                await message.answer('Готово\U0001F978 вызови /status')
            except Exception:
                print(Exception)
                await message.answer(
                    'При выполнении команд по SSH что-то пошло не так \U0001F631\nНо срвер мог перезапуститься, '
                    'проверь /status')
        except Exception:
            await message.answer('Не удалось подключиться к SSH \U0001F631')


@dp.message_handler(commands=['re_Cleex_image'])
async def restart_cleex_image(message: types.Message):
    if int(message.from_user.id) not in config.users_security:
        await message.answer(
            'Вас нет в вайт-листе, передайде администратору свой идентификатор: ' + str(message.from_user.id))
    else:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(server_host, username='vitaly', password='2262')
            await message.answer('1...2...3... \U0001F406')
            try:
                stdin, stdout, stderr = ssh.exec_command('cd /var/www/cleex_image/\nkill -9 $(lsof -t -i:7050)\nkill '
                                                         '-9 $(lsof -t -i:7051)\nuwsgi -M --socket ' +
                                                         str(server_host) +
                                                         ':7050 --processes 4 --threads 2 --stats ' +
                                                         str(server_host) +
                                                         ':7051 --protocol=http -w wsgi:app')
                opt = stdout.readlines()
                opt = "".join(opt)
                opt2 = stderr.readlines()
                opt2 = "".join(opt2)
                if len(opt.strip()) != 0:
                    if len(opt) > 4000:
                        for x in range(0, len(opt), 4000):
                            await message.answer(opt[x:x + 4096])
                    else:
                        await message.answer(opt)
                if len(opt2.strip()) != 0:
                    if len(opt2) > 4000:
                        for z in range(0, len(opt2), 4000):
                            await message.answer(opt2[z:z + 4000])
                    else:
                        await message.answer(opt2)
                await message.answer('Готово\U0001F44D вызови /status')
            except Exception:
                await message.answer('При выполнении команд по SSH что-то пошло не так \U0001F631\nНо срвер мог '
                                     'перезапуститься, проверь /status')
        except Exception:
            await message.answer('Не удалось подключиться к SSH \U0001F631')


@dp.message_handler(commands=['re_Kvik_image'])
async def restart_kvik_image(message: types.Message):
    if int(message.from_user.id) not in config.users_security:
        await message.answer(
            'Вас нет в вайт-листе, передайде администратору свой идентификатор: ' + str(message.from_user.id))
    else:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        await message.answer('1...2...3... \U0001F406')
        try:
            ssh.connect(server_host, username='vitaly', password='2262')
            try:
                stdin, stdout, stderr = ssh.exec_command('cd /var/www/kvik_image/\nkill -9 $(lsof -t -i:6001)\nkill '
                                                         '-9 $(lsof -t -i:7001)\nuwsgi -M --socket ' +
                                                         str(server_host) +
                                                         ':6001 --processes 4 --threads 2 --stats ' +
                                                         str(server_host) +
                                                         ':7001 --protocol=http -w wsgi:app')
                opt = stdout.readlines()
                opt = "".join(opt)
                opt2 = stderr.readlines()
                opt2 = "".join(opt2)
                if len(opt.strip()) != 0:
                    if len(opt) > 4000:
                        for x in range(0, len(opt), 4000):
                            await message.answer(opt[x:x + 4096])
                    else:
                        await message.answer(opt)
                if len(opt2.strip()) != 0:
                    if len(opt2) > 4000:
                        for z in range(0, len(opt2), 4000):
                            await message.answer(opt2[z:z + 4000])
                    else:
                        await message.answer(opt2)
                await message.answer('Готово\U0001F973 вызови /status')
            except Exception:
                await message.answer('При выполнении команд по SSH что-то пошло не так \U0001F631\nНо срвер мог '
                                     'перезапуститься, проверь /status')
        except Exception:
            await message.answer('Не удалось подключиться к SSH \U0001F631')


@dp.message_handler(commands=['re_Redis_cache'])
async def restart_kvik_image(message: types.Message):
    if int(message.from_user.id) not in config.users_security:
        await message.answer(
            'Вас нет в вайт-листе, передайде администратору свой идентификатор: ' + str(message.from_user.id))
    else:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        await message.answer('1...2...3... \U0001F406')
        try:
            ssh.connect(server_host, username='vitaly', password='2262')
            try:
                stdin, stdout, stderr = ssh.exec_command('cd /var/www/redis_cache/\nkill -9 $(lsof -t -i:6550)\nkill '
                                                         '-9 $(lsof -t -i:7550)\nuwsgi -M --socket ' +
                                                         str(server_host) +
                                                         ':6550 --processes 4 --threads 2 --stats ' +
                                                         str(server_host) +
                                                         ':7550 --protocol=http -w wsgi:app')
                opt = stdout.readlines()
                opt = "".join(opt)
                opt2 = stderr.readlines()
                opt2 = "".join(opt2)
                if len(opt.strip()) != 0:
                    if len(opt) > 4000:
                        for x in range(0, len(opt), 4000):
                            await message.answer(opt[x:x + 4096])
                    else:
                        await message.answer(opt)
                if len(opt2.strip()) != 0:
                    if len(opt2) > 4000:
                        for z in range(0, len(opt2), 4000):
                            await message.answer(opt2[z:z + 4000])
                    else:
                        await message.answer(opt2)
                await message.answer('Готово\U0001F973 вызови /status')
            except Exception:
                await message.answer('При выполнении команд по SSH что-то пошло не так \U0001F631\nНо срвер мог '
                                     'перезапуститься, проверь /status')
        except Exception:
            await message.answer('Не удалось подключиться к SSH \U0001F631')


@dp.message_handler(commands=['ports'])
async def get_ports(message: types.Message):
    if int(message.from_user.id) not in config.users_security:
        await message.answer(
            'Вас нет в вайт-листе, передайде администратору свой идентификатор: ' + str(message.from_user.id))
    else:
        await message.answer('\U000026AA Workdirect  --  ' +
                             '\n\U000026AA Cleex (back)  --  6011' +
                             '\n\U000026AA Cleex (image)  --  7050' +
                             '\n\U000026AA Kvik (prod)  --  3000' +
                             '\n\U000026AA Kvik (dev)  --  4000' +
                             '\n\U000026AA Kvik (image)  --  6001' +
                             '\n\U000026AA Kvik (chat)  --  6066' +
                             '\n\U000026AA Kvik (search hints)  --  6555' +
                             '\n\U000026AA Redis cache  --  6550'
                             )


@dp.message_handler(commands=['status'])
async def status(message: types.Message):
    if int(message.from_user.id) not in config.users_security:
        await message.answer(
            'Вас нет в вайт-листе, передайде администратору свой идентификатор: ' + str(message.from_user.id))
    else:
        try:
            response1 = requests.get("http://" + str(server_host) + ":3070")
            if response1.status_code != 200:
                status1 = '\U0001F4A4\U0001F4A4\U0001F4A4'
            else:
                status1 = '\U00002714\U00002714\U00002714'
        except Exception:
            status1 = '\U0001F4A4\U0001F4A4\U0001F4A4'
        try:
            response2 = requests.get("http://" + str(server_host) + ":6011")
            if response2.status_code != 200:
                status2 = '\U0001F4A4\U0001F4A4\U0001F4A4'
            else:
                status2 = '\U00002714\U00002714\U00002714'
        except Exception:
            status2 = '\U0001F4A4\U0001F4A4\U0001F4A4'
        try:
            response3 = requests.get("http://" + str(server_host) + ":7050")
            if response3.status_code != 200:
                status3 = '\U0001F4A4\U0001F4A4\U0001F4A4'
            else:
                status3 = '\U00002714\U00002714\U00002714'
        except Exception:
            status3 = '\U0001F4A4\U0001F4A4\U0001F4A4'
        try:
            response4 = requests.get("http://" + str(server_host) + ":3000")
            if response4.status_code != 200:
                status4 = '\U0001F4A4\U0001F4A4\U0001F4A4'
            else:
                status4 = '\U00002714\U00002714\U00002714'
        except Exception:
            status4 = '\U0001F4A4\U0001F4A4\U0001F4A4'
        try:
            response5 = requests.get("http://" + str(server_host) + ":4000")
            if response5.status_code != 200:
                status5 = '\U0001F4A4\U0001F4A4\U0001F4A4'
            else:
                status5 = '\U00002714\U00002714\U00002714'
        except Exception:
            status5 = '\U0001F4A4\U0001F4A4\U0001F4A4'
        try:
            response6 = requests.get("http://" + str(server_host) + ":6001")
            if response6.status_code != 200:
                status6 = '\U0001F4A4\U0001F4A4\U0001F4A4'
            else:
                status6 = '\U00002714\U00002714\U00002714'
        except Exception:
            status6 = '\U0001F4A4\U0001F4A4\U0001F4A4'
        try:
            response7 = requests.get("http://" + str(server_host) + ":6066")
            if response7.status_code != 200:
                status7 = '\U0001F4A4\U0001F4A4\U0001F4A4'
            else:
                status7 = '\U00002714\U00002714\U00002714'
        except Exception:
            status7 = '\U0001F4A4\U0001F4A4\U0001F4A4'
        try:
            response8 = requests.get("http://" + str(server_host) + ":6550")
            if response8.status_code != 200:
                status8 = '\U0001F4A4\U0001F4A4\U0001F4A4'
            else:
                status8 = '\U00002714\U00002714\U00002714'
        except Exception:
            status8 = '\U0001F4A4\U0001F4A4\U0001F4A4'
        try:
            response9 = requests.get("http://" + str(server_host) + ":6555")
            if response9.status_code != 200:
                status9 = '\U0001F4A4\U0001F4A4\U0001F4A4'
            else:
                status9 = '\U00002714\U00002714\U00002714'
        except Exception:
            status9 = '\U0001F4A4\U0001F4A4\U0001F4A4'
        len1 = 13
        len2 = 10
        len3 = 8
        len4 = 13
        len5 = 15
        len6 = 11
        len7 = 14
        len8 = 11
        len9 = 9
        await message.answer('\U000026AA Workdirect' + ' ' * len1 + status1 +
                             '\n\U000026AA Cleex (back)' + ' ' * len2 + status2 +
                             '\n\U000026AA Cleex (image)' + ' ' * len3 + status3 +
                             '\n\U000026AA Kvik (prod)' + ' ' * len4 + status4 +
                             '\n\U000026AA Kvik (dev)' + ' ' * len5 + status5 +
                             '\n\U000026AA Kvik (image)' + ' ' * len6 + status6 +
                             '\n\U000026AA Kvik (chat)' + ' ' * len7 + status7 +
                             '\n\U000026AA Redis cache' + ' ' * len8 + status8 +
                             '\n\U000026AA Kvik (search)' + ' ' * len9 + status9 +
                             '\n\n/restart для перезапуска')


async def listen():
    stack = []
    try:
        response1 = requests.get("http://" + str(server_host) + ":3070")
        if response1.status_code != 200:
            status1 = 'false'
        else:
            status1 = 'true'
    except Exception:
        status1 = 'false'
    stack.append(status1)
    try:
        response2 = requests.get("http://" + str(server_host) + ":6011")
        if response2.status_code != 200:
            status2 = 'false'
        else:
            status2 = 'true'
    except Exception:
        status2 = 'false'
    stack.append(status2)
    try:
        response3 = requests.get("http://" + str(server_host) + ":7050")
        if response3.status_code != 200:
            status3 = 'false'
        else:
            status3 = 'true'
    except Exception:
        status3 = 'false'
    stack.append(status3)
    try:
        response4 = requests.get("http://" + str(server_host) + ":3000")
        if response4.status_code != 200:
            status4 = 'false'
        else:
            status4 = 'true'
    except Exception:
        status4 = 'false'
    stack.append(status4)
    try:
        response5 = requests.get("http://" + str(server_host) + ":4000")
        if response5.status_code != 200:
            status5 = 'false'
        else:
            status5 = 'true'
    except Exception:
        status5 = 'false'
    stack.append(status5)
    try:
        response6 = requests.get("http://" + str(server_host) + ":6001")
        if response6.status_code != 200:
            status6 = 'false'
        else:
            status6 = 'true'
    except Exception:
        status6 = 'false'
    stack.append(status6)
    try:
        response7 = requests.get("http://" + str(server_host) + ":6066")
        if response7.status_code != 200:
            status7 = 'false'
        else:
            status7 = 'true'
    except Exception:
        status7 = 'false'
    stack.append(status7)
    try:
        response8 = requests.get("http://" + str(server_host) + ":6550")
        if response8.status_code != 200:
            status8 = 'false'
        else:
            status8 = 'true'
    except Exception:
        status8 = 'false'
    stack.append(status8)
    try:
        response9 = requests.get("http://" + str(server_host) + ":6555")
        if response9.status_code != 200:
            status9 = 'false'
        else:
            status9 = 'true'
    except Exception:
        status9 = 'false'
    stack.append(status9)
    if 'false' in stack:
        users_selected = (Users.select()).dicts().execute()
        for user in users_selected:
            message = 'С одним из серверов что-то не так, проверь /status'
            send_text = 'https://api.telegram.org/bot' + config.TOKEN + '/sendMessage?chat_id=' + \
                        str(user['number']) + '&text=' + message
            requests.get(send_text)
            time.sleep(1)


def repeat(coro, loop):
    asyncio.ensure_future(coro(), loop=loop)
    loop.call_later(DELAY, repeat, coro, loop)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_later(DELAY, repeat, listen, loop)
    executor.start_polling(dp, loop=loop, skip_updates=True)
