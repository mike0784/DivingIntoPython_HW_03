arr = [1, 2, 3, 1, 2, 4, 5, 1, 6, 6]
print(arr)
result = []
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in result:
            result.append(arr[i])
            break

print(result)