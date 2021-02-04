# start.sh
# version 5

echo -e "\e[1;33mThis script will install broadcom drivers, desktop environments, apps and customizations for HP Pavilion 15 p087sa using Pop!_OS. \e[0m"
echo -e "\e[1;33mWould you like to continue? y/n \e[0m"

read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    cd resources
    bash main.sh
    cd ..
fi
