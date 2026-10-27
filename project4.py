data = []

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def data_summary():
    if not data:
        print("Please input data first!")
        return
    print("\nData Summary:")
    print("Total elements:", len(data))
    print("Minimum value:", min(data))
    print("Maximum value:", max(data))
    print("Sum of all values:", sum(data))
    print("Average value:", round(sum(data) / len(data), 2))
    
def filter_data():
    if not data:
        print("Please input data first!")
        return

    threshold = int(input("Enter threshold value: "))
    result = list(filter(lambda x: x >= threshold, data))
    print("Filtered Data:", result)



def dataset_statistics():
    if not data:
        print("Please input data first!")
        return

    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = round(total / len(data), 2)

    print("\nDataset Statistics:")
    print("Minimum value:", minimum)
    print("Maximum value:", maximum)
    print("Sum of all values:", total)
    print("Average value:", average)



print("Welcome to the Data Analyzer and Transformer Program")

while True:
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")

    choice = input("Please enter your choice: ")

    if choice == "1":
        data = list(map(int, input(
            "Enter data separated by spaces: "
        ).split()))
        print("Data has been stored successfully!")

    elif choice == "2":
        data_summary()

    elif choice == "3":
        n = int(input("Enter a number to calculate its factorial: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print("Factorial of", n, "is:", factorial(n))

    elif choice == "4":
        filter_data()

    elif choice == "5":
        if not data:
            print("Please input data first!")
        else:
            print("1. Ascending")
            print("2. Descending")
            order = input("Enter your choice: ")

            if order == "1":
                print("Sorted Data in Ascending Order:")
                print(sorted(data))
            elif order == "2":
                print("Sorted Data in Descending Order:")
                print(sorted(data, reverse=True))
            else:
                print("Invalid sorting choice!")

    elif choice == "6":
        dataset_statistics()

    elif choice == "7":
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
