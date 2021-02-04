# social.sh
# version 1

cd social

#discord.sh
echo -e "\e[1;33mWould you like to install discord? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash discord.sh
fi
