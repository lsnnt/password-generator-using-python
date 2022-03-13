from asyncio.windows_events import NULL
import nntplib
from random import randrange


s=['!','@','#','$','%','^','&','*','(',')']
i=str(input("why to use this password! : "))
max=int(input("number of characters : "))
nnt1=""
for n in range(max-4):
    nnt1 = nnt1  +  str(s[randrange(0,10)])
lap=f"{i} ======> {nnt1}nnt1  ."
print(lap)
f=open('passwd.txt','a')
f.write(lap+"\n\n")
f.close()