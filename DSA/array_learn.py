class ArrayLearn:
    def __init__(self, initial_values=None):
        self.array = []
        self.length = 0

        if initial_values is not None:
            for value in initial_values:
                self.insert(value)

    def insert(self, value, index=None):
        """
        Manually insert a value into the array at specified index.
        If index is not provided, append to the end.

        Args:
            value (_type_): The value to insert.
            index (_type_, optional): The index to insert the value at. Defaults to None.

        Raises:
            IndexError: If index is out of bounds.
        """
        if index is None:
            self.array[self.length] = value
        else:
            if index < 0 or index > self.length:
                raise IndexError("Index out of bounds")

            # Shift elements to the right to make space for the new value
            # For example, if the array is [1, 2, 3, 5, 6] and we want to insert 4 at index 3,
            # given the array length is 5, and the index for 6 is 4,
            # we are able to use the length as the index for 6, and shift the elements to the right
            # until we reach the index 3, where we want to insert 4.
            # As a result, the array will become [1, 2, 3, 4, 5, 6]
            for i in range(self.length, index, -1):
                # Shift the elements to the right
                self.array[i] = self.array[i - 1]

            # Insert the new value at the specified index
            self.array[index] = value

        # Increment the length of the array
        self.length += 1

    def delete(self, index):
        """
        Manually delete a value from the array at specified index.

        Args:
            index (int): The index to delete the value at.

        Raises:
            IndexError: If index is out of bounds.
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")

        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]

        self.length -= 1

    def sort(self, method="bubble"):
        """
        Sort the array using the specified method.
        Methods available:
            - bubble
            - selection
            - insertion
            - merge
            - quick
            - heap
        TODO: A check for edge cases, such as when the array contains None values.
        Args:
            method (str, optional): The method to sort the array with. Defaults to "bubble".
        """
        # If the array contains only one or less element, raise an error
        if self.length <= 1:
            raise ValueError("Array contains only one or less element")

        # Sort the array using the specified method
        if method == "bubble":
            self._bubble_sort()
        elif method == "selection":
            self._selection_sort()
        elif method == "insertion":
            self._insertion_sort()
        elif method == "merge":
            self._merge_sort()
        elif method == "quick":
            self._quick_sort()
        elif method == "heap":
            self._heap_sort()
        else:
            raise ValueError("Invalid sorting method")

    def _bubble_sort(self):
        """
        Helper function to sort the array using bubble sort.
        This is a private method and is not intended to be used directly.

        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Bubble sort works by:
        - Iterating through the array
        - Comparing each element with the next element
        - Swapping the elements if the next element is smaller than the current element
        - Repeating the process until the array is sorted
        """
        for i in range(self.length - 1):
            # Flag to check if the array is sorted
            swapped = False
            for j in range(self.length - i - 1):
                # If the next element is smaller than the current element, swap the elements
                if self.array[j + 1] < self.array[j]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]

                    # Set the flag to True as the array is not sorted
                    swapped = True

            # If the array is sorted, break the loop as the array is already sorted
            if not swapped:
                break

    def _selection_sort(self):
        """
        Helper function to sort the array using selection sort.
        This is a private method and is not intended to be used directly.

        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Selection sort works by:
        - Iterating through the array
        - Finding the minimum element in the array
        - Swapping the minimum element with the first element
        - Repeating the process until the array is sorted
        """
        for i in range(self.length - 1):
            # Keep track of the index of the minimum element
            min_index = i

            # Iterate through the array to find the minimum element
            for j in range(i + 1, self.length):
                # If the next element is smaller than the current element, update the index of the minimum element
                if self.array[j] < self.array[min_index]:
                    min_index = j

            # Swap the minimum element with the first element
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]

    def _insertion_sort(self):
        """
        Helper function to sort the array using insertion sort.
        """
        pass

    def _merge_sort(self):
        """
        Helper function to sort the array using merge sort.
        """
        pass

    def _quick_sort(self):
        """
        Helper function to sort the array using quick sort.
        """
        pass

    def _heap_sort(self):
        """
        Helper function to sort the array using heap sort.
        """
        pass

    def get_index(self, value=any):
        """
        Manually get the index of a value in the array using linear search.

        Args:
            value (any): The value to get the index of.
        """
        for i in range(self.length):
            if self.array[i] == value:
                return i

        return -1
