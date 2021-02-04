# config.sh
# version 6

cd config

#codeblocks.sh
echo -e "\e[1;33mWould you like to copy Code::Blocks configs? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" = "y" ]
then
    bash codeblocks.sh
fi
