# openoffice.sh
# version 1.0.0

cd openoffice

echo -e "\e[1;31mWarning: LibreOffice is incompatible with Apache OpenOffice \e[0m" 
echo -e "\e[1;31mWarning: Installing Apache OpenOffice will completely remove LibreOffice! \e[0m" 
echo -e "\e[1;31mWould you like to continue? y/n \e[0m"

read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash libreoffice-remover.sh
    bash openoffice-installer.sh
fi
