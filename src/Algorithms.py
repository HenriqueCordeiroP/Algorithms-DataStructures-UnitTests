class Algorithms:
    def bubblesort(self, array): # comparison in pairs
        for i in range(len(array)-1):
            for j in range(len(array)-1):

                # verify two by two and switch if unordered
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]          

    def insertionsort(self, array): # verify each one
        for i in range(len(array)):

            # select starting index
            j = i

            # verify with previous items to find those larger than the selected item
            # if the first comparation is smaller, the item is in the correct relative place
            while j > 0 and array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]
                j -= 1

    def selectionsort(self, array): # pick and swap
        for i in range(len(array)):
            
            # select item to be compared
            min_index = i
            for j in range(i+1, len(array)):

                # find a smaller value than the selected index
                if array[min_index] > array[j]:

                    # if the value is smaller, update the index
                    min_index = j

                # switch smaller item with currently selected    
            array[min_index], array[i] = array[i], array[min_index]

    def mergesort(self, array): # divide and conquer
        if len(array)>1:
                
            # find middle index
            mid = len(array) // 2

            # divide the array into two equal parts
            left = array[:mid]
            right = array[mid:]

            # recursively repeat the process
            self.mergesort(left)
            self.mergesort(right)

            i = j = k = 0
            
            while i < len(left) and j < len(right):
                
                # compare values in both sides and add the smallest to the final array
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1

            # make sure there aren't values left to be compared
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1

    
    def quicksort(self, array, low, high): # partition and pivot
        if low < high:
           
            # pick the pivot item
            pivot = self._partition(array, low, high)

            # recursively call the function dividing on the pivot
            self.quicksort(array, low, pivot - 1)
            self.quicksort(array, pivot + 1, high)
        

    def _partition(self, array, low, high):

        # set the pivot as the last item in the current array
        pivot = array[high]
        
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1

                array[i], array[j]  = array[j], array[i]


        array[i + 1], array[high] = array[high], array[i + 1]

        return i + 1 

