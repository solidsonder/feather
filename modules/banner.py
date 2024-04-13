from colorama import init, Fore, Back, Style
from time import gmtime, strftime

infox = "["+Fore.BLUE+"*"+Style.RESET_ALL+"]"
warningx = "["+Fore.RED+"!"+Style.RESET_ALL+"]"
unknownx = "["+Fore.YELLOW+"?"+Style.RESET_ALL+"]"


def shbn():
    banner = Fore.LIGHTCYAN_EX +r""" ______   ______     ______     ______   __  __     ______     ______    
/\  ___\ /\  ___\   /\  __ \   /\__  _\ /\ \_\ \   /\  ___\   /\  == \   
\ \  __\ \ \  __\   \ \  __ \  \/_/\ \/ \ \  __ \  \ \  __\   \ \  __<   
 \ \_\    \ \_____\  \ \_\ \_\    \ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_/     \/_____/   \/_/\/_/     \/_/   \/_/\/_/   \/_____/   \/_/ /_/"""+Style.RESET_ALL


    banner2 = Fore.LIGHTWHITE_EX+"\n                A Telegram alarm and transaction tool \n"+Style.RESET_ALL
    banner2 += Fore.LIGHTWHITE_EX+"            Date "+Fore.YELLOW+strftime("%Y-%m-%d %H:%M:%S", gmtime())+Fore.LIGHTWHITE_EX+" github "+Style.RESET_ALL+Fore.YELLOW+"@solidsonder"+Style.RESET_ALL+" \n"+Style.RESET_ALL


    print(banner)
    print(banner2)