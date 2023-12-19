"""numbers = [1, 20, 13, 12, [2, 4, 6], 12, 20]
print(numbers[4])"""

# Initialize an empty list to store records
records = []

# Input the number of records
num_records = int(input("Enter the number of records: "))

# Input each record
for i in range(num_records):
    name = input("Enter name: ")
    cgpa = float(input("Enter CGPA: "))

    # Append the record to the 'records' list
    records.append([name, cgpa])

# Print the list of records
print("List of Records:")
for record in records:
    print(record)


