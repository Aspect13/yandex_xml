#!/bin/bash
cd /home/ad/yandex_xml
source venv/bin/activate
sudo uwsgi --ini uwsgi.ini

