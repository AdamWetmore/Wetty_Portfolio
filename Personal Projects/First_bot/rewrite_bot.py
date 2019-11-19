import random as rd



def file_length(fname):
    file = open(fname)
    file_length = len(file.read().split('.')) - 1
    file.close()
    return file_length



def first_words(fname):

    
    first_words_list = []
    file = open(fname)
    sent_list = file.read().replace('\n','').split('.')
    #removes newline characters and spaces and makes a list where each
    #element is a sentence

    
    for sent in range(len(sent_list)):
        sent_list[sent] = sent_list[sent].split(' ')
        first_words_list.append(sent_list[sent][0])
    file.close()
    first_words_list.remove('')
    #removes null strings from list

    
    return first_words_list




def next_words(fname):

    
    file = open(fname)
    sentence_count = 0
    next_word_dict = {}
    word_list = file.read().replace('\n','').replace('.','. ').split(' ')
    file.close()
    # Creates an ordered list of all words and periods in the file
    

    for word in range(len(word_list)):
        if word_list[word] != '.':
            next_word_dict[word_list[word]] = 0
    next_word_dict_copy = next_word_dict.copy()
    # Creates a dictionary of where the keys are every word in the file excluding periods
    
    
    for key in next_word_dict_copy:
        nexts_list = []
        for word in range(len(word_list) - 1):
            if key == word_list[word]:
                nexts_list.append(word_list[word + 1])
        next_word_dict[key] = nexts_list
    # Creates a list of every word or period that follows each word and inputs that list
    # as the keys value in the previously made dictionary

        
    return next_word_dict




def rewrite(fname):

    
    first_word_list = first_words(fname)
    next_words_dict = next_words(fname)
    length_of_file = file_length(fname)

    
    for i in range(length_of_file):
        sentence_list = [rd.choice(first_word_list)]
        # Chooses the first word of the sentence
        while sentence_list[-1] != '.':
            sentence_list.append(rd.choice(next_words_dict[sentence_list[-1]]))
        # Continues to make random choices for the next word based off the dictionary values for the previous word until '.' is chosen
        
        sentence = ' '.join(sentence_list)
        # Turns the sentence list to a string separating the elements with spaces
        
        print(sentence)






