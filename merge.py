lst=[]
def merge(lst):
    if len(lst)>1:
        mid=len(lst)//2
        left=lst[:mid]
        right=lst[mid:]
        merge(left)
        merge(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                lst[k]=left[i]
                i+=1
                k+=1
            else:
                lst[k]=right[j]
                j+=1
                k+=1
        while i<len(left):
            lst[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            lst[k]=right[j]
            j+=1
            k+=1
n=int(input())
lst=list(map(int,input().split()))
merge(lst)
for i in range(len(lst)):
    if lst[i]==lst[len(lst)-1]:
        print(lst[i])
    else:
        print(lst[i],end=" ")

