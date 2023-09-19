#This code generates a random password. It takes random values from predefined lists and appends them to a new list and shuffles it and gives a random password of the desired length. 
def passwordGenerator():
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    special = ['@','#','$','%','&','!'] #defined all the characters
    n = int(input("Enter Password Length: ")) #takes user input for defining password length
    password = [] #empty password list
    while len(password) <= n: 
        if len(password)<n:
            i = random.choice(alphabets)
            password.append(random.choice([i.upper(),i.lower()])) #appends random alphabet from alphabets list along with randomlly selecting uppercase or lowercase letter.
            if len(password)<n:
                j = str(random.choice(numbers)) #appends a random number
                password.append(j)
                if len(password)<n:
                    k = random.choice(special) # appends a random special character
                    password.append(k)
                else:
                    break
            else:
                break
        else:
            break
    
    random.shuffle(password) #shuffles the password
    
    return ''.join(password) #returns the output
