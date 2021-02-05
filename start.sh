# start.sh
# version 1.0.0

cd resources

echo -e "\e[1;33mThis script will install desktop environments, apps, customizations and copy app configs. \e[0m"
echo -e "\e[1;33mWould you like to continue? y/n \e[0m"

read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash main.sh
fi

echo -e "\e[1;33mIt is recommended to restart your computer.  \e[0m"

echo -e "\e[1;46mEnding script! \e[0m"
