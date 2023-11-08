# Define a recursive function to divide two numbers without using the division operator
def divide(dividend, divisor):
  # Base case: if the dividend is smaller than the divisor, return (0, dividend) as the quotient and remainder
  if dividend < divisor:
    return (0, dividend)
  # Recursive case: divide the dividend by the divisor by subtracting the divisor from the dividend
  # and incrementing the quotient by 1
  else:
    # Call the function with the updated dividend and divisor
    quotient, remainder = divide(dividend - divisor, divisor)
    # Return the quotient and remainder as a tuple
    return (quotient + 1, remainder)