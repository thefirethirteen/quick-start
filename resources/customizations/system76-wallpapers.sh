# system76-wallpapers
# version 3

echo -e "\e[1;45mAdding System76 Wallpapers! \e[0m"

sudo apt-add-repository -ys ppa:system76-dev/stable
sudo apt-get update

sudo apt install -y system76-wallpapers

echo -e "\e[1;32msystem76-wallpapers have been added to /usr/share/backgrounds \e[0m"
echo -e "\e[1;32mSystem76 Wallpapers have been added! \e[0m"
