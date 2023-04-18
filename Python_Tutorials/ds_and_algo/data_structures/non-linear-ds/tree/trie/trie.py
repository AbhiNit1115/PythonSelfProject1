# A trie is a tree based structure that organizes information in a hierarchy.
# Properties: Its typically used to store or search strings in a time and space efficient way.
# Any node in trie can store non-repetitive multiple characters
# Every node stores link of the next character of the string.
# Every node keeps track of end of string.
# Trie is used to solve spelling checker and auto-suggestion.

class TrieNode:

    def __init__(self):
        self.children = {}
        self.end_of_string = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
