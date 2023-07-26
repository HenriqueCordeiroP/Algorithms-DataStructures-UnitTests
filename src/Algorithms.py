class Algorithms:
    def bubblesort(self, array):
        for i in range(len(array)-1):
            for j in range(len(array)-1):

                # verify two by two and switch if unordered
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]          

    def insertionsort(self, array):
        for i in range(len(array)):

            # select starting index
            j = i

            # verify with previous items to find those larger than the selected item
            # if the first comparation is smaller, the item is in the correct relative place
            while j > 0 and array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]
                j -= 1
        return array

    def selectionsort(self, array):
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
        return array

    def mergesort(self, array):
        if len(array)>1:
                
            mid = len(array) // 2

            left = array[:mid]
            right = array[mid:]

            self.mergesort(left)
            self.mergesort(right)

            i = j = k = 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1

        return array
    
    

