# # def is_leapYear(year):
# #     leap = False
# #     if year // 4 ==0:
# #         return leap
# #     elif:
# def isLeapYear(year):
#     if year%4 == 0:
#         if year%100 == 0:
#             if year%400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
# n = int(input())
# print(isLeapYear(n))

def is_leap(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year = int(input())
print(is_leap(year))