# social.sh
# version 1.0.0

cd development

#codeblocks.sh
echo -e "\e[1;33mWould you like to install Code::Blocks? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash codeblocks.sh
fi
