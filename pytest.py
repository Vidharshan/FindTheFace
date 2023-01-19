def my_method():
    return(1,2,3,4);


for _ in range(10):
    print ("Test")

# Ignore a value when unpacking
a,b,_,d = my_method();
print(a,b,d)
