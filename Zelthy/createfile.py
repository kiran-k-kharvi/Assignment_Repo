import os
import re
from datetime import date,datetime


file_name = "My_File_id_"+str(datetime.now().time())
file_name = ''.join(re.split(':|\.',file_name))
print(file_name)
folder_name = str(date.today())

print(folder_name)
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

file_content = input("Please enter the file content : ")

file_path = folder_name+'/'+file_name
with open(file_path,'w') as file:
    file.write(file_content)

