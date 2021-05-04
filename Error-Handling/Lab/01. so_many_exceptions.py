

# You are provided with a code that raises many exceptions. Fix it, so it works correctly.

# numbers_list = input().split(", ")
# result = 0
#
# for i in range(numbers_list):
#     number = numbers_list[i + 1]
#     if number < 5:
#         result *= number
#     elif number > 5 and number > 10:
#         result /= number
#
# print(result)


numbers_list = map(int, input().split(", "))
result = 1

for number in numbers_list:
    if number <= 5:
        result *= number
    elif number <= 10:
        result /= number

print(int(result))

