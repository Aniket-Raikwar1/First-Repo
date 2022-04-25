from logging import root
import math
from unittest.util import _count_diff_all_purpose

# Day - 9 - is perfect square


# def perfect_Sq(A):
#     root = (math.sqrt(A))

#     if root*root == A:
#         return 1
#     else:
#         return 0


# print(perfect_Sq(6))

# T = int(input("Enter testcases:"))
# while T > 0:
#     a = int(input("Enter a number: "))
#     print(perfect_Sq(A=a))
#     T -= 1


# Day - 9 - Square root of a number
# a = int(input("Ente a number: "))

# def solve(A):
#     root = int(math.sqrt(A))
#     print(root)
#     root1 = math.sqrt(A)
#     print((root1))
#     if root == root1:
#         # print(1)
#         return root
#     else:
#         return -1

# print(solve(A=a))

# ----------------------------------------

# Day - 8 - Half diamond
# N = int(input())
# j = 0
# for i in range(2*N - 1):
#     i = j
#     # for j in range():
#     while j <= 2*N - 1:
#         if j <= (2*N - 1)//2:
#             # print((2*N - 1)//2)
#             print("*", end="")
#             j += 1
#         print()

# pass


# ----------------------------------------

# Day - 8 - Full Numeric Pyramid

# ----------------------------------------

# Day - 7 - Star Pattern II

# -----------------------------------------

# Day - 6- Bank account
# N = int(input("N: "))
# M = int(input("M: "))

# for i in range(M):
#     Type = int(input("Type- 1 or 2: "))
#     X = int(input("Enter amount: "))
#     if Type == 1:
#         Balance = N + X
#         print(Balance)
#     elif Type == 2:
#         Balance = N - X
#         if Balance < 0:
#             print("Insufficient Funds")
#         else:
#             print(Balance)
#

# --------------------------------------------

# Day - 6 - Count of digits
# T = int(input("How many testcases? :"))

# # count_ = 0
# while T > 0:
#     count_ = 0

#     N = int(input("Ente the number: "))
#     while N > 0:
#         count_ += 1
#         print("count:", count_)
#         N = N // 10
#         print("Currently N:", N)
#     print("Final:", count_)
#     T -= 1
#     print("Currently T:", T)

# -------------------------------------------

# Day - 4 - Percentage and Grade

# A, B, C, D, E = input().split()
# Total = int(A) + int(B) + int(C) + int(D) + int(E)
# percentage = (Total*100)//500
# # print(percentage)

# if percentage >= 90:
#     print(percentage, "A")
# elif percentage >= 80:
#     print(percentage, "B")
# elif percentage >= 70:
#     print(percentage, "C")
# elif percentage >= 60:
#     print(percentage, "D")
# elif percentage >= 40:
#     print(percentage, "E")
# else:
#     print(percentage, "F")

# -------------------------------------

#  Day - 4 - Is it a leap year?
