# Project Computational Algorithms
# Author: Silvio Dunst
# Student No: G00388192


import random
import time
import pandas as pd
import matplotlib.pyplot as plt


# Start the Main program
def main():
    # Create a Dataframe
    df = pd.DataFrame({'Sample Size':["Bubble Sort","Selection Sort","Quick Sort","Merge Sort","Count Sort"]},index:=None)

    # Create an array with different sample sizes
    samples = [100,250,500,750,1000,1250,2500,3750,5000,10000,20000,40000,80000]
        

    # Create random numbers
    def random_array(n):
        array = []
        for i in range(0,n,1):
            array.append(random.randint(0,100))
        return array

    # Bubble Sort
    # Use the function from GMIT lecture and adopted this to my purpose
    def bubble_sort(bubblearr):
        n = len(bubblearr)
        for outer in range(n-1, 0, -1): # starts at the end of the array n-1 and goes to the start of the array 0 decrease every time by -1
            for inner in range(0,outer,1):#so called bubbling up here
                if bubblearr[inner] > bubblearr[inner+1]:# if not in order swap in the next line
                    temp = bubblearr[inner]
                    bubblearr[inner] = bubblearr[inner+1]# if in order write value in temp variable in the next line
                    bubblearr[inner+1] = temp

    # Selection Sort
    # Use the function from GMIT lecture and adopted this to my purpose
    def selection_sort(selectionarr):
        n = len(selectionarr)
        for outer in range(0,n,1):# the loop runs through each element of the data input array
            min = outer
            for inner in range(outer+1,n,1): # it increments by 1 (outer+1)and searches in every iteration for the smallest element
                if selectionarr[inner] < selectionarr[min]:# if the next element is smaller we write the value in min variable next line if not jump to temp line
                    min = inner # and running through the rest of the array
                    
            temp = selectionarr[outer] # we write the value of first array element in the temp variable
            selectionarr[outer] = selectionarr[min] # we swap write the minimum value of the array to the first element of the array
            selectionarr[min] = temp # we swap write the temp variable value as a minimum value in the array


    # Quick Sort
    #found this code on https://www.educative.io/edpresso/how-to-implement-quicksort-in-python and adopted this to my purpose
    def quick_sort(quickarr):
        elements = len(quickarr)

        #Base case
        if elements < 2:
            return quickarr
        
        current_position = 0 #Position of the partitioning element

        for i in range(1, elements): #Partitioning loop
            if quickarr[i] <= quickarr[0]:
                current_position += 1
                temp = quickarr[i]
                quickarr[i] = quickarr[current_position]
                quickarr[current_position] = temp

        temp = quickarr[0]
        quickarr[0] = quickarr[current_position] 
        quickarr[current_position] = temp #Brings pivot to it's appropriate position
        
        left = quick_sort(quickarr[0:current_position]) #Sorts the elements to the left of pivot
        right = quick_sort(quickarr[current_position+1:elements]) #sorts the elements to the right of pivot

        quickarr = left + [quickarr[current_position]] + right #Merging everything together
        
        return quickarr


    # Merge sort
    # found this code on https://www.geeksforgeeks.org/merge-sort/ and adopted this to my purpose
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

    # Counting sort
    # https://www.geeksforgeeks.org/counting-sort/ and adopted this to my purpose

    def count_sort(countarr):
        max_element = int(max(countarr))
        min_element = int(min(countarr))
        range_of_elements = max_element - min_element + 1

        count_arr = [0 for _ in range(range_of_elements)]# Create a count array for the keys(k) to store count of individual elements and initialize count array as 0
        output_arr = [0 for _ in range(len(countarr))]# Create a output array to store the values of the keys array of individual elements and initialize output array as 0

        for i in range(0, len(countarr)): # Store count of each count array element based on the keys
            count_arr[countarr[i]-min_element] += 1

        for i in range(1, len(count_arr)): # Change count_arr[i] so that count_arr[i] now contains actual position of this element in output array
            count_arr[i] += count_arr[i-1]

        for i in range(len(countarr)-1, -1, -1): # Build the output array 
            output_arr[count_arr[countarr[i] - min_element] - 1] = countarr[i]
            count_arr[countarr[i] - min_element] -= 1

        for i in range(0, len(countarr)):# Copy the output array to arr, so that arr now contains sorted characters
            countarr[i] = output_arr[i]
   
    
    elapsedtimes = []
    elapsedtimesbubblesortall = []
    elapsedtimesselectionsortall = []
    elapsedtimesquicksortall = []
    elapsedtimesmergesortall = []
    elapsedtimescountsortall = []
    sampleindex = 0
    columnposition = 1

    for i in samples: # loops through each sample size 
        sample = random_array(i) # call the random_array function and pass in the array and shuffle around the numbers
        
        sampleruns = range(0,10,1) # runs 10 times through the samples

    
        # Runs through the Bubble sorting function    
        bubbleelapsed_time = 0
        bubbleelapsed_timetotal = 0
        bubbleelapsed_timeaverage = 0
        for run in sampleruns: 
            bubblearr = sample
            bubblestart_time = time.time() # start time of the program count in nanosecond
            bubble_sort(bubblearr) # calls the bubble_sort function here
            bubbleend_time = time.time() # end time of the program count in nanosecond
            bubbleelapsed_time = round((bubbleend_time - bubblestart_time),3) # calculate the time the program runs in milli seconds with 3 decimal places 
            bubbleelapsed_timetotal = bubbleelapsed_timetotal + bubbleelapsed_time # calculate the total time of the all runs
            bubbleelapsed_timeaverage = round(bubbleelapsed_timetotal / len(sampleruns) , 3) # calculate the average time of the all runs in milli seconds with 3 decimal places
        
        elapsedtimesbubblesortall.append(bubbleelapsed_timeaverage)
        elapsedtimes.append(bubbleelapsed_timeaverage) # insert the average time in an Arr
                

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
            selectionelapsed_timetotal = selectionelapsed_timetotal + selectionelapsed_time # calculate the total time of the all runs
            selectionelapsed_timeaverage = round(selectionelapsed_timetotal / len(sampleruns) , 3) # calculate the average time of the all runs in milli seconds with 3 decimal places
            
        elapsedtimesselectionsortall.append(selectionelapsed_timeaverage)
        elapsedtimes.append(selectionelapsed_timeaverage) # insert the average time in an Arr
                    
    
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
            quickelapsed_timetotal = quickelapsed_timetotal + quickelapsed_time # calculate the total time of the all runs
            quickelapsed_timeaverage = round(quickelapsed_timetotal / len(sampleruns) , 3) # calculate the average time of the all runs in milli seconds with 3 decimal places
            
        elapsedtimesquicksortall.append(quickelapsed_timeaverage)
        elapsedtimes.append(quickelapsed_timeaverage) # insert the average time in an Arr
                
        
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
            mergeelapsed_timetotal = mergeelapsed_timetotal + mergeelapsed_time # calculate the total time of the all runs
            mergeelapsed_timeaverage = round(mergeelapsed_timetotal / len(sampleruns) , 3) # calculate the average time of the all runs in milli seconds with 3 decimal places
            
        elapsedtimesmergesortall.append(mergeelapsed_timeaverage)
        elapsedtimes.append(mergeelapsed_timeaverage) # insert the average time in an Arr
                

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
            countelapsed_timetotal = countelapsed_timetotal + countelapsed_time # calculate the total time of the all runs
            countelapsed_timeaverage = round(countelapsed_timetotal / len(sampleruns) , 3) # calculate the average time of the all runs in milli seconds with 3 decimal places
            
        elapsedtimescountsortall.append(countelapsed_timeaverage)
        elapsedtimes.append(countelapsed_timeaverage) # insert the average time in an Arr
        


        # Write a new column in the dataframe after every run
        df.insert(columnposition,str(samples[sampleindex]),elapsedtimes,True)
        sampleindex = sampleindex + 1
        columnposition = columnposition + 1
        elapsedtimes = [] # clear the elapsedtimes array
        print(df)
    
    
    # Plot the Time Results from the Dataframe for Bubble Sort
    fig1, ax1 = plt.subplots(1) 
    ax1.plot(samples,elapsedtimesbubblesortall,c="blue",label="Bubble Sort",marker = 'o',markersize=10)    
    ax1.set_xlabel("Input Size n")
    ax1.set_ylabel("Running Time in ms (milliseconds)")
    ax1.legend()
    ax1.set_title("Bubble Sort \n Worst case O(n2)notation")
    ax1.grid(b=True,which='major',axis='both',linestyle='dotted', linewidth=1)
    fig1.savefig("Bubble sort.png")
    

    # Plot the Time Results from the Dataframe for Selection Sort
    fig2, ax2 = plt.subplots(1) 
    ax2.plot(samples,elapsedtimesselectionsortall,c="orange",label="Selection Sort",marker = 'o',markersize=10)    
    ax2.set_xlabel("Input Size n")
    ax2.set_ylabel("Running Time in ms (milliseconds)")
    ax2.legend()
    ax2.set_title("Selection Sort \n Worst case O(n2)notation")
    ax2.grid(b=True,which='major',axis='both',linestyle='dotted', linewidth=1)
    fig2.savefig("Selection sort.png")

    # Plot the Time Results from the Dataframe for Quick Sort
    fig3, ax3 = plt.subplots(1)
    ax3.plot(samples,elapsedtimesquicksortall,c="red",label="Quick Sort",marker = 'o',markersize=10)    
    ax3.set_xlabel("Input Size n")
    ax3.set_ylabel("Running Time in ms (milliseconds)")
    ax3.legend()
    ax3.set_title("Quick Sort \n Worst case O(n2)notation")
    ax3.grid(b=True,which='major',axis='both',linestyle='dotted', linewidth=1)
    fig3.savefig("Quick sort.png")

    # Plot the Time Results from the Dataframe for Merge Sort
    fig4, ax4 = plt.subplots(1)
    ax4.plot(samples,elapsedtimesmergesortall,c="grey",label="Merge Sort",marker = 'o',markersize=12)    
    ax4.set_xlabel("Input Size n")
    ax4.set_ylabel("Running Time in ms (milliseconds)")
    ax4.legend()
    ax4.set_title("Merge Sort \n Worst case O(n log n)notation")
    ax4.grid(b=True,which='major',axis='both',linestyle='dotted', linewidth=1)
    fig4.savefig("Merge sort.png")

    # Plot the Time Results from the Dataframe for Count Sort
    fig5, ax5 = plt.subplots(1)
    ax5.plot(samples,elapsedtimescountsortall,c="yellow",label="Count Sort",marker = 'o',markersize=10)    
    ax5.set_xlabel("Input Size n")
    ax5.set_ylabel("Running Time in ms (milliseconds)")
    ax5.legend()
    ax5.set_title("Count Sort \n Worst case O(n + k)notation")
    ax5.grid(b=True,which='major',axis='both',linestyle='dotted', linewidth=1)
    fig5.savefig("Count sort.png")

    # Plot the Time Results from the Dataframe for Count Sort       
    fig6, ax6 = plt.subplots(1)
    ax6.plot(samples,elapsedtimesbubblesortall,c="blue",label="Bubble Sort",marker = 'o',markersize=10)
    ax6.plot(samples,elapsedtimesselectionsortall,c="orange",label="Selection Sort",marker = 'o',markersize=10)
    ax6.plot(samples,elapsedtimesquicksortall,c="red",label="Quick Sort",marker = 'o',markersize=10)
    ax6.plot(samples,elapsedtimesmergesortall,c="grey",label="Merge Sort",marker = 'o',markersize=12)
    ax6.plot(samples,elapsedtimescountsortall,c="yellow",label="Count Sort",marker = 'o',markersize=10)    
    ax6.set_xlabel("Input Size n")
    ax6.set_ylabel("Running Time in ms (milliseconds)")
    ax6.legend()
    ax6.set_title("Benchmark of time complexity for differnt\n Sorting algorithms")
    ax6.grid(b=True,which='major',axis='both',linestyle='dotted', linewidth=1)   
    fig6.savefig("Sorting.png")
   


if __name__ == "__main__": # execute only if run from a script
    main() # calls the main program at the start when python start to run
