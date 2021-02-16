# apps.sh
# version 1.2.0

cd apps

#office.sh
echo -e "\e[1;33mWould you like to install any office suites? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash office.sh
fi

#social.sh
echo -e "\e[1;33mWould you like to install any social apps? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash social.sh
fi

#development.sh
echo -e "\e[1;33mWould you like to install any development apps? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash development.sh
fi

#streaming.sh
echo -e "\e[1;33mWould you like to install any streaming apps? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash streaming.sh
fi

#games.sh
echo -e "\e[1;33mWould you like to install any games? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash games.sh
fi

#miscellaneous.sh
echo -e "\e[1;33mWould you like to install any miscellaneous apps? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash miscellaneous.sh
fi

#appremoval.sh
#echo -e "\e[1;33mWould you like to remove any apps? y/n \e[0m"
#read USER_INPUT
#if [ "$USER_INPUT" == "y" ]
#then
#    bash appremoval.sh
#fi
