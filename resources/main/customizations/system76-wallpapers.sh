# system76-wallpapers
# version 1.1.2

echo -e "\e[1;45mAdding System76 Wallpapers! \e[0m"

sudo apt-add-repository -y -s ppa:system76-dev/stable
sudo apt-get -qq update

sudo apt-get -qq -y install system76-wallpapers

echo -e "\e[1;32mThe wallpapers from system76-wallpapers have been added to /usr/share/backgrounds \e[0m"
