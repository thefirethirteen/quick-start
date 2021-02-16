# start.sh
# version 1.0.1

cd resources

echo -e "\e[1;33mWhich script would you like to start? \e[0m"

echo "Available scripts: main.sh"

echo -e "\e[1;33m(If unsure, type main.sh) \e[0m"

read USER_INPUT
bash "$USER_INPUT"
