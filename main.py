class FlattenArrayPython:
    @staticmethod
    def flatten(iterable):
        flattened_list = []
        for item in iterable:
            if isinstance(item, list):
                flattened_list.extend(FlattenArrayPython.flatten(item))
            elif item is not None:
                flattened_list.append(item)
        return flattened_list


# Testiranje implementacije
input_list = [1, [2, 3, 4, 5, 6, 7], 8]
expected_output = [1, 2, 3, 4, 5, 6, 7, 8]
assert FlattenArrayPython.flatten(input_list) == expected_output, "Test case 1 failed"

input_list = [0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]
expected_output = [0, 2, 2, 3, 8, 100, 4, 50, -2]
assert FlattenArrayPython.flatten(input_list) == expected_output, "Test case 2 failed"

input_list = [1, 2, None]
expected_output = [1, 2]
assert FlattenArrayPython.flatten(input_list) == expected_output, "Test case 3 failed"

input_list = []
expected_output = []
assert FlattenArrayPython.flatten(input_list) == expected_output, "Test case 4 failed"

print("All test cases pass")
