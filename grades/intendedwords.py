intendedWords = {
    "cs": "cmp_sc",
    "fall": "fs",
    "spring": "sp",
    "winter": "ws",
    "summer": "ss"
}

def getIntendedWord(criteria):
    for word in intendedWords:
        if criteria == word:
            return intendedWords[word]
    return criteria.lower()