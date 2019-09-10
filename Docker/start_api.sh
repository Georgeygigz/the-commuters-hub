#!/bin/bash

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

echo " "
echo " "
echo "<<<<<<<< Database Setup and Migrations Starts >>>>>>>>>"

# Run database migrations
python3 manage.py db migrate

echo " "
echo " "
echo "<<<<<<<< Database Setup and upgrade db >>>>>>>>>"

# Run database migrations
python3 manage.py db upgrade

echo " "
echo " "
echo "<<<<<<<<<<<<<<<<<<<< START API >>>>>>>>>>>>>>>>>>>>>>>>"
sleep 3

# Start the API
python run.py
