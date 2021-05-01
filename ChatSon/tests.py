from django.test import TestCase

# Simple logic for Joining and Remove-Duplicate
list1 = [1, 6, 7, 15]
list2 = [3, 7, 15, 19, 20]


final_list = []
rest_list = [y for x in [list1, list2] for y in x]
print(rest_list)

# ==========[ Logic 1 for Remove Duplicate ]==========
# for num in rest_list:
#     if num not in final_list:
#         final_list.append(num)

# ==========[ Logic 2 for Remove Duplicate ]==========
final_list = list(dict.fromkeys(rest_list))
print(final_list)