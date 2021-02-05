# main.sh
# version 1.0.0

sudo apt-get update

#package update
echo -e "\e[1;33mWould you like to install all package updates available? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    sudo apt-get -qqy --allow-downgrades upgrade
fi

#runtimes.sh
echo -e "\e[1;33mWould you like to install any runtimes? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash runtimes.sh
fi

#de.sh
echo -e "\e[1;33mWould you like to install any desktop environments? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash de.sh
fi

#apps.sh
echo -e "\e[1;33mWould you like to install any apps? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash apps.sh
fi

#customizations.sh
echo -e "\e[1;33mWould you like to install any customizations? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash customizations.sh
fi

#config.sh
echo -e "\e[1;33mWould you like to copy configs? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash config.sh
fi

#manual.sh
echo -e "\e[1;33mWould you like to copy manuals? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash manual.sh
fi


#remove unnecessary packages
sudo apt autoremove -y
