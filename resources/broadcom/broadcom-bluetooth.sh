# broadcom-bluetooth.sh
# version 1

echo -e "\e[1;45mInstalling Broadcom Bluetooth Drivers! \e[0m"

sudo cp "./broadcom-bluetooth/resources/BCM43142A0-0a5c-216c.hcd" "/lib/firmware/brcm"

echo -e "\e[1;32mBCM43142A0-0a5c-216c.hcd has been installed to /lib/firmware/brcm \e[0m"
echo -e "\e[1;32mBroadcom Bluetooth Drivers have been installed! \e[0m"
