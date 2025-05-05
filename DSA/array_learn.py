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
