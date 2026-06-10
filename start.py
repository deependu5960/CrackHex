from identifier import identify_hash

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
            identify_hash(hash_pwd)
    