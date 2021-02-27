
"""
Maksim Semchuk
CS 350 - Homework 7
"""


def max(x, y):
    if x > y:
        return x
    return y


# Brute force implimentation:
def BruteForceLCS(string_One, string_Two, string_One_Length, string_Two_Length):
    if (string_One_Length == 0 or string_Two_Length == 0):
        return ''
    elif (string_One[string_One_Length - 1] == string_Two[string_Two_Length - 1]):
        return string_One[string_One_Length - 1] + BruteForceLCS(string_One[: - 1], string_Two[:-1], string_One_Length - 1, string_Two_Length - 1)
    else:
        return max(BruteForceLCS(string_One, string_Two, string_One_Length - 1, string_Two_Length), BruteForceLCS(string_One, string_Two, string_One_Length, string_Two_Length - 1))


def DynamicProgrammingLCS(string_One, string_Two, string_One_Length, string_Two_Length):
    storage_Array = [[0]*(string_Two_Length+1)]*(first_string_length+1)
    for i in range(string_One_Length + 1):
        for j in range(string_Two_Length + 1):
            if i == 0 or j == 0:
                storage_Array[i][j] = 0
            elif string_One[i-1] == string_Two[j-1]:
                storage_Array[i][j] = storage_Array[i-1][j-1] + 1
            else:
                storage_Array[i][j] = max(storage_Array[i-1][j], storage_Array[i][j-1])
    return storage_Array


def PrintArrayDifferences(storage_Array: list, first_string, second_string, i, j):
    if i >= 0 and j >= 0 and first_string[i] == second_string[j]:
        PrintArrayDifferences(storage_Array, first_string, second_string, i-1, j - 1)
        print(" " + first_string[i])
    elif (j > 0 and (i == 0 or (storage_Array[i][j - 1] >= storage_Array[i-1][j]))):
        PrintArrayDifferences(storage_Array, first_string, second_string, i, j-1)
        print("+" + second_string[j])
    elif i > 0 and (j == 0 or storage_Array[i][j - 1] < storage_Array[i - 1][j]):
        PrintArrayDifferences(storage_Array, first_string, second_string, i-1, j)
        # print("- " + first_string[i])
    else:
        print("")


if __name__ == "__main__":
    first_string = 'abcde'
    second_string = 'cd'
    first_string_length = len(first_string)
    second_string_length = len(second_string)
    print("Length of first string is: ", first_string_length)
    print("Length of second string is: ", second_string_length)
    result_one = BruteForceLCS(first_string, second_string, first_string_length, second_string_length)
    result_one = ''.join(reversed(result_one))
    print("Brute Force LCS: ", result_one)
    result_two = DynamicProgrammingLCS(first_string, second_string, first_string_length, second_string_length)

    print("Dynamic LCS: ")
    PrintArrayDifferences(result_two, first_string, second_string, first_string_length - 1, second_string_length - 1)
