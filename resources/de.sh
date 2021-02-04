# de.sh
# version 4

cd de

#mate.sh
echo -e "\e[1;33mWould you like to install the Mate Desktop Environment? y/n \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash mate.sh
fi
