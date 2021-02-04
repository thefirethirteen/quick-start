# libreoffice-remover.sh
# version 2

echo -e "\e[1;45mRemoving LibreOffice! \e[0m"

sudo apt-get remove --purge libreoffice* libexttextcat-data*
sudo apt-get autoremove

echo -e "\e[1;32mLibreOffice has been removed! \e[0m"
