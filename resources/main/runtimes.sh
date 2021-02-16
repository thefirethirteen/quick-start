# runtimes.sh
# version 1.0.0

cd runtimes

#java.sh
echo -e "\e[1;33mWould you like to install java? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash java.sh
fi
