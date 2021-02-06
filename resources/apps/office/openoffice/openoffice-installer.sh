# openoffice-installer.sh
# version 1.0.1

echo -e "\e[1;33mWhat version of Apache OpenOffice would you like to install? \e[0m"
echo -e "\e[1;33mAvailable versions: 3.4.1; 4.0.0-4.0.1; 4.1.0-4.1.8 \e[0m"
echo -e "\e[1;33mInput your desired version: \e[0m"
read VERSION

echo -e "\e[1;45mInstalling Apache OpenOffice $VERSION! \e[0m"

wget -nv -O download "https://sourceforge.net/projects/openofficeorg.mirror/files/"$VERSION"/binaries/en-GB/Apache_OpenOffice_"$VERSION"_Linux_x86-64_install-deb_en-GB.tar.gz/download"
tar -xf download
cd en-GB
cd DEBS
sudo dpkg -i *.deb
cd desktop-integration
sudo dpkg -i *.deb
cd ..
cd ..
cd ..
rm -rf download

echo -e "\e[1;32mApache OpenOffice $VERSION has been installed! \e[0m"
