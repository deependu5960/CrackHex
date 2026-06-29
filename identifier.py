from crack import crack

def identify_hash(h):
    h = h.strip()

    if h.startswith(("$2a$","$2b$","$2y$")):
        print("Algorithm : Bcrypt")
        crack(h,"Bcrypt")
    
    elif h.startswith("$1$"):
        print("Algorithm : MD5-Crypt")
        crack(h,"MD5-Crypt")

    elif h.startswith("$5$"):
        print("Algorithm : SHA256-Crypt")
        crack(h,"SHA256-Crypt")

    elif h.startswith("$6$"):
        print("Algorithm : SHA512-Crypt")
        crack(h,"SHA512-Crypt")
        
    elif h.startswith("$S$"):
        print("Algorithm : Drupal 7 SHA512")
        crack(h,"Drupal-7")

    elif h.startswith(("$argon2i$", "$argon2d$", "$argon2id$")):
        print("Algorithm : Argon2")
        crack(h,"Argon2")
    
    else:
        hex_char = "0123456789abcdefABCDEF"
        is_hash = True
        for letter in h:
            if letter not in hex_char:
                is_hash =False
                break

        if is_hash:
            if len(h)==32:
                print("Algorithm possibilities : MD5 / NTLM / LM / MD4")
                alg = input("Enter the Valid Algorithm : ").strip()
                if alg.upper()=="MD5":
                    crack(h,"MD5")
                elif alg.upper()=="NTLM":
                    crack(h,"NTLM")
                elif alg.upper()=="LM":
                    crack(h,"LM")
                elif alg.upper()=="MD4":
                    crack(h,"MD4")
                else:
                    print("Please enter valid algorithm")

            elif len(h)==40:
                print("Algorithm : SHA1")
                crack(h,"SHA1")

            elif len(h)==64:
                print("Algorithm : SHA256")
                crack(h,"SHA256")
                
            elif len(h)==128:
                print("Algorithm : SHA512")
                crack(h,"SHA512")

            else:
                print(f"\033[91m No Algorithm Found, Please check the length of hash\033[0m")
        else:
            print( f"\033[1;91m[!] Invalid Hash\033[0m" )
