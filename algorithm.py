"""
# selection sorting
l1=[4,1,5,2,9,85,0]
min_el=4
for i in range(len(l1)):
    min_el=min(l1[i:])
    min_index=l1.index(min_el,i)
    l1[i],l1[min_index]=l1[min_index],l1[i]
print("selection sorting in ascending order :" ,l1)


#bubble sorting
                               # ascending order
l1=[4,1,5,2,9,85,0]
for j in range(len(l1)-1): #to traverse through all element of list
    for i in range(len(l1)-1):
        if l1[i]>l1[i+1]:
            l1[i],l1[i+1]=l1[i+1],l1[i]
            print(l1) # to show each iterations
        else:
            print(l1) # to show each iterations
    print() #to see iterations as bundle as j changes value

print("bubble sorting in ascending order:" ,l1)
                                 #descending order
l1=[4,1,5,2,9,85,0]
for j in range(len(l1)-1): #to traverse through all element of list
    for i in range(len(l1)-1):
        if l1[i]<l1[i+1]:
            l1[i],l1[i+1]=l1[i+1],l1[i]
            print(l1) # to show each iterations
        else:
            print(l1) # to show each iterations
    print() #to see iterations as bundle as j changes value

print("bubble sorting in descending order:" ,l1)

# merge sorting
                                     #ascending order
def mergesort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        left_list=list1[:mid]
        right_list=list1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i,j,k=0,0,0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                list1[k]=left_list[i]
                i+=1
                k+=1
            else:
                list1[k]=right_list[j]
                j+=1
                k+=1
        while i<len(left_list):
            list1[k]=left_list[i]
            i+=1
            k+=1
        while j < len(right_list):
            list1[k] = right_list[j]
            j += 1
            k += 1
num=int(input("how many elements in list :"))
list1=[int(input()) for x in range(num)]
mergesort(list1)
print("Merge_sort in ascending order :", list1)
                                #descending order
def mergesort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        left_list=list1[:mid]
        right_list=list1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i,j,k=0,0,0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]>right_list[j]:
                list1[k]=left_list[i]
                i+=1
                k+=1
            else:
                list1[k]=right_list[j]
                j+=1
                k+=1
        while i<len(left_list):
            list1[k]=left_list[i]
            i+=1
            k+=1
        while j < len(right_list):
            list1[k] = right_list[j]
            j += 1
            k += 1
num=int(input("how many elements in list :"))
list1=[int(input()) for x in range(num)]
mergesort(list1)
print("Merge_sort in descending order :", list1)


                                       # qucik sorting
def pivot_place(list1,first,last):
    pivot=list1[last]
    left=first
    right=last-1
    while True:
        while left<=right and list1[left]>=pivot:
            left=left+1
        while left<=right and list1[right]<=pivot:
            right=right-1
        if right<left:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
        list1[left],list1[last]=list1[last],list1[left]
        return left
def quicksort(list1,first,last):
    if first<last:
        p = pivot_place(list1,first,last)
        print(p)
        quicksort(list1,first,p - 1)
        quicksort(list1,p + 1,last)

list1=[56,25,40,0,4,7,1,0]
n=len(list1)
quicksort(list1,0,n - 1)
print("quick sortingin ascending order :", list1)

                 #Insertion sorting
def Insertion_sort(list1):
    for i in range(1,len(list1)):
        current_element=list1[i]
        pos=i
        while current_element<list1[pos-1] and pos>0:
            list1[pos]=list1[pos-1]
            pos=pos-1
        list1[pos]=current_element
list1=[56,25,40,0,4,7,1,0]
Insertion_sort(list1)
print("Insertion sorting in ascending order :",list1)

# Inserion sort in descending sort
def Insertion_sort(list1):
    for i in range(1,len(list1)):
        current_element=list1[i]
        pos=i
        while current_element>list1[pos-1] and pos>0:
            list1[pos]=list1[pos-1]
            pos=pos-1
        list1[pos]=current_element
list1=[56,25,40,0,4,7,1,0]
Insertion_sort(list1)
print("Insertion sorting in descending order :",list1)

# Shell sorting   in asceding order
def Shell_sort(alist):
    gap=len(alist)//2
    while gap>0:
        for k in range(gap,len(alist)):
            current_element=alist[k]
            pos=k
            while pos>=gap and current_element<alist[pos-gap]:
                alist[pos]=alist[pos-gap]
                pos=pos-gap
            alist[pos]=current_element
        gap = gap//2
alist=[44,20,0,35,3,9,1,0,22]
Shell_sort(alist)
print("shell sorting in ascending order :",alist)

# Shell sorting   in desceding order
def Shell_sort(alist):
    gap=len(alist)//2
    while gap>0:
        for k in range(gap,len(alist)):
            current_element=alist[k]
            pos=k
            while pos>=gap and current_element>alist[pos-gap]:
                alist[pos]=alist[pos-gap]
                pos=pos-gap
            alist[pos]=current_element
        gap = gap//2
alist=[44,20,0,35,3,9,1,0,22]
Shell_sort(alist)
print("shell sorting in descending order :",alist)


# Binary search
def Binary_search(list1,key):
    low=0
    high=len(list1)-1
    Found=False
    while low<=high and not Found:
        mid=(low+high)//2
        if key==list1[mid]:
            Found=True
        elif key>list1[mid]:
            low=mid+1
        else:
            high=mid-1
    if Found==True:
        print("Key is Found")
    else:
        print("Key is not found")
list1=[23,20,45,65,0,5]
list1.sort()
key=int(input("enter the key : "))
Binary_search(list1,key)


# Quick sorting in ascending order
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    piv = lst[0]
    lst = lst[1::]
    lower = []
    greater = []
    for i in lst:
        if i <= piv:
            lower.append(i)
        else:
            greater.append(i)
    sorted_list = quick_sort(lower) + [piv] + quick_sort(greater)
    return sorted_list

lst=[30,45,3,33,0,23,1]
print(quick_sort(lst))

# Quick sorting in descending order
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    piv = lst[0]
    lst = lst[1::]
    lower = []
    greater = []
    for i in lst:
        if i >= piv:
            lower.append(i)
        else:
            greater.append(i)
    sorted_list = quick_sort(lower) + [piv] + quick_sort(greater)
    return sorted_list

lst=[30,45,3,33,0,23,1]
print(quick_sort(lst))

"""

































