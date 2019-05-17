#!/usr/bin/bash

echo "===================================="
echo "=    ALICIA PROJECT INSTALATION    ="
echo "=  VERSION : 1.1                   ="
echo "=  AUTHOR  : SECURITY007           ="
echo "=  COPYRIGHT (c) 2019              ="
echo "===================================="

echo " "
echo "installing python3"
sudo apt-get install python3
echo "installing python3 pip"
sudo apt-get install python3-pip
echo "installing module"
python3 -m pip install SpeechRecognition
python3 -m pip install wikipedia
python3 -m pip install gtts
python3 -m pip install requests
python3 -m pip install playsound

echo "instalation done..."
echo " "
echo "PENTING:"
echo "sebelum memulai, silahkan edit pada bagian #credential email pada script alicia.py dan isikan username dan password gmail kalian"
echo " "
echo "======HAVE A NICE DAY======"