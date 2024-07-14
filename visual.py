#### VISUAL GENERATION ####

import time 
import sys 
import os 


logo = """
  _____                                    _    _____ _                        _   _     
 |  __ \                                  | |  / ____| |                      | | | |    
 | |__) |_ _ ___ _____      _____  _ __ __| | | (___ | |_ _ __ ___ _ __   __ _| |_| |__  
 |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |  \___ \| __| '__/ _ \ '_ \ / _` | __| '_ \ 
 | |  | (_| \__ \__ \\ V  V / (_) | | | (_| |  ____) | |_| | |  __/ | | | (_| | |_| | | |
 |_|___\__,_|___/___/ \_/\_/ \___/|_|  \__,_| |_____/ \__|_|  \___|_| |_|\__, |\__|_| |_|
  / ____| |             | |                                               __/ |          
 | |    | |__   ___  ___| | _____ _ __                                   |___/           
 | |    | '_ \ / _ \/ __| |/ / _ \ '__|                                                  
 | |____| | | |  __/ (__|   <  __/ |                                                     
  \_____|_| |_|\___|\___|_|\_\___|_|                                                     

                                                                                         
"""

def load_details(parameters):
	breakdown=f"""

+----------------+---------+---------+
|   parameters   | Minimum | Present |
+----------------+---------+---------+
| Length         |       8 |      {'8+' if parameters[0]>=8 else str(parameters[0]) + ' '} |
| Special symbol |       1 |      {'1+' if parameters[1]>=1 else str(parameters[1]) + ' '} |
| Lowercase char |       1 |      {'1+' if parameters[2]>=1 else str(parameters[2]) + ' '} |
| Uppercase char |       1 |      {'1+' if parameters[3]>=1 else str(parameters[3]) + ' '} |
| Digits         |       1 |      {'1+' if parameters[4]>=1 else str(parameters[4]) + ' '} |
+----------------+---------+---------+
\n
"""
	print(breakdown)



def load_logo():
	if os.name =="nt": 
		os.system("cls") 
	else: 
		os.system("clear") 
	print(logo)


def load_animation(s): 
	load_str = s
	ls_len = len(load_str) 
	animation = "|/-\\"
	anicount = 0 
	counttime = 0		
	i = 0					

	while (counttime != 100): 
		time.sleep(0.075) 
		load_str_list = list(load_str) 
		x = ord(load_str_list[i])  
		y = 0							
		if x != 32 and x != 46:			 
			if x>90: 
				y = x-32
			else: 
				y = x + 32
			load_str_list[i]= chr(y) 
		res =''			 
		for j in range(ls_len): 
			res = res + load_str_list[j] 
			
		sys.stdout.write("\r"+res + animation[anicount]) 
		sys.stdout.flush()
		load_str = res 
		anicount = (anicount + 1)% 4
		i =(i + 1)% ls_len 
		counttime = counttime + 1
	if os.name =="nt": 
		os.system("cls") 
	else: 
		os.system("clear") 

