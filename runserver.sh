#!/bin/bash

if [ -e "website/local_settings.py" ]
then
    echo "cp website/settings.py website/settings_bak.py"
    cp website/settings.py website/settings_bak.py
    cp website/local_settings.py website/settings.py
fi

python manage.py runserver 127.0.0.1:8000

