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
        Args:
            method (str, optional): The method to sort the array with. Defaults to "bubble".

        Raises:
            ValueError: If the array contains only one or less element.
            ValueError: If the array contains None values.
            ValueError: If the specified method is invalid.
        """
        # If the array contains only one or less element, raise an error
        if self.length <= 1:
            raise ValueError("Array contains only one or less element")

        if None in self.array:
            raise ValueError("Array contains None values")

        if method not in ["bubble", "selection", "insertion", "merge", "quick", "heap"]:
            raise ValueError("Invalid sorting method")

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

    def _bubble_sort(self):
        """
            Helper function to sort the array using bubble sort.
        This is a private method and is not intended to be used directly.

        Time Complexity:
            - Best Case: O(n) when array is already sorted
            - Worst Case: O(n^2) when array is reverse sorted
            - Average Case: O(n^2)
        Space Complexity: O(1) as sorting is done in-place

        Algorithm:
        1. Compare adjacent elements and swap if they are in wrong order
        2. After each pass, the largest unsorted element "bubbles up" to its correct position
        3. Optimization: If no swaps occur in a pass, array is sorted

        Characteristics:
        - Not stable (may change relative order of equal elements)
        - In-place sorting (O(1) space)
        - Performs O(n^2) comparisons and O(n^2) swaps in the worst case

        Example:
            Initial: [5, 3, 8, 4, 2]
            Pass 1:  [3, 5, 4, 2, 8]
            Pass 2:  [3, 4, 2, 5, 8]
            Pass 3:  [3, 2, 4, 5, 8]
            Pass 4:  [2, 3, 4, 5, 8]
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

            # If no swaps occurred in this pass, array is sorted
            if not swapped:
                break

    def _selection_sort(self):
        """
            Helper function to sort the array using selection sort.
        This is a private method and is not intended to be used directly.

        Time Complexity:
            - Best Case: O(n^2)
            - Worst Case: O(n^2)
            - Average Case: O(n^2)
        Space Complexity: O(1) as sorting is done in-place

        Algorithm:
        1. Divide array into sorted and unsorted parts
        2. Find minimum element in unsorted part
        3. Swap it with first element of unsorted part
        4. Move boundary between sorted and unsorted parts one element to the right
        5. Repeat until array is sorted

        Characteristics:
        - Always performs O(n) swaps
        - Not stable (may change relative order of equal elements)
        - Performs well on small arrays
        - Less efficient than insertion sort for nearly sorted arrays

        Example:
            Initial: [64, 25, 12, 22, 11]
            Pass 1:  [11, 25, 12, 22, 64]  # 11 is minimum, swap with 64
            Pass 2:  [11, 12, 25, 22, 64]  # 12 is minimum, swap with 25
            Pass 3:  [11, 12, 22, 25, 64]  # 22 is minimum, swap with 25
            Pass 4:  [11, 12, 22, 25, 64]  # 25 is minimum, no swap needed
        """
        for i in range(self.length - 1):
            # Keep track of the index of the minimum element
            min_index = i

            # Iterate through the array to find the minimum element
            for j in range(i + 1, self.length):
                # If the next element is smaller than the current element, update the index of the minimum element
                if self.array[j] < self.array[min_index]:
                    min_index = j

            # Swap the minimum element with the first element of unsorted part
            # Only swap if the minimum element is not already in its correct position
            if min_index != i:
                self.array[i], self.array[min_index] = (
                    self.array[min_index],
                    self.array[i],
                )

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
