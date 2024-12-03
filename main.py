def find_missing_keys(english, swedish):
    english_keys = set(english.keys())
    swedish_keys = set(swedish.keys())
    missing_keys = english_keys - swedish_keys
    return missing_keys

english = {
    # add english translation    
}


swedish = {
    # add swedish translation
}

missing_keys = find_missing_keys(english, swedish)
print(missing_keys)