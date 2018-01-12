# Importing required libraries
import os
import re
from bs4 import BeautifulSoup


# Declaring global variables
INPUT_DIRECTORY = "URL_CONTENTS"
OUTPUT_DIRECTORY = "CORPUS"
INPUT_FOLDER = os.getcwd() + "/" + INPUT_DIRECTORY


# Function to generate link and content dictionary
def getFileContents():
    files = os.listdir(INPUT_FOLDER)
    fileDictionary = {}
    for file in files:
        key = file.split(".")[0]
        value = open(INPUT_DIRECTORY + "/" + file, "r")
        fileDictionary[key] = value.read()
    return fileDictionary


# Function to clean the files
def cleanTextFiles():
    fileDictionary = getFileContents()
    for file in fileDictionary:
        fileContent = fileDictionary[file]
        if fileContent.find('<span class="mw-headline" id="See_also">') != -1:
            fileContent = fileContent[:fileContent.index('<span class="mw-headline" id="See_also">')]
        elif fileContent.find('<span class="mw-headline" id="References">') != -1:
            fileContent = fileContent[:fileContent.index('<span class="mw-headline" id="References">')]
        if fileContent.find('<div class="toc" id="toc">') != -1:
            startContent = fileContent[:fileContent.index('<div class="toc" id="toc">')]
            endContent = fileContent[fileContent.find('</div>', (fileContent.find('</div>',(fileContent.index('<div class="toc" id="toc">') + 1)) + 1)) + 7:]
            fileContent = startContent + endContent
        fileDictionary[file] = fileContent
    return fileDictionary


# Function to check whether the given word/text is float
def isFloat(word):
    word = re.sub('[.,]', '', word)
    try:
        float(word)
        return True
    except ValueError:
        return False


# Function to remove punctuations
def removePunctuations(word):
    if word:
        if((word[-1] == '.') or
           (word[-1] == ',')):
            word = word[:len(word)-1]
    if word:
        if((word[0] == '.') or
           (word[0] == ',')):
            word = word[1:]
    return word


# Function to extract text
def extractText():
    texts = cleanTextFiles()
    for text in texts:
        fileContent = texts[text] 
        soup = BeautifulSoup(fileContent, "html.parser")
        title = soup.find('title').text
        header = soup.find('h1').text
        body = ""
        divs = soup.findAll('div', {'id' : 'bodyContent'})
        for div in divs:
            body += div.text
        fullContent = title + " " + header + " " + body
        symbols = re.compile('[_!@\s#$%=+~()}{\][^?&*:;\\/|<>"\']')
        fullContent = re.sub(symbols, ' ', fullContent)
        words = fullContent.split()
        fullText = []
        for word in words:
            if isFloat(word):
                fullText.append(word)
            else:
                fullText.append(removePunctuations(word))
        texts[text] = fullText
    return texts


# Function to store file and extracted text in a dictionary
def convertToText():
    fileDictionary = extractText()
    for file in fileDictionary:
        contents = fileDictionary[file]
        text = ""
        for content in contents:
            text += content.lower() + " "
        fileDictionary[file] = text
    return fileDictionary


# Function to write the content to a file
def writeFile(name, content):
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)
    filename = name + str(".txt")
    path = os.getcwd() + '/' + OUTPUT_DIRECTORY
    files = os.listdir(path)
    if filename not in files:
        file = open(OUTPUT_DIRECTORY + "/" + filename, "w")
        file.write(str(content))
    else:
        file = open(OUTPUT_DIRECTORY + "/" + name + "1" + str(".txt"), "w")
        file.write(str(content))
    file.close()


# Main function
def main():
    fileDictionary = convertToText()
    for link in fileDictionary:
        writeFile(link, fileDictionary[link])
main()