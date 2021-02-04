# streaming.sh
# version 1

cd streaming

#spotify.sh
echo -e "\e[1;33mWould you like to install Spotify? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash spotify.sh
fi
