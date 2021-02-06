# iconpack-obsidian.sh
# version 1.1.0

echo -e "\e[1;45mAdding iconpack-obsidian! \e[0m"

git clone "https://github.com/madmaxms/iconpack-obsidian"

cd iconpack-obsidian
sudo mv Obsidian* /usr/share/icons/
cd ..

rm -rf iconpack-obsidian

echo -e "\e[1;32mThe icons from iconpack-obsidian have been added to /usr/share/icons \e[0m"
