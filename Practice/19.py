n = int(input())

arr = list(map(int, input().split()))

sum_of_new_arr = sum(arr)

if sum_of_new_arr % n == 0:
    x = (sum_of_new_arr // n) + 1

print(x)