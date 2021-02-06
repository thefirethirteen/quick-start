# spotify.sh
# version 1.1.1

echo -e "\e[1;45mInstalling Spotify! \e[0m"

curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg
sudo apt-key -qq add -
sudo tee /etc/apt/sources.list.d/spotify.list

sudo apt-get -qq update

sudo apt-get -qq -y install spotify-client

echo -e "\e[1;32mSpotify has been installed! \e[0m"
