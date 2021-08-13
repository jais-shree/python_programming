lst = [65,7,23,84,92,12,4,23,21,9]
print(lst,": Before sorting")
lst.sort()
print(lst,": After sorting")
first = 0
last = len(lst)-1
mid = (first + last)//2
item = int(input("Enter the number to search : "))
found = False
while(first<=last and not found):
    mid = (first + last)//2
    if lst[mid] == item:
        print(f"Found at location {mid}")
        found = True
    else:
        if item < lst[mid]:
            last = mid-1
        else:
            first = mid+1

if found == False:
    print("Number not found")