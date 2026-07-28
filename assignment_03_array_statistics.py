# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================



def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
        total = calculate_sum(numbers)
        return total / len(numbers)
def find_maximum(numbers):
    highest =numbers[0]
    for num in numbers:
        if num > highest:
         highest = num
    return highest
def find_minimum(numbers):
            lowest = numbers[0]
            for num in numbers:
              if num < lowest:
               lowest = num
            return lowest

def main():
    count = int(input("How many numbers? "))
    if count <= 0:
        print("Error: please enter a positive integer. ")
        return
    numbers = []
    for i in range (1, count + 1):
        num = float(input(f"Enter a number {i}: "))
        if num.is_integer() :
            num = int(num)
        numbers.append(num)


        print("\nResults:")
        print("Sum:     ", calculate_sum(numbers))
        print("Average: ", calculate_average(numbers))
        print("Maximum: ", find_maximum(numbers))
        print("Minimum: ", find_minimum(numbers))

    if __name__ == "__main__":
        main()





