# wine.sh
# version 1.0.1

echo -e "\e[1;45mInstalling wine! \e[0m"

sudo dpkg --add-architecture i386

cd resources
wget -nc https://dl.winehq.org/wine-builds/winehq.key
sudo apt-key add winehq.key
rm -f winehq.key
cd ..

sudo add-apt-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ groovy main'
sudo apt-get update

sudo apt install -qqy --install-recommends winehq-stable

echo -e "\e[1;32mwinehq-stable has been installed to /opt/wine-stable \e[0m"
echo -e "\e[1;32mwine has been installed! \e[0m"
