

import random
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a Dataframe
df = pd.DataFrame({'Algoritms':["Bubble Sort","Selection Sort","Insertion Sort","Quick Sort","Merge Sort"]},index:=None)

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
sampleindex = 0
columnposition = 1

for i in samples: # loops through each sample size 
    sample = random_array(i) # call the random_array function and pass in random numbers

    # Runs through the Bubble sorting function    
    sampleruns = range(0,10,1) # runs 10 times through the samples
    for run in sampleruns: 
        bubblearr = sample
        start_time = time.time() # start time of the program count in nanosecond
        bubble_sort(bubblearr) # calls the bubble_sort function here
        end_time = time.time() # end time of the program count in nanosecond
        elapsed_time = round((end_time - start_time),3) # calculate the time the program runs in milli seconds with 3 decimal places 
        print("The elapsed time is: " ,elapsed_time)
        elapsed_timetotal = elapsed_timetotal + elapsed_time # calculate the total time of the all runs
        elapsed_timeaverage = round(elapsed_timetotal / len(sampleruns) , 3) # calculate the average time of the all runs in milli seconds with 3 decimal places
        #elapsedtimesbubblesort.append(elapsed_time)
        #print("Elapsed times in ms are:" ,elapsedtimesbubblesort)
        print("Total elapsed times" , elapsed_timetotal )
        print("Average running time is" , elapsed_timeaverage)

    elapsedtimesbubblesortall.append(elapsed_timeaverage)
    elapsedtimes.append(elapsed_timeaverage) # insert the average time in an Arr
    print("Elapsed time" , elapsedtimes)
        #print("Sample after sorting:" ,sample)

    # Runs through the Selection sorting function 
    for run in sampleruns: 
        selectionarr = sample
        start_time = time.time() # start time of the program count in nanosecond
        selection_sort(selectionarr) # calls the bubble_sort function here
        end_time = time.time() # end time of the program count in nanosecond
        elapsed_time = round((end_time - start_time),3) # calculate the time the program runs in milli seconds with 3 decimal places 
        print("The elapsed time is: " ,elapsed_time)
        elapsed_timetotal = elapsed_timetotal + elapsed_time # calculate the total time of the all runs
        elapsed_timeaverage = round(elapsed_timetotal / len(sampleruns) , 3) # calculate the average time of the all runs in milli seconds with 3 decimal places
        #elapsedtimesbubblesort.append(elapsed_time)
        #print("Elapsed times in ms are:" ,elapsedtimesbubblesort)
        print("Total elapsed times" , elapsed_timetotal )
        print("Average running time is" , elapsed_timeaverage)

    elapsedtimesselectionsortall.append(elapsed_timeaverage)
    elapsedtimes.append(elapsed_timeaverage) # insert the average time in an Arr
    print("Elapsed time" , elapsedtimes)

    # Runs through the Insertion sorting function 
    for run in sampleruns: 
        insertionarr = sample
        start_time = time.time() # start time of the program count in nanosecond
        insertion_sort(insertionarr) # calls the bubble_sort function here
        end_time = time.time() # end time of the program count in nanosecond
        elapsed_time = round((end_time - start_time),3) # calculate the time the program runs in milli seconds with 3 decimal places 
        print("The elapsed time is: " ,elapsed_time)
        elapsed_timetotal = elapsed_timetotal + elapsed_time # calculate the total time of the all runs
        elapsed_timeaverage = round(elapsed_timetotal / len(sampleruns) , 3) # calculate the average time of the all runs in milli seconds with 3 decimal places
        #elapsedtimesbubblesort.append(elapsed_time)
        #print("Elapsed times in ms are:" ,elapsedtimesbubblesort)
        print("Total elapsed times" , elapsed_timetotal )
        print("Average running time is" , elapsed_timeaverage)

    elapsedtimesinsertionsortall.append(elapsed_timeaverage)    
    elapsedtimes.append(elapsed_timeaverage) # insert the average time in an Arr
    print("Elapsed time" , elapsedtimes)

    # Runs through the Quick sorting function 
    for run in sampleruns: 
        quickarr = sample
        start_time = time.time() # start time of the program count in nanosecond
        quick_sort(quickarr) # calls the quick_sort function here
        end_time = time.time() # end time of the program count in nanosecond
        elapsed_time = round((end_time - start_time),3) # calculate the time the program runs in milli seconds with 3 decimal places 
        print("The elapsed quick sort time is: " ,elapsed_time)
        elapsed_timetotal = elapsed_timetotal + elapsed_time # calculate the total time of the all runs
        elapsed_timeaverage = round(elapsed_timetotal / len(sampleruns) , 3) # calculate the average time of the all runs in milli seconds with 3 decimal places
        #elapsedtimesbubblesort.append(elapsed_time)
        #print("Elapsed times in ms are:" ,elapsedtimesbubblesort)
        print("Total elapsed quick sort times" , elapsed_timetotal )
        print("Average running quick sort time is" , elapsed_timeaverage)

    elapsedtimesquicksortall.append(elapsed_timeaverage)
    elapsedtimes.append(elapsed_timeaverage) # insert the average time in an Arr
    print("Elapsed quick sort time" , elapsedtimes)

    # Runs through the Merge sorting function 
    for run in sampleruns: 
        mergearr = sample
        start_time = time.time() # start time of the program count in nanosecond
        quick_sort(mergearr) # calls the quick_sort function here
        end_time = time.time() # end time of the program count in nanosecond
        elapsed_time = round((end_time - start_time),3) # calculate the time the program runs in milli seconds with 3 decimal places 
        print("The elapsed quick sort time is: " ,elapsed_time)
        elapsed_timetotal = elapsed_timetotal + elapsed_time # calculate the total time of the all runs
        elapsed_timeaverage = round(elapsed_timetotal / len(sampleruns) , 3) # calculate the average time of the all runs in milli seconds with 3 decimal places
        #elapsedtimesbubblesort.append(elapsed_time)
        #print("Elapsed times in ms are:" ,elapsedtimesbubblesort)
        print("Total elapsed merge sort times" , elapsed_timetotal )
        print("Average running merge sort time is" , elapsed_timeaverage)

    elapsedtimesmergesortall.append(elapsed_timeaverage)
    elapsedtimes.append(elapsed_timeaverage) # insert the average time in an Arr
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
plt.xlabel("Samples")
plt.ylabel("Running Time in ms")
plt.legend()
plt.show()
plt

#if __name__ == "__main__": # execute only if run from a script
   # main() # calls the main program at the start when python start to run
