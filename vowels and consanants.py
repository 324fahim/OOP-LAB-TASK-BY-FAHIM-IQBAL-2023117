# Define a function to count vowels and consonants in a word
def count_vowels_consonants(word):
  # Initialize the vowel and consonant counts to zero
  vowel_count = 0
  consonant_count = 0
  # Convert the word to lower case
  word = word.lower()
  # Loop through each character in the word
  for char in word:
    # Check if the character is a vowel
    if char in "aeiou":
      # Increment the vowel count
      vowel_count += 1
    # Check if the character is a consonant
    elif char.isalpha():
      # Increment the consonant count
      consonant_count += 1
  # Return the vowel and consonant counts as a tuple
  return (vowel_count, consonant_count)

# Ask the user to enter a word
word = input("Enter a word: ")
# Call the function and store the result
result = count_vowels_consonants(word)
# Print the result
print(f"The word {word} has {result[0]} vowels and {result[1]} consonants.")