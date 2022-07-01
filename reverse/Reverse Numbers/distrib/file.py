chars = "`1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM"
chars_num = {}
x = 0
for i in chars:
    chars_num[i] = x
    x += 1

flag = ""
sum_of_nums = 0
sum_of_nums_list = []
for i in flag:
    if sum_of_nums < 100:
        sum_of_nums += chars_num[i]
    elif sum_of_nums > 100:
        sum_of_nums -= chars_num[i]
    sum_of_nums_list.append(sum_of_nums)
print(sum_of_nums_list)
# sum_of_nums_list = [87, 151, 83, 152, 90, 93, 132, 129, 113, 87, 90, 147, 130, 53, 56, 113, 72, 137, 95, 121, 51]
