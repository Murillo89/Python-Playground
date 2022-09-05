import random
import time

#Random number function
# print(random.randint(0, 9))

#Hello World
# print("hello World")


#looper function
# def fruitlooper():

#   fruits = ["apple", "orange", "banana"]
#   for x in fruits:
#     print(x)

# fruitlooper()

# def numLooper():

#   num = range(0, 11)
#   for i in num:
#     print(i)

#   for j in range(5):
#     print(j)

# numLooper()

# seconds = time.time()
# print("Time in seconds since the epoch:", seconds)
# local_time = time.ctime(seconds)
# print("Local time:", local_time)

# print("This is the start of the program.")
# time.sleep(5)
# print("This prints five seconds later.")

#countdown function
# def countDown():

#   num = range(0, 11)
#   for x in num:
#     time.sleep(1)
#     print(x)

# countDown()

# Timer starts
# starttime = time.time()
# lasttime = starttime
# lapnum = 1
# value = ""
  
# print("Press ENTER for each lap.\nType Q and press ENTER to stop.")
  
# while value.lower() != "q":
              
#     # Input for the ENTER key press
#     value = input()
  
#     # The current lap-time
#     laptime = round((time.time() - lasttime), 2)
  
#     # Total time elapsed since the timer started
#     totaltime = round((time.time() - starttime), 2)
  
#     # Printing the lap number, lap-time, and total time
#     print("Lap No. "+str(lapnum))
#     print("Total Time: "+str(totaltime))
#     print("Lap Time: "+str(laptime))
            
#     print("*"*20)
  
#     # Updating the previous total time and lap number
#     lasttime = time.time()
#     lapnum += 1
  
# print("Exercise complete!")

def counting():

  value = ""
  num = 0

  while num != 10:
  
    value = input()
    num += 1
    print(num)

  print("Done counting")

counting()
