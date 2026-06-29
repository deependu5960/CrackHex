from identifier import identify_hash
from db import check_database_cache

if __name__ == "__main__":
    while True:

        banner = r'''
                                                        
                                                                  ___  ___
         _____   _      __     _____   _  __     __    __   ____  \  \/  /  
        |  ___\ | |/\  /  \   |  ___\ | |/ /    |  |__|  | | . /   \    /
        | |___  |   / / __ \  | |__   |   \     |   __   | |  /_   /    \
        |_____\ |_|  /_/  \_\ |_____\ |_|\_\    |__|  |__| |____\ /__/\__\    
        
        '''
        
        print(f"\033[94m{banner}\033[0m")
        
        hash_pwd = input(f"\033[1;91m Enter Your Hash : \033[0m")
        if hash_pwd.lower() =="exit":
            exit()
        else:
            cache_result = check_database_cache(hash_pwd)
            if cache_result["found"]:
                print(f"[+] Instant Match Found in Crack-Hex DB!")
                print(f"[+] Algorithm : {cache_result['algo']}")
                print(f"\033[1;92m[+] Password : {cache_result['plain_text']}\033[0m")
                # leave the interation early here because we already have the answer!
                continue
            else :
                identify_hash(hash_pwd)
    
