# codeblocks.sh
# version 1.0.0

cd codeblocks

echo -e "\e[1;33mHave you installed firacode? \e[0m"
echo -e "\e[1;33mHave you installed Code::Blocks \e[0m"
echo -e "\e[1;33mHave you run Code::Blocks at least once? \e[0m"
echo -e "\e[1;33my/n \e[0m"

read USER_INPUT
if [ "$USER_INPUT" = "y" ]
then
    echo -e "\e[1;45mCopying Code::Blocks configs! \e[0m"
    
    cp "./resources/default.conf" "/home/andrewf/.config/codeblocks/"
    
    echo -e "\e[1;32mCode::Blocks configs have been copied! \e[0m"
fi
