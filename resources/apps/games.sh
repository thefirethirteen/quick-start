# games.sh
# version 1.0.0

cd games

#steam.sh
echo -e "\e[1;33mWould you like to install Steam? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash steam.sh
fi
