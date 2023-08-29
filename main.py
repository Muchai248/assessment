# Stacks

def is_balanced(expression):
    stack = []
    for char in expression:
        if char in "{[(":
            stack.append(char)
        elif char in "}])":
            if not stack:
                return False
            if char == "}" and stack[-1] == "{":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == ")" and stack[-1] == "(":
                stack.pop()
            else:
                return False
    return not stack


def remove_duplicates(sequence):
    unique_elements = set(sequence)
    return list(unique_elements),

def word_frequency(sentence):
    words = sentence.lower().split()
    word_frequency = {}
    for word in words:
        if word not in word_frequency:
            word_frequency[word]+=1
        else:
            word_frequency[word]=0 

        return word_frequency

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1)) 
print(is_balanced(expression2))