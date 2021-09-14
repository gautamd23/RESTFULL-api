


def algorithm(arr):
    for i in range(len(arr)):
         for j in range(i+1,len(arr)):
           if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
    return arr

arr = [54,52,8,3,93,4,62,479,2,10,32,6]

print(algorithm(arr))

