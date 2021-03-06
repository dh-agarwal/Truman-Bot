intendedWords = {
    "fall": "fs",
    "spring": "sp",
    "winter": "ws",
    "summer": "ss",
    "cs": "cmp_sc",
    "dsgn": "design",
    "stats": "stat",
    "statistics": "stat",
    "philosophy": "phil",
    "nursing": "nurse",
    "management": "mangmt",
    "journalism": "journ",
    "history": "hist",
    "finance": "financ",
    "english": "englsh",
    "economics": "econom",
    "econ": "econom",
    "com": "commun",
    "comm": "commun",
    "communications": "commun",
    "communication": "commun",
    "chemistry": "chem",
    "accounting": "acctcy",
    "animal": "an_sci",
    "astronomy": "astron",
    "biochem": "biochm",
    "it": "infotc",
    "datascience": "data_sci",
    "data_science": "data_sci",
    "engineering": "enginr",
    "engineer": "enginr",
    "geology": "geog",
    "honors": "gn_hon",
    "general_honors": "gn_hon",
    "healthscience": "hlth_sci",
    "italian": "ital",
    "spanish": "span",
    "theatre": "theatr",
    "anthropology": "anthro",
    "sociology": "sociol",
    "management": "mangmt",
    "marketing": "mrktng",
    "nursing": "nurse",
    "psychology": "psych",
    "physics": "phys",
}

def getIntendedWord(criteria):
    for word in intendedWords:
        if criteria == word:
            return intendedWords[word]
    return criteria.lower()