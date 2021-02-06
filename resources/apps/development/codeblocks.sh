# codeblocks.sh
# version 1.0.1

echo -e "\e[1;45mInstalling Code::Blocks! \e[0m"

sudo add-apt-repository -y ppa:codeblocks-devs/release
sudo apt-get update

sudo apt-get install -qqy codeblocks codeblocks-contrib

sudo add-apt-repository -ry ppa:codeblocks-devs/release

echo -e "\e[1;32mCode::Blocks has been installed! \e[0m"
