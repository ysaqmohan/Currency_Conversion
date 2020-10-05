# Currency_Conversion
Steps to deploy the application:
1. Create the directories as mentioned below.
2. Create the virtual environment from packages.txt in /edw/Currency_Conversion/ directory.
3. Move the bash script and python script (Copying the whole code of the application will suffice)
4. Set up the crontab. 

Note: The current application runs with the default linux user. If creating a sepearte user for the application, grant appropirate privileges to directories, files and scripts.

#Creating directories
mkdir edw
cd edw
mkdir Currency_Conversion
cd Currency_Conversion
mkdir bash
mkdir python
mkdir data
mkdir logs

#Virtual environment
virtualenv -p /usr/bin/python3.6 project_Currency
source project_Currency/bin/activate
pip install -r packages.txt

#Scheduler
sudo apt-get install cron
crontab -e
0 */1 * * * sh /edw/Currency_Conversion/bash/Currency_script.sh
service cron start


#Execute the script manually
sh /edw/Currency_Conversion/bash/Currency_script.sh
