# main.sh
# version 2.1.0

cd main

echo -e "This script will install desktop environments, apps, customizations and copy app configs."
echo -e "Do you want to continue? [Y/n]"

read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    #update package database
    sudo apt-get update
    
    #required packages
    #sudo apt-get -y install python3
    #sudo apt-get -y install python-is-python3
    
    #required repositories
    sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main universe restricted multiverse"

    #package update
    echo -e "Do you want to install all package updates available? [Y/n]"
    read USER_INPUT
    if [ "$USER_INPUT" == "y" ]
    then
        sudo apt-get -y upgrade --allow-downgrades
    fi

    #runtimes.sh
    echo -e "Do you want to install any runtimes? [Y/n]"
    read USER_INPUT
    if [ "$USER_INPUT" == "y" ]
    then
        bash runtimes.sh
    fi

    #de.sh
    echo -e "Do you want to install any desktop environments? [Y/n]"
    read USER_INPUT
    if [ "$USER_INPUT" == "y" ]
    then
        bash de.sh
    fi

    #apps.sh
    echo -e "Do you want to install any apps? [Y/n]"
    read USER_INPUT
    if [ "$USER_INPUT" == "y" ]
    then
        bash apps.sh
    fi

    #customizations.sh
    echo -e "Do you want to install any customizations? [Y/n]"
    read USER_INPUT
    if [ "$USER_INPUT" == "y" ]
    then
        bash customizations.sh
    fi

    #remove unnecessary packages
    sudo apt-get -y autoremove
fi

#echo -e "\e[1;33mAfter restarting, start [next_script_name].sh using start.sh  \e[0m"
