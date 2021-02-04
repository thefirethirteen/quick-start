# apps.sh
# version 17

cd apps

#office.sh
echo -e "\e[1;33mWould you like to install any office suites? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash office.sh
fi

#social.sh
echo -e "\e[1;33mWould you like to install any social apps? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash social.sh
fi

#development.sh
echo -e "\e[1;33mWould you like to install any development apps? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash development.sh
fi

#spotify.sh
echo -e "\e[1;33mWould you like to install Spotify? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash spotify.sh
fi

#steam.sh
echo -e "\e[1;33mWould you like to install Steam? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash steam.sh
fi

#wine.sh
echo -e "\e[1;33mWould you like to install wine? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash wine.sh
fi


