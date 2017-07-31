I order to set up credentials used for emailing:
git clone/git pull the latest version of the code.

copy the credentials template to home folder:
sudo cp /home/pi/TM_Timber/BinSensor/credentials_Template.py /home/pi/credentials.py

open the credentials file to enter your details:
sudo nano /home/pi/credentials.py

Enter your user, email and password into the quotes, and save.
This file in the home directory will not be affected by future git pull requests, so you wil not need to keep re-adding your details.

Cheers!
