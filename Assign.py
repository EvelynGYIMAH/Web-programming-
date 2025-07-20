def print_multiplication_table(size=12):
    # Print header row
    print("    ", end="")
    for i in range(1, size + 1):
        print(f"{i:4}", end="")
    print("\n" + "-" * (size * 4 + 4))

    # Print table rows
    for row in range(1, size + 1):
        print(f"{row:2} |", end="")  # Row header
        for col in range(1, size + 1):
            print(f"{row * col:4}", end="")
        print()

# Run the function
print_multiplication_table()
