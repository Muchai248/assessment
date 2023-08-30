import string
# Stacks
def is_balanced(expression):
    stack = []
    open_brackets = "([{"
    closed_brackets = ")]}"

    for char in expression:
        if char in open_brackets:
            stack.append(char)
        elif char in closed_brackets:
            if not stack:
                return False
            if open_brackets.index(stack.pop()) != closed_brackets.index(char):
                return False

    return len(stack) == 0

expression2 = "([)]"
expression1 = "({}[])"

print(is_balanced(expression1)) 
print(is_balanced(expression2))  
 

def remove_duplicates(sequence):
    got = set()
    total = []

    for item in sequence:
        if item not in got:
            total.append(item)
            got.add(item)

    return total

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
total = remove_duplicates(input_sequence)
print(total) 


def word_frequency(sentence):
    words = sentence.lower().split()
    word_freq = {}

    for word in words:
        word = word.strip(string.punctuation)
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)