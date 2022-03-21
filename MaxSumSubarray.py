def getMaxContiguousSum(array):
    """
    Takes as input an array of integers and returns the contiguous subarray,
    which has the largest sum and the sum itself.
    :param
            array : array containing integer numbers
    :return
            maxSum: largest integer sum among all the contiguous subarrays
            correspondingArray: contiguous subarray which gives the maxSum
    """
    try:
        #Check whether the array is empty
        if len(array)==0:
            return 0,[]

        #Check whether the array contains a non valid input
        for i in array:
            if not (type(i)==int or type(i)==float):
                return "TypeError"


        #maxSum will contain the final outcome
        maxSum = max(array)

        # keep track of the array which gives the maximum sum. Initially they are set to the maximum sum returned by
        # the array containing a single element.

        startIndex = endIndex = array.index(maxSum)

        #The first cycle loops through all the item of the array
        for i in range(len(array)):

            #tempSum stores the maximum sum found so far, which contains in a first moment, the first element of the array
            tempSum = array[i]

            #The nested loop explores all the possible contiguous arrays from the first element of the array all the way
            #right and stores the maximum sum and its indices in the appropriate variables.
            #It terminates its execution once it reaches the last number of the array.
            #Afterward i increments, the nested loop starts again.
            for j in range(i + 1, len(array)):

                #tempSum is equal to the previous value plus the current item of the list
                tempSum = tempSum + array[j]

                #it checks whether the temporary sum is greater than the maximum sum found so far (maxSum)
                #if that's the case, it updates the maxSum value and the indices of the array
                if tempSum >= maxSum:
                    maxSum = tempSum
                    startIndex = i
                    endIndex = j

        #Once the end of the loop, we finally got the desired outputs.
        return maxSum, array[startIndex:endIndex + 1]

    except Exception as e:
        print(e)
