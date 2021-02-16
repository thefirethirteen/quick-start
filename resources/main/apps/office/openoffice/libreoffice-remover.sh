# libreoffice-remover.sh
# version 1.0.1

echo -e "\e[1;45mRemoving LibreOffice! \e[0m"

sudo apt-get -qq -y remove "libreoffice*"
sudo apt-get -qq -y autoremove

echo -e "\e[1;32mLibreOffice has been removed! \e[0m"
