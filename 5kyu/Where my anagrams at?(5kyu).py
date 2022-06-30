def anagrams(word, words):
    return [i for i in words if sorted(word) == sorted(i)]