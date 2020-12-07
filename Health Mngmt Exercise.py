
# #####======================================CWH Health Mngmt Exercise===============================================================
# # Function For Date Time

# def time():
#     import datetime
#     return datetime.datetime.now()
# def add(k):
#  #  =================================For Noah====================
#     if k==1:
#         a = int(input("Enter 1 for exercise and 2 for food : \n"))
#         if (a == 1):
#             value = input("Enter here: \n")
#             with open('Noah-Ex.txt', 'a') as opn:
#                 opn.write( str([str(time())])+ ": " + value  + "\n")
#                 print("Written Successfully.")
#         elif a== 2:
#             value = input("Enter here: \n")
#             with open('Noah-Food.txt', 'a') as opn:
#                 opn.write( str([str(time())])+ ": " + value  + "\n")
#                 print("Written Successfully.")
# #  =================================For Adam====================
#     elif k==2:
#         a = int(input("Enter 1 for exercise and 2 for food : \n"))
#         if a== 1:
#             value = input("Enter here: \n")
#             with open('Adam-Ex.txt', 'a') as opn:
#                 opn.write( str([str(time())])+ ": " + value  + "\n")
#                 print("Written Successfully.")
#         elif a == 2:
#             value = input("Enter here: \n")
#             with open('Adam-Food.txt', 'a') as opn:
#                 opn.write( str([str(time())])+ ": " + value  + "\n")
#                 print("Written Successfully.")
#         else:
#             print("Invalid input.")
#     else:
#         print("Invalid input!!")
# #  =================================Retrive====================
# def retrive(k):
#     if k == 1:
#         a = int(input("Enter 1 for exercise and 2 for food : \n"))
#         if a == 1:
#             with open("Noah-Ex.txt") as opn:
#                 for i in opn:
#                     print(i, end=" ")
#         if a == 2:
#             with open("Noah-Food.txt") as opn:
#                 for i in opn:
#                     print(i, end=" ")
#     elif k == 2:
#         a = int(input("Enter 1 for exercise and 2 for food : \n"))
#         if a == 1:
#             with open("Adam-Ex.txt") as opn:
#                 for i in opn:
#                     print(i, end=" ")
#         if a == 2:
#             with open("Adam-Food.txt") as opn:
#                 for i in opn:
#                     print(i, end=" ")
# # # ===============Invoking Functions============
# s = int(input("Enter 1 for Add, 2 For Retrive"))
# if s==1:
#     c = int(input("Enter 1 For Noah 2 For Adam"))
#     add(c)
# else:
#     c = int(input("Enter 1 For Noah 2 For Adam"))
#     retrive(c)
