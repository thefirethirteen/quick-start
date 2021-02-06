# spotify.sh
# version 1.0.1

echo -e "\e[1;45mInstalling Spotify! \e[0m"

curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | sudo apt-key add -
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list

sudo apt-get update

sudo apt-get install -qqy spotify-client

echo -e "\e[1;32mSpotify has been installed! \e[0m"
