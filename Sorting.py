# Bubble Sort
import random
import time

def random_array(n):
    array = []
    for i in range(0,n,1):
        array.append(random.randint(0,100))
    return array


arr = random.sample(range(-100,10000),10)

def bubble_sort(arr):
    n = len(arr)
    for outer in range(n-1, 0, -1): # starts at the end of the array n-1 and goes to the start of the array 0 decrease every time by -1
        for inner in range(0,outer,1):
            print(f"inner is {inner} swapping {arr[inner]} and {arr[inner+1]}")

            if arr[inner] > arr[inner+1]:
                temp = arr[inner]
                arr[inner] = arr[inner+1]
                arr[inner+1] = temp
                
        print(f"outer is {outer}")
        print(arr)

# array variables
#arr = [7,5,2,3,1]
#arr = random.sample(range(1,100),10)
# call function here 
start_time = time.time_ns() # start time of the program
bubble_sort(arr)
end_time = time.time_ns() # end time of the program
elapsed_time = end_time - start_time # calculate the time the program runs
print("The elapsed time is: " ,elapsed_time)
#print(arr)


# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for outer in range(0,n,1):
        min = outer
        print(f"outer is {outer}")
        for inner in range(outer+1,n,1):
            if arr[inner] < arr[min]:
                min = inner
                
        print(f"min is {min}")
        print(f"swapping {arr[outer]} and {arr[min]}")
        temp = arr[outer]
        arr[outer] = arr[min]
        arr[min] = temp

arr = [7,5,2,3,1]


# call function here 
#selection_sort(arr)
#print(arr)


# Insertion sort

def insertion_sort(arr):
    n = len(arr)
    
    for indexelement in range(1,n,1): # step through each index element start with the second position in step of 1 you don't have to set the step
        keyvalue = arr[indexelement] # use the array element to write the array element value into the key

        previousposition = indexelement - 1 # decrease array index by 1 and write it in a new variable currentposition
        # Move element of array[0...currentposition-1], that are greater than the key, to one position ahead of their current position
        while previousposition >=0 and arr[previousposition] > keyvalue: # the current position must be on indexelement 0 or greater and the 
                                                                        # value of the previuos position must be greater than actual keyvalue
            arr[previousposition + 1] = arr[previousposition] # than increase array index by one (arr[previousposition + 1])and write the value 
                                                            # from the previous index into it
            previousposition = previousposition - 1 # decrease the index previous position by 1
        arr[previousposition + 1] = keyvalue # if the value of the previuos position is not greater than actual keyvalue the while loops stops
                                            # # increase the index previous position by 1 again in the array and write actual value of the 
                                            # arr[indexelement] into it = the keyvalue
       
# array variables
#arr = [7,5,2,3,1]

# call function here 
#insertion_sort(arr)
#print(arr)








#bubble_sort(arr)
#selection_sort(arr)

def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x < lst[0]])) + [lst[0]] + quicksort([x for x in lst[1:] if x > lst[0]])

unsort_list = ["g","a","s","t","1","sdf"]
sorted_list = quicksort(unsort_list)
print(sorted_list)

