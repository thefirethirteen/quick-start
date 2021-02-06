# codeblocks.sh
# version 1.0.2

echo -e "\e[1;45mInstalling Code::Blocks! \e[0m"

sudo add-apt-repository -qqy ppa:codeblocks-devs/release
sudo apt-get update

sudo apt-get install -qqy codeblocks codeblocks-contrib

sudo add-apt-repository -qqy -r ppa:codeblocks-devs/release

echo -e "\e[1;32mCode::Blocks has been installed! \e[0m"
