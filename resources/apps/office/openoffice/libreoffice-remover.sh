# libreoffice-remover.sh
# version 1.0.0

echo -e "\e[1;45mRemoving LibreOffice! \e[0m"

sudo apt-get remove -qqy "libreoffice*"
sudo apt-get autoremove -qqy

echo -e "\e[1;32mLibreOffice has been removed! \e[0m"
