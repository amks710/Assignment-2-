#Arham Mehdi
#Assignment 2
#Merge sort with sound and showing every step
import time
import winsound

# Function to merge the two sorted arrays
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Creating the temporary arrays
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]

    i = j = 0
    k = left

    # Merging the temporary arrays back into arr[l:r+1]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            # Playing swap sound effect beep beep
            winsound.Beep(500, 100)
        k += 1

    # Copying the remaining elements of L[] if any at all
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copying the remaining elements of R[] if any left
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    # Printing the current state of the array after merging
    print("Merged Array:", arr)

# Function to perform Merge Sort
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        # Recursive calls to split the array
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # Merge the sorted halves
        merge(arr, left, mid, right)

# Function to print the array
def print_array(arr):
    print("Sorted Array:", arr)

# Main function
def main():
    # Input the array
    arr = list(map(int, input("Please enter your space separated array : ").split()))

    print("Sorting array using Merge Sort...")
    print("Initial Array:", arr)

    merge_sort(arr, 0, len(arr) - 1)

    # Printing the sorted array
    print_array(arr)

if __name__ == "__main__":
    main()
