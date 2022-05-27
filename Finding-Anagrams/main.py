# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if sorted(word) == sorted(anagram):
        return True
    else:
        return False

first_word = input('Enter a word: ')
second_word = input('Enter it\'s anagram: ')
print(find_anagram(first_word, second_word))