import os
os.system("clear")
def banner():
	print("\033[1;36;40m_                                   _                _")
	print("| |_ ___ _ __ _ __ ___  _   ___  __ | |__   __ _  ___| | _____ _ __")
	print("| __/ _ \ '__| '_ ` _ \| | | \ \/ / | '_ \ / _` |/ __| |/ / _ \ '__|")
	print("| ||  __/ |  | | | | | | |_| |>  <  | | | | (_| | (__|   <  __/ |")
	print(" \__\___|_|  |_| |_| |_|\__,_/_/\_\ |_| |_|\__,_|\___|_|\_\___|_|\033[0m")
	print("                \033[1;33;40mSONU\033[0m")
	print("")
banner()
while(1):
	try:
		usr=input("\033[1;33;40mEnter username -: \033[0m")
		if usr=="root":
			pas=input("\033[1;33;40mEnter password -: \033[0m")
			if pas=="root":
				os.system("clear")
				banner()
				break
			else :
				print("")
				print("")
				print("")
				print("")
				print("\033[1;31;40m Wrong username/password\033[0m")
				print("")
				print("")
				print("")
				print("")
		else:
			print("")
			print("")
			print("")
			print("")
			print("")
			print("\033[1;31;40m wrong username/password\033[0m")
			print("")
			print("")
			print("")
			print("")
	except KeyboardInterrupt:
		print("")
		print("")
		print("")
		print("")
		print("\033[1;31;40m wrong username/password\033[0m")
		print("")
		print("")
		print("")
		print("")
