# de.sh
# version 1.1.0

cd de

#mate.sh
echo -e "\e[1;33mWould you like to install the Mate Desktop Environment? [Y/n] \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash mate.sh
fi

#gnome.sh
echo -e "\e[1;33mWould you like to install the Gnome Desktop Environment? [Y/n] \e[0m"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash gnome.sh
fi
