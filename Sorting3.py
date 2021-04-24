
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

def bubble_sort(bubblearr):
    n = len(bubblearr)
    for outer in range(n-1, 0, -1): # starts at the end of the array n-1 and goes to the start of the array 0 decrease every time by -1
        for inner in range(0,outer,1):
            #print(f"inner is {inner} swapping {arr[inner]} and {arr[inner+1]}")

            if bubblearr[inner] > bubblearr[inner+1]:
                temp = bubblearr[inner]
                bubblearr[inner] = bubblearr[inner+1]
                bubblearr[inner+1] = temp
                
        #print(f"outer is {outer}")
        #print(arr)


# Selection Sort
def selection_sort(selectionarr):
    n = len(selectionarr)
    for outer in range(0,n,1):
        min = outer
        #print(f"outer is {outer}")
        for inner in range(outer+1,n,1):
            if selectionarr[inner] < selectionarr[min]:
                min = inner
                
        #print(f"min is {min}")
        #print(f"swapping {arr[outer]} and {arr[min]}")
        temp = selectionarr[outer]
        selectionarr[outer] = selectionarr[min]
        selectionarr[min] = temp

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

# Quick Sort
def quick_sort(quickarr):
    if not quickarr:
        return []
    return (quick_sort([x for x in quickarr[1:] if x < quickarr[0]])) + [quickarr[0]] + quick_sort([x for x in quickarr[1:] if x > quickarr[0]])


# Merger sort
# found this code on https://www.geeksforgeeks.org/merge-sort/ and adopted this

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


#mergearr = [7,5,2,3,1]

# call function here 
#merge_sort(arr)
#print(mergearr)

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

#countarr = [7,5,2,3,1]

# call function here 
#count_sort(countarr)
#print(countarr)

#def main():  

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

    # Runs through the Bubble sorting function    
    sampleruns = range(0,10,1) # runs 10 times through the samples
    #'''
    bubbleelapsed_time = 0
    bubbleelapsed_timetotal = 0
    bubbleelapsed_timeaverage = 0
    for run in sampleruns: 
        bubblearr = sample
        bubblestart_time = time.time() # start time of the program count in nanosecond
        bubble_sort(bubblearr) # calls the bubble_sort function here
        bubbleend_time = time.time() # end time of the program count in nanosecond
        bubbleelapsed_time = round((bubbleend_time - bubblestart_time),3) # calculate the time the program runs in milli seconds with 3 decimal places 
        print("The elapsed time is: " ,bubbleelapsed_time)
        bubbleelapsed_timetotal = bubbleelapsed_timetotal + bubbleelapsed_time # calculate the total time of the all runs
        bubbleelapsed_timeaverage = round(bubbleelapsed_timetotal / len(sampleruns) , 3) # calculate the average time of the all runs in milli seconds with 3 decimal places
        #elapsedtimesbubblesort.append(elapsed_time)
        #print("Elapsed times in ms are:" ,elapsedtimesbubblesort)
        print("Total elapsed times" , bubbleelapsed_timetotal )
        print("Average running time is" , bubbleelapsed_timeaverage)

    elapsedtimesbubblesortall.append(bubbleelapsed_timeaverage)
    elapsedtimes.append(bubbleelapsed_timeaverage) # insert the average time in an Arr
    print("Elapsed time" , elapsedtimes)
        #print("Sample after sorting:" ,sample)
    #'''
    #'''
    # Runs through the Selection sorting function 
    selectionelapsed_time = 0
    selectionelapsed_timetotal = 0
    selectionelapsed_timeaverage = 0

    for run in sampleruns: 
        selectionarr = sample
        selectionstart_time = time.time() # start time of the program count in nanosecond
        selection_sort(selectionarr) # calls the bubble_sort function here
        selectionend_time = time.time() # end time of the program count in nanosecond
        selectionelapsed_time = round((selectionend_time - selectionstart_time),3) # calculate the time the program runs in milli seconds with 3 decimal places 
        print("The elapsed time is: " ,selectionelapsed_time)
        selectionelapsed_timetotal = selectionelapsed_timetotal + selectionelapsed_time # calculate the total time of the all runs
        selectionelapsed_timeaverage = round(selectionelapsed_timetotal / len(sampleruns) , 3) # calculate the average time of the all runs in milli seconds with 3 decimal places
        #elapsedtimesbubblesort.append(elapsed_time)
        #print("Elapsed times in ms are:" ,elapsedtimesbubblesort)
        print("Total elapsed times" , selectionelapsed_timetotal )
        print("Average running time is" , selectionelapsed_timeaverage)

    elapsedtimesselectionsortall.append(selectionelapsed_timeaverage)
    elapsedtimes.append(selectionelapsed_timeaverage) # insert the average time in an Arr
    print("Elapsed time" , elapsedtimes)
    #'''
    #'''
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
    #'''
    #'''
    # Runs through the Quick sorting function 
    quickelapsed_time = 0
    quickelapsed_timetotal = 0
    quickelapsed_timeaverage = 0

    for run in sampleruns: 
        quickarr = sample
        quickstart_time = time.time() # start time of the program count in nanosecond
        quick_sort(quickarr) # calls the quick_sort function here
        quickend_time = time.time() # end time of the program count in nanosecond
        quickelapsed_time = round((quickend_time - quickstart_time),3) # calculate the time the program runs in milli seconds with 3 decimal places 
        print("The elapsed quick sort time is: " ,quickelapsed_time)
        quickelapsed_timetotal = quickelapsed_timetotal + quickelapsed_time # calculate the total time of the all runs
        quickelapsed_timeaverage = round(quickelapsed_timetotal / len(sampleruns) , 3) # calculate the average time of the all runs in milli seconds with 3 decimal places
        #elapsedtimesbubblesort.append(elapsed_time)
        #print("Elapsed times in ms are:" ,elapsedtimesbubblesort)
        print("Total elapsed quick sort times" , quickelapsed_timetotal )
        print("Average running quick sort time is" , quickelapsed_timeaverage)

    elapsedtimesquicksortall.append(quickelapsed_timeaverage)
    elapsedtimes.append(quickelapsed_timeaverage) # insert the average time in an Arr
    print("Elapsed quick sort time" , elapsedtimes)
    #'''
    #'''
    # Runs through the Merge sorting function 
    mergeelapsed_time = 0
    mergeelapsed_timetotal = 0
    mergeelapsed_timeaverage = 0

    for run in sampleruns: 
        mergearr = sample
        mergestart_time = time.time() # start time of the program count in nanosecond
        merge_sort(mergearr) # calls the quick_sort function here
        mergeend_time = time.time() # end time of the program count in nanosecond
        mergeelapsed_time = round((mergeend_time - mergestart_time),3) # calculate the time the program runs in milli seconds with 3 decimal places 
        print("The elapsed quick sort time is: " ,mergeelapsed_time)
        mergeelapsed_timetotal = mergeelapsed_timetotal + mergeelapsed_time # calculate the total time of the all runs
        mergeelapsed_timeaverage = round(mergeelapsed_timetotal / len(sampleruns) , 3) # calculate the average time of the all runs in milli seconds with 3 decimal places
        #elapsedtimesbubblesort.append(elapsed_time)
        #print("Elapsed times in ms are:" ,elapsedtimesbubblesort)
        print("Total elapsed merge sort times" , mergeelapsed_timetotal )
        print("Average running merge sort time is" , mergeelapsed_timeaverage)

    elapsedtimesmergesortall.append(mergeelapsed_timeaverage)
    elapsedtimes.append(mergeelapsed_timeaverage) # insert the average time in an Arr
    print("Elapsed merge sort time" , elapsedtimes)
    #'''

    # Runs through the Count sorting function 
    countelapsed_time = 0
    countelapsed_timetotal = 0
    countelapsed_timeaverage = 0

    for run in sampleruns: 
        countarr = sample
        countstart_time = time.time() # start time of the program count in nanosecond
        count_sort(countarr) # calls the quick_sort function here
        countend_time = time.time() # end time of the program count in nanosecond
        countelapsed_time = round((countend_time - countstart_time),3) # calculate the time the program runs in milli seconds with 3 decimal places 
        print("The elapsed quick sort time is: " ,countelapsed_time)
        countelapsed_timetotal = countelapsed_timetotal + countelapsed_time # calculate the total time of the all runs
        countelapsed_timeaverage = round(countelapsed_timetotal / len(sampleruns) , 3) # calculate the average time of the all runs in milli seconds with 3 decimal places
        #elapsedtimesbubblesort.append(elapsed_time)
        #print("Elapsed times in ms are:" ,elapsedtimesbubblesort)
        print("Total elapsed merge sort times" , countelapsed_timetotal )
        print("Average running merge sort time is" , countelapsed_timeaverage)

    elapsedtimescountsortall.append(countelapsed_timeaverage)
    elapsedtimes.append(countelapsed_timeaverage) # insert the average time in an Arr
    print("Elapsed merge sort time" , elapsedtimes)




    # Write a new column in the dataframe after every run
    df.insert(columnposition,str(samples[sampleindex]),elapsedtimes,True)
    sampleindex = sampleindex + 1
    columnposition = columnposition + 1
    elapsedtimes = [] # clear the elapsedtimes array
    print(df)

    print(elapsedtimesbubblesortall)
    print(elapsedtimesselectionsortall)
    print(elapsedtimesinsertionsortall)
    print(elapsedtimesquicksortall)
    print(elapsedtimesmergesortall)
    print(elapsedtimescountsortall)

    # plot the Time Results from the Dataframe
#plt.plot(data=df)
#sns.scatterplot(x="Sample Size",y="Running Times in (ms)",data=df,hue="Algoritms")
#sns.scatterplot(x="2000",y="Algoritms",data=df,hue="Algoritms")
#sns.scatterplot(x=samples,y="Bubble Sort",data=df,hue="Algoritms")
#sns.scatterplot(data=df,hue="Algoritms")
##plt.scatter(samples,elapsedtimesbubblesortall,c="red",label="Bubble Sort")
##plt.scatter(samples,elapsedtimesselectionsortall,c="blue",label="Selection Sort")
##plt.scatter(samples,elapsedtimesinsertionsortall,c="green",label="Insertion Sort")
plt.plot(samples,elapsedtimesbubblesortall,c="blue",label="Bubble Sort",marker = 'o',markersize=10)
plt.plot(samples,elapsedtimesselectionsortall,c="orange",label="Selection Sort",marker = 'o',markersize=10)
plt.plot(samples,elapsedtimesinsertionsortall,c="green",label="Insertion Sort",marker = 'o',markersize=10)
plt.plot(samples,elapsedtimesquicksortall,c="red",label="Quick Sort",marker = 'o',markersize=10)
plt.plot(samples,elapsedtimesmergesortall,c="grey",label="Merge Sort",marker = 'o',markersize=10)
plt.plot(samples,elapsedtimescountsortall,c="yellow",label="Count Sort",marker = 'o',markersize=10)
plt.xlabel("Samples")
plt.ylabel("Running Time in ms")
plt.legend()
plt.show()
plt

#if __name__ == "__main__": # execute only if run from a script
   # main() # calls the main program at the start when python start to run
