def repeated_word(string):
    clean_string = ''.join(c.lower() if c.isalpha() else ' ' for c in string)
    
    words = clean_string.split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            return word
        else:
            word_count[word] = 1
    
    return None


def word_count(string):
    clean_string = ''.join(c.lower() if c.isalpha() else ' ' for c in string)
    
    words = clean_string.split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count


def most_frequent_words(string):
    clean_string = ''.join(c.lower() if c.isalpha() else ' ' for c in string)
    
    words = clean_string.split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    max_count = max(word_count.values())
    most_frequent = [word for word, count in word_count.items() if count == max_count]
    
    return most_frequent

