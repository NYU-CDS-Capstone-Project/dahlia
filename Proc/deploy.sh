#!/bin/bash

# Make sure only root can run our script
#if [ "$(id -u)" != "0" ]; then
#    tput setaf 1
#    echo "This script must be run as root" 1>&2
#    tput sgr0
#    exit 1
#fi
echo ""
echo "Welcome to the Dahlia installation script"
echo "==========================================="
echo ""
# Get user parameters
read -p "Server name for Dahlia: " SERVERNAME
read -p "Server web directory, or your localhost web directory: " SERVERPATH
# Install
echo ""
echo "Thank you. Now starting installation ..."
echo ""

tput bold
echo "Installing basic prerequisites ..."
tput sgr0
echo ""

easy_install python
easy_install pip

tput bold
echo "Installing required python packages ..."

pip install nltk
pip install reverse_geocoder 
echo ""
tput bold
echo "Downloading Dahlia from github ..."
tput sgr0
echo ""

git clone https://github.com/NYU-CDS-Capstone-Project/dahlia.git $SERVERPATH/dahlia

echo ""
tput bold
echo "Preliminary Dahlia configuration ..."
tput sgr0
echo ""

chmod 755 $SERVERPATH/run.sh
chmod 755 $SERVERPATH/Proc/deploy.sh

echo ""
tput bold
echo "Done!"
tput sgr0
echo ""

echo "Please visit your new Dahlia installation at: http://$SERVERNAME/dahlia/Vis/"
echo ""

