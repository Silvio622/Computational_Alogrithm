

import random
import time

samples = [100,250,4000] #create an array with different sample sizes

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


elapsedtimesbubblesort = []

for run in range(0,10,1): # runs 10 times through the samples

    # Runs through the bubble_sort sorting function
    for i in samples: # loops through each sample size 
        sample = random_array(i)
        #print("Sample before sorting:" ,sample) # sample before sorting
        bubblearr = sample
        start_time = time.time() # start time of the program count in nanosecond
        bubble_sort(bubblearr) # calls the bubble_sort function here
        end_time = time.time() # end time of the program count in nanosecond
        elapsed_time = round((end_time - start_time),3) # calculate the time the program runs in milli seconds with 3 decimal places 
        print("The elapsed time is: " ,elapsed_time)
        elapsedtimesbubblesort.append(elapsed_time)
        print("Elapsed times in ms are:" ,elapsedtimesbubblesort)
        #print("Sample after sorting:" ,sample)


#sample = random_array(2)
#print(sample)