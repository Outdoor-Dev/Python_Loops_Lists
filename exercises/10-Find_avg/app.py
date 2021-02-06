my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:

def newAverage(theAverage):
   total = 0
   for x in theAverage:
       total += x
   return(total / len(theAverage))

print(newAverage(my_list))

