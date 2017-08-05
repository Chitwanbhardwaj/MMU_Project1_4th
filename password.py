import random
opt = ['1','2','3','4','5','6','7','8','9','0']
choice = raw_input("enter numbers-")
sel = list(choice) + opt
z=[]
pwd = int(raw_input("enter password length -"))
for x in range(pwd):
    z.append(random.choice(sel))

pswd =str(''.join(z))

print pswd
