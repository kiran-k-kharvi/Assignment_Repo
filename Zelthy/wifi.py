
import subprocess
import os

wifi_details = subprocess.check_output(['netsh', 'wlan', 'show', 'network' ,'mode=Bssid'])
wifi_details = wifi_details.decode('ascii')
wifi_details = wifi_details.replace('\r', '')
wifi_details_list = wifi_details.split('\n')
wifi_details_list = wifi_details_list[4:]


available_wifi = []
i = 0
print(wifi_details_list)
while i < len(wifi_details_list)-1:
    if i % 11 == 0:
        key = wifi_details_list[i].split(':')[1]
        val = int(wifi_details_list[i+5].split(':')[1].replace('%',''))
        available_wifi.append((key,val))
    i += 1
available_wifi = sorted(available_wifi,key=lambda wf:wf[1],reverse=True)
available_wifi = available_wifi[:3]


print("Available wifi network and thier network strengts are : \n")
top = 1
for ssid_details in available_wifi:
    print(str(top)+')'+ssid_details[0]+"   :   "+str(ssid_details[1])+'%')
    top+=1

def createNewConnection(ssid_name, password):
	newConnection = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
	<name>"""+ssid_name+"""</name>
	<SSIDConfig>
		<SSID>
			<name>"""+ssid_name+"""</name>
		</SSID>
	</SSIDConfig>
	<connectionType>ESS</connectionType>
	<connectionMode>auto</connectionMode>
	<MSM>
		<security>
			<authEncryption>
				<authentication>WPA2PSK</authentication>
				<encryption>AES</encryption>
				<useOneX>false</useOneX>
			</authEncryption>
			<sharedKey>
				<keyType>passPhrase</keyType>
				<protected>false</protected>
				<keyMaterial>"""+password+"""</keyMaterial>
			</sharedKey>
		</security>
	</MSM>
</WLANProfile>"""
	command = "netsh wlan add profile filename=\""+ssid_name+".xml\""+" interface=Wi-Fi"
	with open(ssid_name+".xml", 'w') as file:
		file.write(newConnection)
	os.system(command)


def connect(ssid_name,password):
        try:
            
            os.system("netsh wlan connect name=\""+ssid_name+"\" ssid=\""+ssid_name+"\" interface=Wi-Fi")
        except:
            print("Did not connect. Try again. ")
            return False
        else:
            return True



sr_number = int(input("\nTo which wifi you wish to connect? \nEnter the serial number (eg:2) : "))
try_count = 1
while sr_number>3 and try_count<3:
            sr_number = int(input("Try again with valid serial number : "))
            try_count+=1


if sr_number<4:
    ssid = available_wifi[sr_number-1][0].strip()
    flag = False
    pass_try_count=1
    while not flag and pass_try_count<4:
        password = input("\nPlease Enter the password : \n ")

        createNewConnection(ssid,password)
        flag = connect(ssid,password)
        if flag:
            print("Connected successfully!!!")
            break
        else:
            pass_try_count +=1
    if not flag:
        print("Run the script again!!!")


else:
    print("Run the script again!!!")
    