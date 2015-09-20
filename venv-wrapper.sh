#!/run/current-system/sw/bin/bash
cd /usr/local/rezeptionistin
. /usr/local/rezeptionistin/.venv/bin/activate
/usr/local/rezeptionistin/.venv/bin/python /usr/local/rezeptionistin/main.py -c /usr/local/rezeptionistin/config.ini 
