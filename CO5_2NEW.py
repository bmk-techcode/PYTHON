ofile=open("file.txt","r")
content=ofile.readlines()
l=len(content)

feven=open("evenfile.txt","w")
fodd=open("oddfile.txt","w")

for i in range(l):
    if i%2==0:
        
        feven.write(content[i])

    else:
        fodd.write(content[i])
print("FILE UPDATED ....")
ofile.close()
feven.close()
fodd.close()
