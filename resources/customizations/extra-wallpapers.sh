# extra-wallpapers.sh
# version 1.0.0

cd extra-wallpapers

echo -e "\e[1;45mAdding extra wallpapers! \e[0m"

cd resources
sudo cp ./wallpaper-* /usr/share/backgrounds/
cd ..

echo -e "\e[1;32mextra wallpapers have been added to /usr/share/backgrounds \e[0m"
echo -e "\e[1;32mExtra Wallpapers have been added! \e[0m"
