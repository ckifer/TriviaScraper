
import pytesseract
import numpy
import re
from removeirrelevant import remove_irrelevant

def stringify_screenshot(imageQ, imageAone, imageAtwo, imageAthree):
    query = pytesseract.image_to_string(imageQ)
    answerOne = pytesseract.image_to_string(imageAone)
    answerTwo = pytesseract.image_to_string(imageAtwo)
    answerThree = pytesseract.image_to_string(imageAthree)
    print(query)
    print(answerOne)
    print(answerTwo)
    print(answerThree)

    print("Question: " + query)
    query = remove_irrelevant(query)
    query = query.replace(' ', '+')
    results = [query, answerOne, answerTwo, answerThree]
    return results