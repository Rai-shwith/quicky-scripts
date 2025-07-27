def merge_sort(arr,low=0,high=None):
    if high is None:
        high = len(arr)
    if (high - low <= 1):
        return 
    mid = (low + high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid,high)
    merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    temp = []
    left = low
    right = mid
    while (left < mid and right < high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while (left < mid):
        temp.append(arr[left])
        left+=1
    while (right < high):
        temp.append(arr[right])
        right+=1
    arr[low:high]=temp
    return arr
    
if __name__ == "__main__":
    arr = [9,4,5,7,2,1,4,6,8,4,2,6,8,4,3,8]
    merge_sort(arr)
    print(arr)
    