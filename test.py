# 冒泡排序法


def bubble_sort(lst):
    count = len(lst)
    if count < 2:
        return lst

    for i in range(count):
        for j in range(1, count - i):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]

    return lst


# 二分查找


def binary_search(arr, start, end, key):
    if start > end:
        return -1
    mid = start + (end - start) / 2

    if arr[mid] > key:
        return binary_search(arr, start, mid - 1, key)
    if arr[mid] < key:
        return binary_search(arr, mid + 1, end, key)

    return mid


# 输出 0-100 之间的素数


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n//2):
        if n % i == 0:
            return False

    return True


for i in range(100):
    if is_prime(i):
        print(i)

l = range(2, 1)
print(l)