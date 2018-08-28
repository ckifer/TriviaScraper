import re

def remove_irrelevant(query):
    stopwords = ['what','who','is','a','at','is','he', 'she', 'which', '\'', '\"', '`', '?', '.', ',', '(', ')']
    edgecases = ['ﬂ'];
    querywords = query.split()

    resultwords  = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)

    return result;