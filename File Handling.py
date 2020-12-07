
### ==================================File Handdling=======================

# ----------------Reading File------------------
# f = open('new.txt')
# cmt = f.read() # or print(f.read())
# print(cmt)
# f.close()

# Reading line by line
# for line in f:
#     print(line, end="")

# Using readline/s () Function
# print(f.readline(4))
# print(f.readlines())


# ----------------Writing Mode on FIles---------------
# f = open('new1.txt', 'w')
# cmt = f.write(' New Written Text.')
# print(cmt) # tells number of letter writtened or assigned to the file
#  #------------------appending txt------------
# f = open('new1.txt', 'a')
# cmt = f.write(' New Written Text.\n')
# print(cmt)
# f.close()


## using read and write mode wee can ead and write data at same time
# f = open('new1.txt', 'r+')
# cmt = f.write(' New Written Text.\n')
# print(cmt)
# f.close()



# ========================Seek And Tell in File handling======================
## tell() func tells position file pointer and seek() func locates fpointer

# a = open("new.txt")
# a.seek(0)  # Maker filepointer position at 0
# print(a.tell())
# print(a.readline())
# print(a.tell())
# print(a.seek(8))
# print(a.readline())
# data = a.read()
# print(data)


## this works
# with open('new.txt') as f:
#     a = f.read()
#     print(a)
#
# f = open('new.txt')
# dta = f.read()
# print(dta)
