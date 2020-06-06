# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    result = []
    left_pointer = right_pointer = 0 # setting the pointers to 0
    while left_pointer < len(arrA) and right_pointer < len(arrB): # while both pointers are less than the length of the array.
        if arrA[left_pointer] < arrB[right_pointer]: # Checking to see if the left side is bigger than the right.
            result.append(arrA[left_pointer]) # adding the left pointers to the results list
            left_pointer += 1

        else:
            result.append(arrB[right_pointer]) # If not then we are adding to the results list the right side of the array.
            right_pointer += 1

    # If for some reason the lists have values in one but not the other then we
    # are taking the values and then adding them to the end of the array.
    result.extend(arrA[left_pointer:])
    result.extend(arrB[right_pointer:])

    return result


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    midpoint = int(len(arr) / 2)
    left, right = merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:])

    return merge(left, right)


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    start2 = mid + 1
    if arr[mid] <= arr[start2]:
        return arr

    while start <= mid and start2 <= end:
        # If element 1 is in right place
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2
            # Shift all the elements over to make room
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value  # slot in lower value
            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1


def merge_sort_in_place(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
