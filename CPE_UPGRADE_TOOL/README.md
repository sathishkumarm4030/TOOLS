# Vcpe MIGRATION TOOL
step1: install packages
below are the packages used in script.please install pkgs before running script or when facing error install
1) netmiko - https://github.com/sathishkumarm4030/netmiko_enhanced.git
2) textfsm
3) pandas
4) requests
5) json

Install listed packages in Ubuntu 16.04
apt-get install git
apt-get install python-pip
pip install pandas
pip install textfsm
pip install requests
#sudo pip install cffi==1.11.5
sudo apt-get install python-serial

2) download repos from git
git clone https://github.com/sathishkumarm4030/netmiko_enh_june6.git
git clone https://github.com/sathishkumarm4030/Upgradevcpe.git



install below packages
1) download netmiko pkg from github - git clone https://github.com/sathishkumarm4030/netmiko_enh_june6.git
2) cd netmiko & run "python setup.py install"


step3: run DoCpeUpgrade.py


after script run:

RESULT stored in RESULT.csv

device cmd output stored in PARSED_DATA FOLDER

SCRIPT LOGS stored in LOGS



