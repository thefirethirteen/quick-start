# miscellaneous.sh
# version 1

cd miscellaneous

#wine.sh
echo -e "\e[1;33mWould you like to install wine? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash wine.sh
fi
