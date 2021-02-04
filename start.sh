# start.sh
# version 7

cd resources

echo -e "\e[1;33mThis script will install desktop environments, apps, customizations and copy app configs. \e[0m"
echo -e "\e[1;33mWould you like to continue? y/n \e[0m"

read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash main.sh
fi
