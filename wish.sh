#!/system/bin/sh

if [[ $1 = "-h" ]]
then
	python help.py
elif [[ $# -eq 2 ]]
then
	if [[ $1 = "animation" ]]
	then
		clear
  play-audio wish.mp3 &
		python animation.py $2
 elif [[ $1 = "email" ]]
 then
		clear
		python emailsend.py $2
 else 
  python help.py
	fi
else 
	python help.py
fi
