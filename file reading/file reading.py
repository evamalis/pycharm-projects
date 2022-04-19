myfile=open('song.txt','w')
#for line in myfile:
#    print(line)
myfile.write("tttt")
print("zzzz", file=myfile)
myfile=open('song.txt', 'r')
print(myfile.read())