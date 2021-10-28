import random
print("WELCOME TO READABLE PASSWORD GENERATOR ")

wordlist=[]
special_char = ["@","#","$","%","&"]
with open("wikipidia-text.txt" ,"r") as file:
    data = file.readlines()
    for line in data:
        words = line.split()

        for item in words:
            if len(item)>5:
                wordlist.append(item.capitalize())

data=random.choice(wordlist)
scar=random.choice(special_char)
num=str(random.randint(10,99))

passw=data+scar+num
print("THIS IS YOUR PASSWORD ==>" ,passw)
print("THANK YOU FOR GETTING YOUR RANDOM READABLE PASSWORD. ")


    
