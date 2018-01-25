w="11.01.2018"
file=open("text.txt","r")
text=file.read()
file.read(10)
file.close()
c = text.count(w)
while c > 0:
    print(w)
    c -= 1

#print(cont)
#print (file.read(4))
#file.close()
# print(2)

my_file = open("some.txt", "w")
my_file.write("text.txt")
my_file.close()


