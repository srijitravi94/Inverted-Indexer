# Importing required libraries
import os


# Declaring global variables
INPUT_DIRECTORY = "CORPUS" 
INPUT_FOLDER = os.getcwd() + "/" + INPUT_DIRECTORY
OUTPUT_DIRECTORY_INVERTED_INDEX = "INVERTED_INDEX"
OUTPUT_FOLDER_INVERTED_INDEX = os.getcwd() + "/" + OUTPUT_DIRECTORY_INVERTED_INDEX
OUTPUT_DIRECTORY_TERM_TABLE = "TERM_FREQUENCY_TABLES"
OUTPUT_FOLDER_TERM_TABLE = os.getcwd() + "/" + OUTPUT_DIRECTORY_TERM_TABLE
OUTPUT_DIRECTORY_DOCUMENT_TABLE = "DOCUMENT_FREQUENCY_TABLES"
OUTPUT_FOLDER_DOCUMENT_TABLE = os.getcwd() + "/" + OUTPUT_DIRECTORY_DOCUMENT_TABLE


# Function to generate term table and document table
def generateTables(invertedIndex):
    words = invertedIndex.keys()
    termTable = {}
    documentTable = {}
    for word in words:
        docIDs = invertedIndex[word].keys()
        termFrequency = 0
        documentList = []
        for docID in docIDs:
            termFrequency += invertedIndex[word][docID]
            documentList.append(docID)
        termTable[word] = termFrequency 
        docAndCount = [documentList, len(documentList)]
        documentTable[word] = docAndCount
    return termTable, documentTable


# Function to concatenate words based on input ngram
def getWord(words,ngram,i):
    if ngram==1:
        word = words[i]
    elif ngram==2:
        word = words[i] + " " + words[i+1]
    else:
        word = words[i] + " " + words[i+1] + " " + words[i+2]
    return word


# Function to get length
def getLength(words,ngram):
    if ngram==1:
        length = len(words)
    elif ngram==2:
        length = len(words)-1
    else:
        length = len(words)-2
    return length


# Function to generate ngram
def generateNGrams(ngram):
    invertedIndex = {}
    tokenDict = {}
    files = os.listdir(INPUT_FOLDER)
    for file in files:
        contents = open(INPUT_DIRECTORY + "/" + file, "r").read()
        words = contents.split()
        file = file.split(".")[0]
        length = getLength(words,ngram)
        for i in range(length):
            word = getWord(words,ngram,i)
            if word not in invertedIndex.keys():
                docIDCount = {file : 1}
                invertedIndex[word] = docIDCount
            elif file in invertedIndex[word].keys():
                invertedIndex[word][file] += 1
            else:
                docIDCount = {file : 1}
                invertedIndex[word].update(docIDCount)
    return invertedIndex


# Function to write term frequency table to a file
def writeTermTable(termTable, ngram):
    if not os.path.exists(OUTPUT_DIRECTORY_TERM_TABLE):
        os.makedirs(OUTPUT_DIRECTORY_TERM_TABLE)
    sortedTermTable = sorted(termTable.items(), key=lambda x:x[1])
    filename = ngram + "TermTable.txt"
    termFile = open(OUTPUT_FOLDER_TERM_TABLE + "/" + filename, "w")
    count = len(sortedTermTable)-1
    while count>=0:
        termFrequency = sortedTermTable[count][0] + " : " + str(sortedTermTable[count][1]) + "\n"
        termFile.write(termFrequency)
        count = count - 1
    termFile.close()


# Function to write document frequency table to a file
def writeDocumentTable(documentTable, ngram):
    if not os.path.exists(OUTPUT_DIRECTORY_DOCUMENT_TABLE):
        os.makedirs(OUTPUT_DIRECTORY_DOCUMENT_TABLE)
    filename = ngram + "DocumentTable.txt"
    documentFile = open(OUTPUT_FOLDER_DOCUMENT_TABLE + "/" + filename, "w")
    for term in sorted(documentTable.keys()):
        document = term + " : " + str(documentTable[term][0]) + " " + str(documentTable[term][1]) + "\n"
        documentFile.write(document)
    documentFile.close()


# Function to write inverted indexes of each file
def writeInvertedIndex(invertedIndex, ngram):
    if not os.path.exists(OUTPUT_DIRECTORY_INVERTED_INDEX):
        os.makedirs(OUTPUT_DIRECTORY_INVERTED_INDEX)
    filename = ngram + "InvertedIndex.txt"
    file = open(OUTPUT_FOLDER_INVERTED_INDEX + "/" + filename, "w")
    for word in invertedIndex:
        sentence = word + str(invertedIndex[word]) + "\n"
        file.write(sentence)
    file.close()


# Main function:
def main():
    #Unigram
    unigramInvertedIndex = generateNGrams(1)
    unigramTermTable, unigramDocumentTable = generateTables(unigramInvertedIndex)
    writeInvertedIndex(unigramInvertedIndex,"Unigram")
    writeTermTable(unigramTermTable,"Unigram")
    writeDocumentTable(unigramDocumentTable,"Unigram")
    
    #Bigram
    bigramInvertedIndex = generateNGrams(2)
    bigramTermTable, bigramDocumentTable = generateTables(bigramInvertedIndex)
    writeInvertedIndex(bigramInvertedIndex,"Bigram")
    writeTermTable(bigramTermTable,"Bigram")
    writeDocumentTable(bigramDocumentTable,"Bigram")
    
    #Trigram
    trigramInvertedIndex = generateNGrams(3)
    trigramTermTable, trigramDocumentTable = generateTables(trigramInvertedIndex)
    writeInvertedIndex(trigramInvertedIndex,"Trigram")
    writeTermTable(trigramTermTable,"Trigram")
    writeDocumentTable(trigramDocumentTable,"Trigram")

main()