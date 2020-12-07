
# austro * patterns



#  # In This Program We cannot use like this
# # 1.)     new = bool(input('Enter '));
# #      -----    AND    ------
# # b = int(input('Enter 1 or 0 number: '));
# # new = bool(b);



# # ----------------------If-loop Method-------------------
# a = int(input('Enter a number: '));
# b = int(input('Enter 1 or 0 number: '));
# new = bool(b);
#
# if new == True:
#     for i in range (1, a+1):
#         # print(i)
#         for j in range (1, i+1):
#             print("*", end=" ");
#         print();
# elif new == False:
#     for i in range (a+1, 0, -1):
#         # print(i)
#         for j in range (1, i+1):
#             print("*", end="");
#         print();



# -----------------------Using Function--------------------------
# ===========Func-1===============
# a = int(input("Enter First Number: \n"))
# b = int(input("Enter 0 or 1 Number: \n"))
# new = bool(b)
# def pattern(a,b):
#     if new == True:
#         for i in range (1, a+1):
#             for j in range (1, i+1):
#                 print("*", end=" ");
#             print();
#     elif new == False:
#         for i in range (a+1, 0, -1):
#             for j in range (1, i+1):
#                 print("*", end="");
#             print();
#
#
# pattern(a, b);



# =====================Func 2=======================
# a = int(input("Enter First Number: \n"))
# b = int(input("Enter 0 or 1 Number: \n"))
# new = bool(b)
# def pattern(a, new):
#     if new == True:
#         c =1;
#         while c <=a:
#             print("*"*c);
#             c =c+1;
#     else:
#         while a > 0:
#             print("*"*a)
#             a =a-1;
#
# pattern(a, b)
#
# =============================Using Try Except Exception============
# try:
#     a = int(input('Enter a number: '));
#     b = int(input('Enter 1 or 0 number: '));
#     new = bool(b);
#
#     if new == True:
#         for i in range (1, a+1):
#         # print(i)
#             for j in range (1, i+1):
#                 print("*", end=" ");
#             print();
#     elif new == False:
#         for i in range (a+1, 0, -1):
#             # print(i)
#             for j in range (1, i+1):
#                 print("*", end=" ");
#             print("");
#
# except Exception as e:
#     print("Your Input is Wrong Please Input Corrrect Values!!1")



# # Short Method
# i=1
# for j in range(1,7):
#     print( j*"*")
#     i=i+1


# # ===========================Opposite Direction Pattern==========================
# i=1
# # for j in range(7,0,-1):
#     print(i*" " + j*"*")
#     i=i+1


# # =======Second methd======
# i=7
# for j in range(1,7):
#     print( i*" "+j*"*")
#     i=i-1





# ---------With User Input----
# num = int(input("enter a num: "))
# a=1
# for j in range(num,0,-1):
#     print(a*" " + j*"*")
#     a=a+1




# =========================V shape Pattern=======================
# i=0
# for j in range(11, 0 , -2):
#     print(i*' ' + j*'*');
#     i=i+1;


