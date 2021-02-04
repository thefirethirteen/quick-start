# apps.sh
# version 16

cd apps

#discord.sh
echo -e "\e[1;33mWould you like to install discord? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash discord.sh
fi

#codeblocks.sh
echo -e "\e[1;33mWould you like to install Code::Blocks? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash codeblocks.sh
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

#office.sh
echo -e "\e[1;33mWould you like to install any office suites? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash office.sh
fi
