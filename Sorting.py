# Bubble Sort
'''
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

def quick_sort(quickarr):
    if not quickarr:
        return []
    return (quick_sort([x for x in quickarr[1:] if x < quickarr[0]])) + [quickarr[0]] + quick_sort([x for x in quickarr[1:] if x > quickarr[0]])

unsort_list = ["g","a","s","t","1","sdf"]
sorted_list = quick_sort(unsort_list)
print(sorted_list)

'''
'''
# Merger sort
# https://www.geeksforgeeks.org/merge-sort/

def merge_sort(mergearr):
    if len(mergearr)>1:
        mid = len(mergearr)//2 # Finding the mid of the array
        left = mergearr[:mid] # Dividing the array elements into left from middle
        right = mergearr[mid:] # Dividing the array elements into right from middle
        merge_sort(left) # Sorting the left half
        merge_sort(right) # Sorting the right half
        i = j = k = 0 # set the array index i,j,k to 0

        while i < len(left) and j < len(right):# Copy data to temp arrays left[] and right[]
            if left[i] < right[j]:
                mergearr[k] = left[i]
                i = i + 1 # increment the index i for the left side
            else:
                mergearr[k] = right[j]
                j = j + 1 # increment the index j for the right side
            k = k + 1 # increment the index k for the mergearr

        while i < len(left): # Checking if any element was on the left side
            mergearr[k] = left[i] # write the left index i value in the mergearr on the appropiate position
            i = i + 1 # increment the index i for the left side
            k = k + 1 # increment the index k for the mergearr

        while j < len(right): # Checking if any element was on the right side
            mergearr[k] = right[j] # write the right index j value in the mergearr on the appropiate position
            j = j + 1 # increment the index j for the right side
            k = k + 1 # increment the index k for the mergearr


mergearr = [7,5,2,3,1]

# call function here 
merge_sort(arr)
print(mergearr)
'''
'''
# Counting sort
# https://www.geeksforgeeks.org/counting-sort/

def count_sort(countarr):
    max_element = int(max(countarr))
    min_element = int(min(countarr))
    range_of_elements = max_element - min_element + 1

    count_arr = [0 for _ in range(range_of_elements)]# Create a count array to store count of individual elements and initialize count array as 0
    output_arr = [0 for _ in range(len(countarr))]# Create a output array to store the count array of individual elements and initialize output array as 0

    for i in range(0, len(countarr)): # Store count of each count array element
        count_arr[countarr[i]-min_element] += 1

    for i in range(1, len(count_arr)): # Change count_arr[i] so that count_arr[i] now contains actual position of this element in output array
        count_arr[i] += count_arr[i-1]

    for i in range(len(countarr)-1, -1, -1): # Build the output array 
        output_arr[count_arr[countarr[i] - min_element] - 1] = countarr[i]
        count_arr[countarr[i] - min_element] -= 1

    for i in range(0, len(countarr)):# Copy the output array to arr, so that arr now contains sorted characters
        countarr[i] = output_arr[i]

    #return countarr

countarr = [7,5,2,3,1]

# call function here 
count_sort(countarr)
print(countarr)
'''

import random
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a Dataframe
df = pd.DataFrame({'Algoritms':["Bubble Sort","Selection Sort","Insertion Sort","Quick Sort","Merge Sort","Count Sort"]},index:=None)

samples = [100,200,500,1000,5000] #create an array with different sample sizes

def random_array(n):
    array = []
    for i in range(0,n,1):
        array.append(random.randint(0,100))
    return array

# Insertion Sort
def insertion_sort(insertionarr):
    n = len(insertionarr)
    
    for indexelement in range(1,n,1): # step through each index element start with the second position in step of 1 you don't have to set the step
        keyvalue = insertionarr[indexelement] # use the array element to write the array element value into the key

        previousposition = indexelement - 1 # decrease array index by 1 and write it in a new variable currentposition
        # Move element of array[0...currentposition-1], that are greater than the key, to one position ahead of their current position
        while previousposition >=0 and insertionarr[previousposition] > keyvalue: # the current position must be on indexelement 0 or greater and the 
                                                                        # value of the previuos position must be greater than actual keyvalue
            insertionarr[previousposition + 1] = insertionarr[previousposition] # than increase array index by one (arr[previousposition + 1])and write the value 
                                                            # from the previous index into it
            previousposition = previousposition - 1 # decrease the index previous position by 1
        insertionarr[previousposition + 1] = keyvalue # if the value of the previuos position is not greater than actual keyvalue the while loops stops
                                            # # increase the index previous position by 1 again in the array and write actual value of the 
                                            # arr[indexelement] into it = the keyvalue


#elapsedtimesbubblesort = []
elapsed_timetotal = 0
elapsed_timeaverage = 0
elapsedtimes = []
elapsedtimesbubblesortall = []
elapsedtimesselectionsortall = []
elapsedtimesinsertionsortall = []
elapsedtimesquicksortall = []
elapsedtimesmergesortall = []
elapsedtimescountsortall = []
sampleindex = 0
columnposition = 1

for i in samples: # loops through each sample size 
    sample = random_array(i) # call the random_array function and pass in the array and shuffle around the numbers

    sampleruns = range(0,10,1) # runs 10 times through the samples

    # Runs through the Insertion sorting function
    insertionelapsed_time = 0
    insertionelapsed_timetotal = 0
    insertionelapsed_timeaverage = 0

    for run in sampleruns: 
        insertionarr = sample
        insertionstart_time = time.time() # start time of the program count in nanosecond
        insertion_sort(insertionarr) # calls the bubble_sort function here
        insertionend_time = time.time() # end time of the program count in nanosecond
        insertionelapsed_time = round((insertionend_time - insertionstart_time),3) # calculate the time the program runs in milli seconds with 3 decimal places 
        print("The elapsed time is: " ,insertionelapsed_time)
        insertionelapsed_timetotal = insertionelapsed_timetotal + insertionelapsed_time # calculate the total time of the all runs
        insertionelapsed_timeaverage = round(insertionelapsed_timetotal / len(sampleruns) , 3) # calculate the average time of the all runs in milli seconds with 3 decimal places
        #elapsedtimesbubblesort.append(elapsed_time)
        #print("Elapsed times in ms are:" ,elapsedtimesbubblesort)
        print("Total elapsed times" , insertionelapsed_timetotal )
        print("Average running time is" , insertionelapsed_timeaverage)

    elapsedtimesinsertionsortall.append(insertionelapsed_timeaverage)    
    elapsedtimes.append(insertionelapsed_timeaverage) # insert the average time in an Arr
    print("Elapsed time" , elapsedtimes)
    



