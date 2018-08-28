from screenshot import acquire_image
from ocr import stringify_screenshot
import cv2
import time
import re
import requests
from PIL import Image
from scaleImage import scaleImage

def main():
    acquire_image()
    image = Image.open('/Users/coltinkifer/Desktop/cashShowQ.png')
    imageAone = Image.open('/Users/coltinkifer/Desktop/cashShowAone.png')
    imageAtwo = Image.open('/Users/coltinkifer/Desktop/cashShowAtwo.png')
    imageAthree = Image.open('/Users/coltinkifer/Desktop/cashShowAthree.png')
    image = scaleImage(image)
    imageAone = scaleImage(imageAone)
    imageAtwo = scaleImage(imageAtwo)
    imageAthree = scaleImage(imageAthree)
    results = stringify_screenshot(image, imageAone, imageAtwo, imageAthree)
    question = results[0]
    params = {'q': question }
    url = 'https://www.google.com/search'
    r = requests.get(url, params=params)
    print("GOOGLING: " + r.url)
    print("STATUS_CODE: " + str(r.status_code) + '\n')

    body = r.text
    if len(results) > 2:
        answers = [results[1], results[2], results[3]]
        count = []
        totalCount = 0
        for index, answer in enumerate(answers):
            regex = "(?i)" + answer
            matches = len(re.findall(regex, body, re.IGNORECASE))
            count.append(matches)
            totalCount = totalCount + matches
            print("REGEX: " + regex + ": " + str(count[index]))
        print("Total matches: " + str(totalCount))
    else:
        print("OCR FAILED!!!")
  

        
if __name__ == "__main__":
    while True:
        input("Ready...")
        start_time = time.time()
        main()
        print("--- %s seconds ---" % (time.time() - start_time))