# wine.sh
# version 1.1.2

sudo dpkg --add-architecture i386

wget -nc https://dl.winehq.org/wine-builds/winehq.key
sudo apt-key add winehq.key
rm -f winehq.key

sudo add-apt-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ groovy main'
sudo apt-get update

sudo apt-get -y install --install-recommends winehq-stable
