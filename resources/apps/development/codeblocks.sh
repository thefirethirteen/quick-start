# codeblocks.sh
# version 1.0.3

echo -e "\e[1;45mInstalling Code::Blocks! \e[0m"

sudo add-apt-repository -qq -y ppa:codeblocks-devs/release
sudo apt-get -qq -y update

sudo apt-get -qq -y install codeblocks codeblocks-contrib

sudo add-apt-repository -qq -y -r ppa:codeblocks-devs/release

echo -e "\e[1;32mCode::Blocks has been installed! \e[0m"
