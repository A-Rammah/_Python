# -*- coding: utf-8 -*-
"""lab2-4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1H-Vb8p6gGFtM9bFgydnTaHSvGEi7KjBb

**Write a Python function that encodes a string based on the following rules:**
1. Replace each character in the string with its position in the English alphabet (e.g., a -> 1, b -> 2, ..., z -> 26).
2. If the character is uppercase, double its position (e.g., A -> 2, B -> 4, ..., Z -> 52).
3. Non-alphabetic characters (such as digits, spaces, punctuation) should be ignored in the output.
4. Return the encoded string where each number is separated by a hyphen (-).

**Constraints:**
- The input string will only contain printable characters.
- The function must handle both lowercase and uppercase characters.
- You are not allowed to use any Python built-in libraries (e.g., ord, chr) or imported modules.

**Output:**
A dictionary with letters as keys and their frequencies as values, sorted by frequency in descending order.

**Input Format:**
A single string containing any printable characters.

**Output Format:**
A single string containing the encoded values of the characters, separated by hyphens.
"""

sentence = input("Please enter your sentence!")

def encode_sentence(sentence):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    char_list = []
    # input: abceeABCeE

    for char in sentence:
        if char.isprintable() and char.isalpha():
            idx = 0
            while idx < len(alphabet):
                if char.islower() and char == alphabet[idx]:
                    encoded_char = str(alphabet.index(char) + 1)
                    char_list.append(encoded_char)
                    break
                elif char.isupper() and char.lower() == alphabet[idx]:
                    encoded_char = str((alphabet.index(char.lower())+1) * 2)
                    char_list.append(encoded_char)
                    break
                idx += 1
    encoded_char_list = "-".join(char_list)
    print(encoded_char_list)

encode_sentence(sentence)