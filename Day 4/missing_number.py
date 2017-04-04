"""Missing Number Function"""

def find_missing(array1,array2):
    #if given arrays are both null return 0
    if len(array1)==0 and len(array2)==0:
        return 0
    # if array1 is longer than array2 loop to see which value is missing in array2
    elif len(array1)>len(array2):
        for i in array1:
            if i in array2:
                pass
            else:
                return i   #return the missing value
    #if array2 is longer than array1 loop to see which value is missing in array1
    elif len(array2)>len(array1):
        for i in array2:
            if i in array1:
                pass
            else:
                return i #return the missing value
    #else the arrays are equal then just like the null arrays, return 0
    else:
        return 0