f=open("test.txt","w")
new=[]
while True:
    new.append(input("Enter new prize: ")+"\n")
    r=input("Continue? y/n ")
    if r=='n' or r=='N':
        break
    else:
        continue
f.writelines(new)
f.close()
