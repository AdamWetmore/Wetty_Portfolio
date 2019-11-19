def stray(arr):
    if arr[0] == arr[1]:
        for i in range(1,len(arr)):
            if arr[i] != arr[0]:
                result = arr[i]
                break
    else:
        if arr[0] == arr[2]:
            result = arr[1]
        else:
            result = arr[0]
    return result
