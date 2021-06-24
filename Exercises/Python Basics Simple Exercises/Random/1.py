import random

random.seed(12) #initialize the random number generator

r = random.random() #returns random number
r = random.randint(12,54) 
# print(random.getstate()) #reutrns the current state of the random generator
print(r)