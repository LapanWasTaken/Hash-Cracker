#!/usr/bin/python3

#################
#               #
# Only for test #
#               #
#################

#author : LapanWasTaken 🤓
import hashlib, time, os, sys

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print(color.BOLD)
os.system('clear')
print(color.RED + """
  _   _           _      ____                _             
 | | | | __ _ ___| |__  / ___|_ __ __ _  ___| | _____ _ __ 
 | |_| |/ _` / __| '_ \| |   | '__/ _` |/ __| |/ / _ \ '__|
 |  _  | (_| \__ \ | | | |___| | | (_| | (__|   <  __/ |   
 |_| |_|\__,_|___/_| |_|\____|_|  \__,_|\___|_|\_\___|_|   
                                                           
Create by .:LapanWasTaken:.
""")
print(color.CYAN + "Github   : " + color.GREEN + "https://github.com/LapanWasTaken")
print(color.CYAN + "Telegram : " + color.GREEN + "t.me/Cendawann")
print(color.CYAN + "Quote    : " + color.GREEN + "Life is a series of thousand little miracles , notice them ")
print(color.CYAN + "Note     : " + color.GREEN + "Don't Sell My Tool !")
print(color.CYAN + "  /\_/\ " )
print(color.CYAN + "  (•_•) " )
print(color.CYAN + "  (>     " )
flag = 0
hash = input(color.BLUE + "[+] Enter MD5 hash: " + color.BLUE + "")
wordlist = input(color.YELLOW + "[+] Enter Wordlist: " + color.BLUE + "")
os.system('clear')
time.sleep(1)
status1 = 'Cracking'
status2 = 'Cracked'
status3 = 'Not Cracked'

try:
    file = open(wordlist, "r")
except:
    print("[!] Tiada File DiJumpai!")
    quit()

print('[*] Cracking...')
print(color.BOLD)
print('')
print('')
time.sleep(2)
print(color.RED + "Status : " + color.BLUE + status1)

for word in file:
    encode = word.encode('utf-8')
    digest = hashlib.md5(encode.strip()).hexdigest()
    

    if digest == hash:
        os.system('clear')
        print('[+] Yeaay dah jumpa Password.')
        print('[+] Nah Password: ' + color.GREEN + word)
        flag = 1
        status2 = "Cracked"
        print(color.BOLD)
        print(color.RED + "Status : " + color.BLUE + status2)        
        break
    
if flag == 0:
    #os.system('clear')
    print("[!] Password Tiada Dalam List.")
    status = "(Not Cracked)"
    print(color.BOLD)
    print(color.RED + "Status : " + color.BLUE + status3)     
    quit()
