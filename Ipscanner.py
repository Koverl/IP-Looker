import requests
import os
from colorama import Fore, Style, init


init(autoreset=True)




#ASCIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
print (""" ## ##    ## ##     ##     ###  ##  
##   ##  ##   ##     ##      ## ##  
####     ##        ## ##    # ## #  
 #####   ##        ##  ##   ## ##   
    ###  ##        ## ###   ##  ##  
##   ##  ##   ##   ##  ##   ##  ##  
 ## ##    ## ##   ###  ##  ###  ##  
                                    
""")

ip_address = input("Enter the IP address for lookup:\n")
print(Fore.GREEN + "Performing IP Lookup...")
    
response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    
if response.status_code == 200:
        ip_info = response.json()
        print(Fore.GREEN + f"IP Address: {ip_info.get('ip', 'N/A')}")
        print(Fore.GREEN + f"Hostname: {ip_info.get('hostname', 'N/A')}")
        print(Fore.GREEN + f"City: {ip_info.get('city', 'N/A')}")
        print(Fore.GREEN + f"Region: {ip_info.get('region', 'N/A')}")
        print(Fore.GREEN + f"Country: {ip_info.get('country', 'N/A')}")
        print(Fore.GREEN + f"Location: {ip_info.get('loc', 'N/A')}")
        print(Fore.GREEN + f"Organization: {ip_info.get('org', 'N/A')}")
        print(Fore.GREEN + f"Postal: {ip_info.get('postal', 'N/A')}")

else:
        print(Fore.GREEN + "Failed to perform IP lookup. Please check the IP address and try again.")
        