import bcrypt
import hashlib
from passlib.hash import md5_crypt, sha256_crypt, sha512_crypt,lmhash
from argon2 import PasswordHasher
from Crypto.Hash import MD4
from argon2.exceptions import VerifyMismatchError,VerificationError
from itertools import permutations

def crack_bcrypt(h,gs_paswd,count):
    if bcrypt.checkpw(gs_paswd.encode("utf-8"),h.encode("utf-8")):
        print(f"\033[1;92m[SUCCESS]\033[0m Password matched : ",f"\033[1;92m{gs_paswd}\033[0m")
        print("Total attempts : ",count)
        return True
    else:
        print(f"\033[91m[FAILED]\033[0m Password not matched! : ",gs_paswd)
        return False

def crack_md5(h,gs_paswd,count):
    if hashlib.md5(gs_paswd.encode()).hexdigest() == h.lower():
        print(f"\033[1;92m[SUCCESS]\033[0m Password matched : ",f"\033[1;92m{gs_paswd}\033[0m")
        print("Total attempts : ",count)
        return True
    else:
        print(f"\033[91m[FAILED]\033[0m Password not matched! : ",gs_paswd)
        return False

def crack_md4(h,gs_paswd,count):
    hsh = MD4.new()
    hsh.update(gs_paswd.encode())
    if hsh.hexdigest().lower() == h.lower():
        print(f"\033[1;92m[SUCCESS]\033[0m Password matched : ",f"\033[1;92m{gs_paswd}\033[0m")
        print("Total attempts : ",count)
        return True
    else:
        print(f"\033[91m[FAILED]\033[0m Password not matched! : ",gs_paswd)
        return False

def crack_ntlm(h,gs_paswd,count):
    hsh = MD4.new()
    hsh.update(gs_paswd.encode("utf-16le"))
    if hsh.hexdigest().lower() == h.lower():
        print(f"\033[1;92m[SUCCESS]\033[0m Password matched : ",f"\033[1;92m{gs_paswd}\033[0m")
        print("Total attempts : ",count)
        return True
    else:
        print(f"\033[91m[FAILED]\033[0m Password not matched! : ",gs_paswd)
        return False

def crack_lm(h,gs_paswd,count):
    try:
        if lmhash.verify(gs_paswd,h.lower()):
            print(f"\033[1;92m[SUCCESS]\033[0m Password matched : ",f"\033[1;92m{gs_paswd}\033[0m")
            print("Total attempts : ",count)
            return True
        else:
            print(f"\033[91m[FAILED]\033[0m Password not matched! : ",gs_paswd)
            return False
    
    except UnicodeEncodeError:
        print(f"\033[1;91m Not able to process this word\033[0m : ",gs_paswd)
        return False

def crack_sha256(h,gs_paswd,count):
    if hashlib.sha256(gs_paswd.encode()).hexdigest() == h.lower():
        print(f"\033[1;92m[SUCCESS]\033[0m Password matched : ",f"\033[1;92m{gs_paswd}\033[0m")
        print("Total attempts : ",count)
        return True
    else:
        print(f"\033[91m[FAILED]\033[0m Password not matched! : ",gs_paswd)
        return False

def crack_sha512(h,gs_paswd,count):
    if hashlib.sha512(gs_paswd.encode()).hexdigest() == h.lower():
        print(f"\033[1;92m[SUCCESS]\033[0m Password matched : ",f"\033[1;92m{gs_paswd}\033[0m")
        print("Total attempts : ",count)
        return True
    else:
        print(f"\033[91m[FAILED]\033[0m Password not matched! : ",gs_paswd)
        return False

def crack_sha1(h,gs_paswd,count):
    if hashlib.sha1(gs_paswd.encode()).hexdigest() == h.lower():
        print(f"\033[1;92m[SUCCESS]\033[0m Password matched : ",f"\033[1;92m{gs_paswd}\033[0m")
        print("Total attempts : ",count)
        return True
    else:
        print(f"\033[91m[FAILED]\033[0m Password not matched! : ",gs_paswd)
        return False

def crack_md5_crypt(h,gs_paswd,count):
    if md5_crypt.verify(gs_paswd,h):
        print(f"\033[1;92m[SUCCESS]\033[0m Password matched : ",f"\033[1;92m{gs_paswd}\033[0m")
        print("Total attempts : ",count)
        return True
    else:
        print(f"\033[91m[FAILED]\033[0m Password not matched! : ",gs_paswd)
        return False

def crack_sha256_crypt(h,gs_paswd,count):
    if sha256_crypt.verify(gs_paswd,h):
        print(f"\033[1;92m[SUCCESS]\033[0m Password matched : ",f"\033[1;92m{gs_paswd}\033[0m")
        print("Total attempts : ",count)
        return True
    else:
        print(f"\033[91m[FAILED]\033[0m Password not matched! : ",gs_paswd)
        return False

def crack_sha512_crypt(h,gs_paswd,count):
    if sha512_crypt.verify(gs_paswd,h):
        print(f"\033[1;92m[SUCCESS]\033[0m Password matched : ",f"\033[1;92m{gs_paswd}\033[0m")
        print("Total attempts : ",count)
        return True
    else:
        print(f"\033[91m[FAILED]\033[0m Password not matched! : ",gs_paswd)
        return False

def crack_argon2(h,gs_paswd,count):
    ph = PasswordHasher()
    try:
        ph.verify(h,gs_paswd)
        print(f"\033[1;92m[SUCCESS]\033[0m Password matched : ",f"\033[1;92m{gs_paswd}\033[0m")
        print("Total attempts : ",count)
        return True
    except (VerifyMismatchError,VerificationError):
        print(f"\033[91m[FAILED]\033[0m Password not matched! : ",gs_paswd)
        return False

def crack_pass(algo,h,gs_paswd,count):
    if algo=="Bcrypt":
        if crack_bcrypt(h,gs_paswd,count):
            return True
    
    elif algo=="MD5":
        if crack_md5(h,gs_paswd,count):
            return True

    elif algo=="MD4":
        if crack_md4(h,gs_paswd,count):
            return True

    elif algo=="NTLM":
        if crack_ntlm(h,gs_paswd,count):
            return True
    
    elif algo=="LM":
        if crack_lm(h,gs_paswd,count):
            return True

    elif algo=="SHA256":
        if crack_sha256(h,gs_paswd,count):
            return True

    elif algo=="SHA512":
        if crack_sha512(h,gs_paswd,count):
            return True

    elif algo=="SHA1":
        if crack_sha1(h,gs_paswd,count):
            return True

    elif algo=="MD5-Crypt":
        if crack_md5_crypt(h,gs_paswd,count):
            return True

    elif algo=="SHA256-Crypt":
        if crack_sha256_crypt(h,gs_paswd,count):
            return True

    elif algo=="SHA512-Crypt":
        if crack_sha512_crypt(h,gs_paswd,count):
            return True

    elif algo=="Argon2":
        if crack_argon2(h,gs_paswd,count):
            return True


def crack(h,algo):
    h = h.strip()
    print(f"\033[1;91m Please select cracking mode \033[0m \n \033[1;91m[1]\033[0m filtered-Wordlist Mode(filtered by length of password)  \n \033[1;91m[2]\033[0m self-generate-wordlist Mode (Customizable) \n \033[1;91m[3]\033[0m Default Mode ")
    
    mode = input(f"\033[1;91m Enter your Mode :\033[0m ")
    
    if mode=="1":
        print(f"\033[1;91m How would you like to filter \033[0m  \n \033[1;91m[1]\033[0m Filter by password length\n \033[1;91m[2]\033[0m Filter by starting letter\n \033[1;91m[3]\033[0m Filter by both")
        flt = input(f"\033[1;91m Enter filter option :\033[0m ").strip()

        if flt == "1":
            try:
                pwd_len = int(input(f"\033[1;91m Enter length of password :\033[0m "))
                count = 0
                with open("/usr/share/wordlists/rockyou.txt","r",encoding="latin-1") as f:
                    for line in f:
                        gs_paswd = line.strip()
                        if len(gs_paswd)==pwd_len:
                            count+=1
                            if crack_pass(algo,h,gs_paswd,count):
                                return

                    else:
                        print(f"\n\033[1;91m [Password Not Found],\033[0m please try another wordlist...")
            except:
                print(f"\033[1;91m Please enter Valid input\033[0m")
        
        if flt == "2":
            str_letter = input(f"\033[1;91m Enter starting letters : \033[0m")
            count = 0
            with open("/usr/share/wordlists/rockyou.txt","r",encoding="latin-1") as f:
                for line in f:
                    gs_paswd = line.strip()
                    if gs_paswd.startswith(str_letter):
                        count+=1
                        if crack_pass(algo,h,gs_paswd,count):
                            return

                else:
                    print(f"\n\033[1;91m [Password Not Found],\033[0m please try another wordlist...")
        
        if flt == "3":
            try :
                pwd_len = int(input(f"\033[1;91m Enter length of password : \033[0m"))
                str_letter = input(f"\033[1;91m Enter starting letters : \033[0m")
                count = 0
                with open("/usr/share/wordlists/rockyou.txt","r",encoding="latin-1") as f:
                    for line in f:
                        gs_paswd = line.strip()
                        if gs_paswd.startswith(str_letter) and (len(gs_paswd) == pwd_len):
                            count+=1
                            if crack_pass(algo,h,gs_paswd,count):
                                return

                    else:
                        print(f"\n\033[1;91m [Password Not Found],\033[0m please try another wordlist...")
            except:
                print(f"\033[1;91m Please enter Valid input\033[0m")
        else:
            print(f"\033[1;91m Please enter Valid input\033[0m")
        


    elif mode=="2":
        print(f"\033[1;91m Enter your words\033[0m \n [type /e when complete]")
        word = []
        count = 0
        while True:
            wrd = input(">> ")
            if wrd.lower()=="/e":
                break
            word.append(wrd)

        print("Your wordlist : ", word)
        opt = input(f"\033[1;91m Do you want to filter combinations [y/n] : \033[0m").lower().strip()

        if opt == "y":
            print(f"\033[1;91m How would you like to filter \033[0m  \n \033[1;91m[1]\033[0m Filter by password length\n \033[1;91m[2]\033[0m Filter by starting letter\n \033[1;91m[3]\033[0m Filter by both")
            flt = input(f"\033[1;91m Enter filter option :\033[0m ").strip()
            if flt == "1":
                try:
                    pass_len = int(input(f"\033[1;91m Enter password length : \033[0m"))
                    for i in range(1, len(word)+1):
                        for p in permutations(word, i):
                            gs_paswd = "".join(p)
                            if len(gs_paswd) == pass_len:
                                count+=1
                                if crack_pass(algo,h,gs_paswd,count):
                                    return
                    else:
                        print(f"\n\033[1;91m [Password Not Found],\033[0m please try another combinations...")
                except:
                    print(f"\033[1;91m Please Enter valid no.\033[0m ")
            
            elif flt == "2":
                strt_letter = input(f"\033[1;91m Enter starting letter : \033[0m")
                for i in range(1, len(word)+1):
                    for p in permutations(word, i):
                        gs_paswd = "".join(p)
                        if gs_paswd.startswith(strt_letter):
                            count+=1
                            if crack_pass(algo,h,gs_paswd,count):
                                return
                else:
                    print(f"\n\033[1;91m [Password Not Found],\033[0m please try another combinations...")

            elif flt == "3":
                try:
                    pass_len = int(input(f"\033[1;91m Enter password length :\033[0m "))
                    strt_letter = input(f"\033[1;91m Enter starting letter : \033[0m")
                    for i in range(1, len(word)+1):
                        for p in permutations(word, i):
                            gs_paswd = "".join(p)
                            if gs_paswd.startswith(strt_letter) and (len(gs_paswd) == pass_len):
                                count+=1
                                if crack_pass(algo,h,gs_paswd,count):
                                    return
                    else:
                        print(f"\n\033[1;91m [Password Not Found],\033[0m please try another combinations...")
                except:
                    print(f"\033[1;91m Please enter valid input...\033[0m")
       
            else:
                print(f"\n\033[1;91m Invalid option...\033[0m")
        
        else:
            for i in range(1, len(word)+1):
                for p in permutations(word, i):
                    gs_paswd = "".join(p)
                    count+=1
                    if crack_pass(algo,h,gs_paswd,count):
                        return
            else:
                print(f"\n\033[1;91m [Password Not Found],\033[0m please try another combinations...")
        
    elif mode=="3":
        count = 0
        with open("/usr/share/wordlists/rockyou.txt","r",encoding="latin-1") as f:
            for line in f:
                    
                gs_paswd = line.strip()
                count+=1
                if crack_pass(algo,h,gs_paswd,count):
                    return
            
            else:
                print(f"\n\033[1;91m [Password Not Found],\033[0m please try another wordlist...")
        

    else:
        print(f"\n\033[1;91m Invalid Mode\033[0m\n Try again...")
        crack_pass(h,algo)
