import os,platform,requests,time

banner="""\033[1;32m
        
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░ 
       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
     ░▒▓██▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓██▓▒░  ░▒▓███████▓▒░░▒▓████████▓▒░░▒▓██████▓▒░░▒▓███████▓▒░  
 ░▒▓██▓▒░    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓██████▓▒░													\033[0m"""

def linex():
    print('\x1b[38;5;196m                                                                                                                                      							    ﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌')


def menu():
	os.system('python ZKV6_enc.py')



def subscription():
	print(banner)
	x=platform.version()[14:][:21][::-1].upper()+platform.release()[15:][::-1].upper()+platform.version()[:8]
	y=x.replace( ' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace(' ', '')
	xyz="ZK6-"
	key=xyz+y
	httpCaht=requests.get('https://github.com/ZK-V6/ZKV/blob/main/Approval.txt').text
	if key in httpCaht:
		linex()
		print("\033[92m Your key is approved")
		time.sleep(3)
		menu()
		return None
	linex()
	print ("\033[91m Your key is not approved")
	linex()
	print("Your Key :"+key)
	linex()
	input("Press enter to send key")
	os.system("xdg-open https://t.me/+fvzGD195KjllMGI1")
	subscription()
	return None
	exit()
subscription()
	

	
	
