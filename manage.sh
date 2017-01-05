#!/usr/bin/env bash

if [ "${1}" == "" ] || [ "${1}" == "help" ]; then

    echo "manage.sh <option>"
    echo ""
    echo "start"
    echo "stop"
    echo "package"
    echo "help"
    echo ""

elif [ "${1}" == "start" ]; then

    echo "starting..."
fi
