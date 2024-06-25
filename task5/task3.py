def findAllConcatenatedWords(words): # идея делить слова на части не равные самому слову
    wordSet = set(words)
    def isConcatenated(word):
        return any(word[:i] in wordSet and (word[i:] in wordSet or isConcatenated(word[i:])) 
                   for i in range(1, len(word)-1))

    return list(filter(isConcatenated, words))

words1 = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
print(findAllConcatenatedWords(words1))
