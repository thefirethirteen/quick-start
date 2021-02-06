# wine.sh
# version 1.1.0

echo -e "\e[1;45mInstalling wine! \e[0m"

sudo dpkg --add-architecture i386

wget -nc https://dl.winehq.org/wine-builds/winehq.key
sudo apt-key -qq add winehq.key
rm -f winehq.key

sudo add-apt-repository -qq -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ groovy main'
sudo apt-get -qq update

sudo apt-get -qq -y install --install-recommends winehq-stable

echo -e "\e[1;32mwinehq-stable has been installed to /opt/wine-stable \e[0m"
