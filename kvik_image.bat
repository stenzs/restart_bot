@echo off
echo Inter password 2262
ssh -t vitaly@192.168.8.111 sudo "ls; cd /var/www/kvik_image/; sudo kill -9 $(sudo lsof -t -i:6001); uwsgi --socket 192.168.8.111:6001 --processes 4 --threads 2 --stats 192.168.8.111:7001 --protocol=http -w wsgi:app"
pause

