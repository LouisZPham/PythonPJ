from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()

words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))

#Another one without using defaultdict

def group_anagrams2(b):
    anagram_dict = {}
    for word in b:
        sorted_word = tuple(sorted(word))
        # If the sorted word is already a key in the dictionary, append the original word to its list of anagrams
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        # Otherwise, create a new key for the sorted word and set its value to a list containing the original word
        else:
            anagram_dict[sorted_word] = [word]
    return list(anagram_dict.values())

listofwords = ["men", "nem","rat", "tar", "tra"]
print(group_anagrams2(listofwords))