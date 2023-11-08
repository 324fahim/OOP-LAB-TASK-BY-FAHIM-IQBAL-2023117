# Ask the user for the number of rows in the triangle
rows = int(input("Enter the number of rows: "))

# Use a for loop to iterate over the rows
for i in range(1, rows + 1):
  # Print i asterisks in each row
  print("*" * i)