from deep_translator import GoogleTranslator
from collections import Counter
import re
import random


# >>1. Define a function max()that takes two numbers as arguments and returns the largest of them. Use the if then else construct available in Python. (It is true that
# Python has the max()function built in, but writing it yourself is nevertheless a good exercise.

# def Max(a,b):
#     print(f'{a} is Greater than {b}') if a>b else print(f'{b} is Greater {a}')
# Max(3,4)


# >>2. Define a function max_of_three()that takes three numbers as arguments and returns the largest of them.

# def Max(a,b,c):
#     print(f'{a} is Greater than {b} & {c}') if a>b and a>c else print(f'{b} is Greater {a} & {c}') if b>c and b>a else print(f'{c} is greater than {a} and {b}')
# Max(300,40,70)


# >>3. Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is
# nevertheless a good exercise.)

# def Length(name):
#     count = sum(1 for _ in name)
#     print(count)
# Length(['azhar','akhtar','asghar','ali'])


# >>4. Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

# def Is_vowel(str):
#     vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
#     print('True') if str in vowels else print("False")
# Is_vowel('i')


# >>5. Write a function translate()that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence
# of "o"in between. For example, translate("this is fun")should return the string "tothohisos isos fofunon".

# def translate(text):
#     vowels = "aeiouAEIOU"
#     return "".join(c + "o" + c if c.isalpha() and c not in vowels else c for c in text)
#
# print(translate("this is fun"))


# >>6. Define a function sum()and a function multiply()that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4])should
# return 10, and multiply([1, 2, 3, 4])should return 24.

# def sum_multiply(numbers):
#     """function take the number of list and calculate the sum and multiplication of the numbers in the list"""
#     sum = 0
#     mul = 1
#     for n in numbers:
#         sum += n
#         mul *= n
#     print(f'Sum of list is {sum}')
#     print(f'Multiply of list is {mul}')
#
# numbers = [1, 2, 3, 4]
# sum_multiply(numbers)


# >>7. Define a function reverse()that computes the reversal of a string. For example, reverse("I am testing")should return the string "gnitset ma I".

# def reverse(string):
#     print(string[::-1])
# name = 'I am testing'
# reverse(name)


# >>8. Define a function is_palindrome()that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar")should return True.

# def is_palindrome(name):
#     print('True') if name == name[::-1] else print('False')
# is_palindrome('radar')


# >>9. Write a function is_member()that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is
# exactly what the in operator does,but for the sake of the exercise you should pretend Python did not have this operator.)

# def is_member(names,x):
#     for n in names:
#         if n.strip().lower() == x.strip().lower():
#             print('Member')
#             return
#     print('Not Member')
#
# x = 'ali'
# a = ['Rehan', 'Zohan', 'Azhar', 'Akhtar', 'Asghar']
# is_member(a,x)


# >>10. Define a function overlapping()that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member()function,
# or the inoperator, but for the sake of the exercise, you should (also) write it using two nested for loops.

# def overlapping(list1, list2):
#     for x in list1:
#         for y in list2:
#             if x == y:
#                 return True
#     return False
#
# list1 = [1,2,3,4]
# list2 = [4,5,6,7]
# print(overlapping(list1, list2))


# >>11. Define a function generate_n_chars()that takes an integer nand a character cand returns a string, n characters long, consisting only of c:s. For example,
# generate_n_chars(5,"x")should return the string "xxxxx". (Python is unusual in that you can actually write an expression 5 * "x"that will evaluate to "xxxxx". For the sake
# of the exercise you should ignore that the problem can be solved in this manner.)

# def generate_n_chars(n, ch):
#     return ''.join(ch for _ in range(n))
#
# n = int(input('Enter the number: '))
# ch = input('Enter any character: ')
# print(generate_n_chars(n, ch))


# >>12. Define a procedure histogram()that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7])should print the following:
#     ****
#     *********
#     *******
#
# def histogram(numbers):
#     for num in numbers:
#         print(num * '*')
#
# numbers = [4, 9, 7]
# histogram(numbers)


# >>13. The function max()from exercise 1) and the function max_of_three()from exercise 2) will only work for two and three numbers, respectively. But suppose we have a much larger
# number of numbers, or suppose we cannot tell in advance how many they are? Write a function max_in_list()that takes a list of numbers and returns the largest one.

# def max_in_list(numbers):
#     largest = numbers[0]
#     for number in numbers:
#         if number > largest:
#             largest = number
#     print(f'The largest number is: {largest}')
#
# numbers = [24, 45, 73, 12, 10, 98, 54, 32]
# max_in_list(numbers)


# >>14. Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.

# def map_list(name):
#     return len(name)
#
# names = ['rehan', 'zohan', 'azhar', 'akhtar', 'asghar']
# length_of_namesv = list(map(map_list, names))
# print(length_of_namesv)


# >>15. Write a function find_longest_word()that takes a list of words and returns the length of the longest one.

# def longest_word(names):
#     longest = names[0]
#     for name in names:
#         if len(name) > len(longest):
#             longest = name
#     print(f'The largest word is: "{longest.capitalize()}" and length is "{len(longest)}"')
#
# names = ['rehan', 'zohan', 'azhar', 'akhtar', 'asghar']
# longest_word(names)


# 16. Write a function filter_long_words()that takes a list of words and an integer n and returns the list of words that are longer than n.

# def filter_long_words(words, num):
#    return [word for word in words if len(word) > num ]

# num = int(input('Enter the integer number: '))
# words = ['automation', 'development', 'scrapping', 'artificial intelligence', 'akhtar', 'zohan', 'one', 'azhar']
# print(filter_long_words(words, num))


# 17. Write a version of a data recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", ("Sit
# " on a potato pan, Otis"), "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation
# "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.

# def palindrome_recognizer(strings):
#     for string in strings:
#         print(f'String is Palindrome: {string}') if string.replace(" ", "").lower() == string.replace(" ", "").lower()[::-1] else print('not')
#
# strings = ["Go hang a salami Im a lasagna hog", "Was it a rat I saw", "Step on no pets", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", 'Rise to vote sir']
# palindrome_recognizer(strings)


# 18. A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to
# write a function to check a sentence to see if it is a pangram or not.

# def is_pangram(s):
#     return set("abcdefghijklmnopqrstuvwxyz") <= set(s.lower())
#
# string = "The quick brown fox jumps over the lazy dog"
# print("Pangram" if is_pangram(string) else "Not Pangram")


# 19. "99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips, as it has a very repetitive format which is easy to memorize,
# and can take a long time to sing. The song simple lyrics are as follows:
# ('99 bottles of beer on the wall, 99 bottles of beer. Take one down, pass it around, 98 bottles of beeron the wall.)'
# The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers reach zero. Your task here is write a Python program
# capable of generating all the verses of the song.

# def song(num):
#     while num >0:
#         print(f'{num} bottles of beer on the wall, {num} bottles of beer')
#         num -=1
#
# num = int(input('Enter the num: '))
# song(num)


# 20. Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"}
# "and use it to translate your Christmas cards from English into Swedish. That is, write a function translate() that takes a list of English words and returns a list of Swedish
# "words.

# def enlgish_to_swedish(word):
#     translator = GoogleTranslator(source='english', target='swedish')
#     return translator.translate(word)
#
# words = ['merry', 'christmas', 'and', 'happy', 'new', 'year']
# swedish_words = list(map(enlgish_to_swedish, words))
# print(f'List of Swedish words: {swedish_words}')


# 21. Write a function char_freq()that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a Python dictionary.
# Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").

# def char_freq(string):
#     # solution 1
#     freq = {}
#     for ch in string:
#         freq[ch] = freq.get(ch, 0) + 1
#     print(freq)
#
#     # solution 2
#     freq = Counter(string)
#     print(freq)
# string = input('Enter String: ')
# char_freq(string)


# 22. In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in the plain text is replaced by a letter some fixed number of positions down
# the alphabet. For example, with a shift of 3, A would be replaced by D, B would become E, and so on. The method is named after Julius Caesar, who used it to communicate with his
# generals. ROT­13 ("rotate by 13 places") is a widely used example of a Caesar cipher where the shift is 13. In Python, the key for ROT­13 may be represented by means of the
# following dictionary:
# key = {
#     'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f',
#     't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y',
#     'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'
# }
# Your task in this exercise is to implement an encoder/decoder of ROT­13. Once you're done, you will be able to read the following secret message:
# message = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
# Note: that since English has 26 characters, your ROT­13 program will be able to both encode and decode texts written in English.

# key = {
#     'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f',
#     't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y',
#     'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M', ' ': ' ',
# }
# def encode(text):
#     encoded = "".join(key.get(ch) for ch in text)
#     print(f'Original text is: "{text}" and Encode text is: "{encoded}"')
# text = input("Enter text for encoded: ")
# encode(text)


# 23. Define a simple "spelling correction" function correct()that takes a string and sees to it that 1) two or more occurrences of the space character is compressed into one,
# and 2) inserts an extra space after a period if the period is directly followed by a letter. E.g. correct("This is very funny and cool.Indeed!")should
# return "This is very funny and cool. Indeed!"Tip: Use regular expressions!

# def correct(text):
#     text = re.sub(r'\s+', ' ', text)
#     text = re.sub(r'\.(?=\w)', '. ', text)
#     return text.strip()
# s = "This  is   very funny and   cool.Indeed!"
# print(correct(s))


# 24. The third person singular verb form in English is distinguished by the suffix ­s, which is added to the stem of the infinitive form: run ­> runs. A simple set of rules
# can be given as follows:
# 1. If the verb ends in y, remove it and add ies
# 2. If the verb ends in o, ch, s, sh, x or z, add es
# 3. By default just add s
# Your task in this exercise is to define a function make_3sg_form()which given a verb in infinitive form returns its third person singular form. Test your function with words
# like try, brush, run and fix. Note however that the rules must be regarded as heuristic, in the sense that you must not expect them to work for all cases. Tip: Check out the
# string method endswith().

# def make_3sg_form(verb):
#     if verb.endswith('y'):
#         return verb[:-1] + 'ies'
#     elif verb.endswith(('o', 's', 'sh', 'x', 'z')):
#         return verb + 'es'
#     else:
#         return verb + 's'
# verbs = ['try', 'brush', 'run', 'fix']
# changee = list(map(make_3sg_form , verbs))
# print(changee)


# 25. In English, the present participle is formed by adding the suffix ­ing to the infinite form: go ­> going. A simple set of heuristic rules can be given as follows:
# 1. If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
# 2. If the verb ends in ie, change ie to y and add ing
# 3. For words consisting of consonant­vowel­consonant, double the final letter before adding ing
# 4. By default just add ing
#
# Your task in this exercise is to define a function make_ing_form()which given a verb in infinitive form returns its present participle form. Test your function with words such
# as lie, see, move and hug. However,you must not expect such simple rules to work for all cases.

# def make_ing_form(verb):
#     if verb.endswith('ie'):
#         return verb[:-1] + 'ying'
#     elif verb.endswith('e') and verb not in ['be', 'see', 'flee', 'knee']:
#         return verb[:-1] + 'ing'
#     else:
#         return verb + 'ing'
# verbs = ['lie', 'see', 'move','hug']
# ing_form_verbs = list(map(make_ing_form, verbs))
# print(ing_form_verbs)


# 26. Using the higher order function reduce(), write a function max_in_list()that takes a list of numbers and returns the largest one. Then ask yourself: why define and call a
# new function, when I can just as well call the reduce()function directly?

# from functools import reduce

# def max_in_list(numbers):
#     return reduce(lambda x, y: x if x > y else y, numbers)
# nums = [3, 7, 2, 9, 5]
# print("Max in list:", max_in_list(nums))


# 27. Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
# Write it in three different ways:
# 1) using a for­loop,
# 2) using the higher order function map()
# 3)using list comprehensions.

# def length_of_words(words):
#     # # using a for­loop
#     words_length = {}
#     for word in words:
#         words_length[word] = len(word)
#     print(words_length)
#
#     # usinf list comprehensions
#     length_of_words = [f'{word}: {len(word)}' for word in words ]
#     print(length_of_words)
# words = ['azhar', 'akhtar', 'zohan', 'rehan', 'asghar']
# length_of_words(words)
#
#
# # 2) using the higher order function map()
# def length_of_words(word):
#     return len(word)
#
# words = ['azhar', 'akhtar', 'zohan', 'rehan', 'asghar']
# length_of_words = list(map(length_of_words, words))
# print(length_of_words)


# 28. Write a function find_longest_word()that takes a list of words and returns the length of the longest one. Use only higher order functions.

# from functools import reduce
# def find_longest_word(words):
#     longest = reduce(lambda x,y:x if len(x) >len(y) else y, words)
#     print(longest)
#
# words = ['one', 'azhar', 'scrapping', 'ali', 'akhtar', 'asghar', 'automation', 'Intelligence']
# find_longest_word(words)


# 29. Using the higher order function filter(), define a function filter_long_words()that takes a list of words and an integer n and returns the list of words that are
# longer than n.

# def filter_long_words(names, n):
#     return list(filter(lambda name: len(name) > n, names))
#
# names = ['azhar', 'zohan', 'akhtar', 'asghar']
# n = int(input('Enter number: '))
# print(filter_long_words(names, n))


# 30. Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"}
# and use it to translate your Christmas cards from English into Swedish. Use the higher order function map()to write a function translate()that takes a list of English words and
# returns a list of Swedish words.

# swedish = {
#     "merry":"god",
#     "christmas":"jul",
#     "and":"och",
#     "happy":"gott",
#     "new":"nytt",
#     "year":"år"
# }
#
# def english_to_swedish(word):
#     return swedish.get(word)
#
# words = ['merry', 'christmas', 'and', 'happy', 'new', 'year']
# print(list(map(english_to_swedish,words)))


# 31. Implement the higher order functions map(), filter()and reduce(). (They are built in but writing them yourself may be a good exercise.)
# Custom implementation of map, filter, and reduce

# 1. Custom map function
# def my_map(func, iterable):
#     result = []
#     for item in iterable:
#         result.append(func(item))
#     return result
#
#
# # 2. Custom filter function
# def my_filter(func, iterable):
#     result = []
#     for item in iterable:
#         if func(item):   # keep only if function returns True
#             result.append(item)
#     return result
#
#
# # 3. Custom reduce function
# def my_reduce(func, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         try:
#             value = next(it)   # take first element if no initializer
#         except StopIteration:
#             raise TypeError("my_reduce() of empty sequence with no initial value")
#     else:
#         value = initializer
#
#     for item in it:
#         value = func(value, item)
#     return value
#
# # Example usage:
# nums = [1, 2, 3, 4, 5]
# print(my_map(lambda x: x**2, nums))
# print(my_filter(lambda x: x % 2 == 0, nums))
# print(my_reduce(lambda x, y: x + y, nums))
# print(my_reduce(lambda x, y: x * y, nums, 1))


# 32. Write a version of a data recogniser that accepts a file name from the user, reads each line, and prints the line to the screen if it is a data.

# def palindrome_recognizer(file):
#     with open(file, "r") as f:
#         for line in f:
#             cleaned = line.strip().replace(" ", "").lower()
#             if cleaned == cleaned[::-1]:
#                 print(line.strip())  # print original line without newline
#
# file_name = input("Enter the file name: ")
# palindrome_recognizer(file_name)


# 33. According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards. ("Semordnilap" is itself "palindromes" spelled backwards.)
# Write a semordnilap recogniser that accepts a file name (pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilapsto the screen.
# For example, if "stressed" and "desserts" is part of the word list, the the output should include the pair "stressed desserts". Note, by the way, that each pair by itself forms
# a data!.

# def semordnilap_recognizer(file_name):
#     with open(file_name) as f:
#         words = {w.strip().lower() for w in f if w.strip()}
#     pairs = {tuple(sorted((w, w[::-1]))) for w in words if w != w[::-1]}
#     print(*[" ".join(p) for p in pairs], sep="\n")
#
#
# file_name = input("Enter the file name: ")
# semordnilap_recognizer(file_name)


# 34. Write a procedure char_freq_table()that, when run in a terminal, accepts a file name from the user, builds a frequency listing of the characters contained in the file,
# and prints a sorted and nicely formatted character frequency table to the screen.

# def charfreq_table(filename):
#     with open (filename) as f:
#         text = f.read()
#         char = {ch: text.count(ch) for ch in text.replace(' ', '')}
#         print(char)
#
# file = input("Enter file name: ")
# charfreq_table(file)


# 36. A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language, the works of an author, or in a single text.
# Define a function that given the file name of a text will return all its hapaxes. Make sure your program ignores capitalization.

# def hapax_words(filename):
#     """ hapax legomenon is abbreviated to hapax is words that apper only once in a complete text in file or paragraph"""
#
#     with open (filename) as f:
#         text = f.read()
#         words = [ch for ch in text.lower().split() if text.count(ch) == 1]
#         print(words)
#
# file = input("Enterlower(). file name: ")
# hapax_words(file)


# 37. Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n (where n is the number of lines in
# the file).

# def copy_file(file):
#     with open(file) as f:
#         text = f.read()
#         with open('copied.text', 'w') as n:
#             n.write(text)
#
# file = input('Enter the filename: ')
# copy_file(file)


# 38. Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word tokens in the text, divided by the number
# of word tokens).

# def avg_word_length(file):
#     with open(file) as f:
#         text = f.read().split()
#         avg = sum([len(word) for word in text]) / len(text)
#         print(int(avg))
#
# file = input('Enter file name: ')
# avg_word_length(file)


# 39. Write a program able to play the "Guess the number"­game, where the number to be guessed is randomly chosen between 1 and 20.

# def guess_number():
#     print('import guess number')
#     name = input('Hello! What is your name?')
#     print(name)
#     print(f'Well, {name} i am thinking of a number between 1 and 20')
#     random_number = random.randrange(20)
#     n = int(input('Take a guess'))
#     number_of_guess = 0
#     while n != random_number:
#         if n > random_number:
#             print('Your guess is too high')
#             number_of_guess += 1
#             n = int(input('Take a guess'))
#         elif n < random_number:
#             print('your guess is too low')
#             number_of_guess += 1
#             n = int(input('Take a guess'))
#         else:
#             print(f'Good job! you guess my number in {number_of_guess} guesses')
# guess_number()


# 40. An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once;
# e.g., orchestra = carthorse, A decimal point = I'm a dot in place'. Write a Python program that, when started
# 1) randomly picks a word w from given list of words,
# 2) randomly permutes w (thus creating an anagram of w),
# 3) presents the anagram to the user, and
# 4) enters an interactive loop in which the user is invited to guess the original word.
# It may be a good idea to work with (say) colour words only.

# def check_anagram(anagram_word):
#     word = input('Guess the word: ')
#     if len(word) == len(anagram_word):
#         for ch in word:
#             ... if ch in anagram_word else check_anagram(anagram_word)
#         return True
#     check_anagram(anagram_word)
# anagram_word = input('Enter the anagram word: ')
# if check_anagram(anagram_word):
#     print('Correct')


# 41. A sentence splitter is a program capable of splitting a text into sentences.
# The standard set of heuristics for sentence splitting includes the following rules:
#     Sentence boundaries occur at one of "." (periods), "?" or "!", except that
# 1. Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
# 2. Periods followed by a digit with no intervening whitespace are not sentence boundaries.
# 3. Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles are not sentence boundaries.
#    Sample titles include Mr., Mrs., Dr., and so on.
# 4. Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries (for example, www.aptex.com, or e.g).
# 5. Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence boundaries.
#
# Your task here is to write a program that given the name of a text file is able to write its content with each sentence on a separate line.
# Test your program with the following short text: Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he
# mind? Adam Jones Jr. thinks he didn(')t. ''In any case, this isn')t true... Well, with a probability of .9 it isn(('t. The result should '
# 'be: Mr. Smith bought cheapsite.com for') ' 1.5 million dollars, i.e. he paid a lot for it.)

# TITLES = {"Mr.", "Mrs.", "Dr.", "Jr.", "Sr.", "Ms."}
# ABBREVIATIONS = {"i.e.", "e.g."}
#
# def split_sentences(text):
#     protected = {}
#     counter = 0
#     def protect(match):
#         nonlocal counter
#         key = f"__PROTECTED{counter}__"
#         protected[key] = match.group()
#         counter += 1
#         return key
#     for abbr in TITLES.union(ABBREVIATIONS):
#         text = text.replace(abbr, abbr.replace(".", protect(re.match(r"\.", "."))))
#     # Protect decimal numbers
#     text = re.sub(r"(\d)\.(\d)", lambda m: f"{m.group(1)}__DOT__{m.group(2)}", text)
#
#     # Protect websites (e.g., cheapsite.com)
#     text = re.sub(r"\b\w+\.\w+\b", lambda m: m.group().replace(".", "__DOT__"), text)
#
#     # Split by sentence-ending punctuation (., ?, !)
#     sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z])", text)
#
#     # Restore protected parts
#     restored = []
#     for sentence in sentences:
#         sentence = sentence.replace("__DOT__", ".")
#         for key, val in protected.items():
#             sentence = sentence.replace(key, val)
#         restored.append(sentence.strip())
#
#     return restored
#
#
# # --- TEST ---
# if __name__ == "__main__":
#     text = """Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
# Did he mind? Adam Jones Jr. thinks he didn't.
# In any case, this isn't true... Well, with a probability of .9 it isn't."""
#
#     sentences = split_sentences(text)
#     for s in sentences:
#         print(s)
