# broadcom.sh
# version 9

cd broadcom

#broadcom-wireless.sh
echo -e "\e[1;33mWould you like to install Broadcom Wireless Internet Drivers? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash broadcom-wireless.sh
fi

#broadcom-bluetooth.sh
echo -e "\e[1;33mWould you like to install Broadcom Bluetooth Drivers? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash broadcom-bluetooth.sh
fi

