def are_anagrams(word1, word2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Check if the sorted versions of the words are the same
    return sorted(word1) == sorted(word2)

# Input two words from the user
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# Check if the words are anagrams and display the result
if are_anagrams(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")
    