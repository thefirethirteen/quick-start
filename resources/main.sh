# main.sh
# version 2.0.1

cd main

echo -e "\e[1;33mThis script will install desktop environments, apps, customizations and copy app configs. \e[0m"
echo -e "\e[1;33mWould you like to continue? [Y/n] \e[0m"

read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    #update package database
    sudo apt-get update

    #required repositories
    sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main universe restricted multiverse"

    #package update
    echo -e "\e[1;33mWould you like to install all package updates available? [Y/n] \e[0m"
    read USER_INPUT
    if [ "$USER_INPUT" == "y" ]
    then
        sudo apt-get -y upgrade --allow-downgrades
    fi

    #runtimes.sh
    echo -e "\e[1;33mWould you like to install any runtimes? [Y/n] \e[0m"
    read USER_INPUT
    if [ "$USER_INPUT" == "y" ]
    then
        bash runtimes.sh
    fi

    #de.sh
    echo -e "\e[1;33mWould you like to install any desktop environments? [Y/n] \e[0m"
    read USER_INPUT
    if [ "$USER_INPUT" == "y" ]
    then
        bash de.sh
    fi

    #apps.sh
    echo -e "\e[1;33mWould you like to install any apps? [Y/n] \e[0m"
    read USER_INPUT
    if [ "$USER_INPUT" == "y" ]
    then
        bash apps.sh
    fi

    #customizations.sh
    echo -e "\e[1;33mWould you like to install any customizations? [Y/n] \e[0m"
    read USER_INPUT
    if [ "$USER_INPUT" == "y" ]
    then
        bash customizations.sh
    fi

    #manual.sh
    #echo -e "\e[1;33mWould you like to copy manuals? [Y/n] \e[0m"
    #read USER_INPUT
    #if [ "$USER_INPUT" == "y" ]
    #then
    #    bash manual.sh
    #fi

    #remove unnecessary packages
    sudo apt-get -y autoremove
fi

#echo -e "\e[1;33mAfter restarting, start [next_script_name].sh using start.sh  \e[0m"

echo "Done."
