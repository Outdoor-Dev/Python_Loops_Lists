import random
#Remember import random function here:

my_list = [4,5,734,43,45]

#The magic is here:

for i in range(10):
    my_list.append(random.randint(0,11))

    print(my_list)