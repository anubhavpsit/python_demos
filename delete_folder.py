# Added On : 2018-06-20
#Author : Anubhav anubhav.psit.2009@gmail.com
# Cron to delete the folder after specific day

import os
import sys
import shutil
import datetime
from datetime import datetime, timedelta

N = 8  #Days ago
folder_path = "/home/Desktop/python_tutorial/" # Folder Path

date_N_days_ago = datetime.now() - timedelta(days=N)
DELETE_DATE = date_N_days_ago.strftime ("%Y-%m-%d");
today_date = datetime.now().strftime ("%Y-%m-%d")
mydir=folder_path+DELETE_DATE
if os.path.exists(mydir): shutil.rmtree(mydir)
print("Delete folder date => " + DELETE_DATE)
print("Today date => " + today_date)
print("Delete dir path => " + mydir)