# office.sh
# version 1

cd office

#openoffice.sh
echo -e "\e[1;33mWould you like to install Apache OpenOffice? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash openoffice.sh
fi
