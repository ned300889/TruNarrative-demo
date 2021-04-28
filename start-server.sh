#!/usr/bin/env bash

(cd TruNarrative_siveyans_com; gunicorn TruNarrative_siveyans_com.wsgi:application --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"