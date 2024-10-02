from wordscore import score_word

def run_scrabble(tiles):
    """
    This function reads a file of words and returns a list of valid words
    that can be made from the letters in the input word.

    @param word: a string of letters
    @return: a list of valid words
    """

    # check if input is a string
    if not isinstance(tiles, str):
        return "Input must be a string"
    
    tiles = tiles.upper()

    # get frequency of each char in word
    char_freqs = {}
    for char in tiles:
        if char not in char_freqs:
            char_freqs[char] = 0
        char_freqs[char] += 1

    # check if input is between 2 and 7 characters long
    if len(tiles) < 2 or len(tiles) > 7:
        return "Input must be between 2 and 7 characters long"
    
    # check if input is all letters
    for char in char_freqs:
        if not char.isalpha() and char not in ["*", "?"]:
            return "Input must be all letters"
    
    if char_freqs.get("*", 0) + char_freqs.get("?", 0) > 2:
        return "Input must have at most 2 wildcards"
    
    #open file and read in data
    with open("sowpods.txt","r") as infile:
        raw_input = infile.readlines()
        data = [datum.strip('\n') for datum in raw_input] 
    
    # convert data to a dictionary of words with first letter as key
    data_dict = {}
    for word in data:
        if word[0] not in data_dict:
            data_dict[word[0]] = []
        data_dict[word[0]].append(word)

    # # get all possible scrabble words from input word
    valid_words = set()
    for char in char_freqs:
        if char in data_dict or char in ["*", "?"]:
            dataset = data_dict[char] if char in data_dict else data
            for word in dataset:
                if len(word) <= len(tiles):
                    word_freqs = {}
                    for char in word:
                        if char not in word_freqs:
                            word_freqs[char] = 0
                        word_freqs[char] += 1
                    
                    wildcard_count = char_freqs.get("*", 0) + char_freqs.get("?", 0)
                    valid = True
                    
                    for char in word_freqs:
                        difference = word_freqs[char] - char_freqs.get(char, 0)
                        if difference > 0 + wildcard_count:
                            valid = False
                            break
                        
                        if difference > 0:
                            wildcard_count -= word_freqs[char] - char_freqs.get(char, 0)
                            # word = word.replace(char, "*", difference)
                            word = word.replace(char, char.lower(), difference)

                    if valid:
                        valid_words.add(word)
                


    # create tuple of positive scores and valid words sorted by max score then alphabetically
    # word_scores = [(score_word(word), word) for word in valid_words]
    # word_scores.sort(key = lambda x: (-x[0], x[1]))
    # valid_words = (word_scores, len(word_scores))
    valid_words = [score_word(word) for word in valid_words]
    valid_words.sort(key = lambda x: (-x[0], x[1]))

    return (valid_words, len(valid_words))