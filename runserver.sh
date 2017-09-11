#!/bin/bash

if [ -e "website/local_settings.py" ]
then
    echo "cp website/settings.py website/settings_bak.py"
    cp website/settings.py website/settings_bak.py
    cp website/local_settings.py website/settings.py
fi

sudo python3 manage.py runserver 0.0.0.0:80
