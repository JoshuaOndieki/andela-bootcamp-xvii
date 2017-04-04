#maximum and minimum numbers generator

def find_max_min(numbers):
  max_min_array=[] #create list to hold the min and max values
  max_min_array.append(min(numbers)) #append to the list: min value at index 0
  max_min_array.append(max(numbers)) #                    max value at index 1
  if max_min_array[0]==max_min_array[1]: #if the value of min is equal to value of max
    num_of_elements = []
    num_of_elements.append(len(numbers))
    return num_of_elements                #                 return the number of elements
  else:
    return max_min_array #return the list with min and max values respectively

