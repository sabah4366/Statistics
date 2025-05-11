import statistics as st

#1- finding mean using statistics - this is the besyt practise  ,mean is sensitive to outliers 
data = [23,24,65,64,65,34]
mean_value = st.mean(data)

#2Median , median is insensitive to outliers
data = [23,24, 22]
median_value = st.median(data)
# print(median_value)

#3 mode - freequency of occurences
#will get first repeated number
data = [21,23,22,22,22,23,23 ]
mode_value = st.mode(data)
# print(mode_value)

#4-multimode will give you multiple occurence values like [23,24]
#multimode will give you repeated values are equal count if the the count of 24 is 2 and 23 is 2 and 25 is 3 then it will show only 25
#but if the 24 is 2 and 23 is 2 and 25 is 2 then show [23,24,25]
# data = [23,24,25,26,27,23,26]
# multi_mode = st.multimode(data)
# print(multi_mode)

#5-Standard deviation
data = [23,87,25,26,124,23,26]
dev= st.stdev(data)
print(dev)

#6 variance
data = [23,87,25,26,124,23,26]
value =st.variance(data)
print(value)

import math
square_root = math.sqrt(value)
print(square_root)

