# customizations.sh
# version 1.1.0

cd customizations

#systen76-wallpapers.sh
echo -e "\e[1;33mWould you like to install system76-wallpapers? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash system76-wallpapers.sh
fi

#iconpack-obsidian.sh
echo -e "\e[1;33mWould you like to install iconpack-obsidian? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash iconpack-obsidian.sh
fi

#fonts-firacode.sh
echo -e "\e[1;33mWould you like to install firacode fonts? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash fonts-firacode.sh
fi
