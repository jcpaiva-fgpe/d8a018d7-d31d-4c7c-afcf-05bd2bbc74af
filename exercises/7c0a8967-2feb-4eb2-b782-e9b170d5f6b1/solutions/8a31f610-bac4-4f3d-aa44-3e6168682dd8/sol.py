import ast

def sort_numbers(arr):
    # Implement Bubble Sort or another sorting algorithm here
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
    return arr

if __name__ == "__main__":
    arr = ast.literal_eval(input())
    sorted_arr = sort_numbers(arr)
    print(sorted_arr)