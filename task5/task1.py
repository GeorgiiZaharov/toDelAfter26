words = ["apple","pen"]
def rec(word):
    if not word: return True
    good_words = list(filter(lambda x: word.startswith(x), words))
    if not good_words: return False
    return any([rec(word[len(good_word):]) for good_word in good_words])
print(rec("applepen"))