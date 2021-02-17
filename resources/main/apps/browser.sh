# browser.sh
# version 1.0.0

cd browser

#firefox.sh
echo -e "Do you want to install Firefox? [y/n]"
read USER_INPUT
if [ "$USER_INPUT" == "y" ]
then
    bash firefox.sh
fi
