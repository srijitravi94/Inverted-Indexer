# Importing required libraries
import urllib.request as ul
import re
import os
from bs4 import BeautifulSoup


# Declaring global variables
INPUT_FILE = "CRAWLED_URLS.txt"
OUTPUT_FOLDER = "URL_CONTENTS"
BASE_URL = "https://en.wikipedia.org/wiki/"


# Function to extract content from the input file
def parseFile():
    file = open(INPUT_FILE, "r").read()
    links = file.splitlines()
    return links


# Function to extract the HTML Contents
def getContent():
    links = parseFile()
    contentDictionary = {}
    for link in links:
        webPage = ul.urlopen(link)
        soup = BeautifulSoup(webPage, "html.parser")
        contentDictionary[link] = soup
    return contentDictionary


# Function to write the HTML contents to an output file
def writeFile(name, content):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    filename = name + str(".txt")
    path = os.getcwd() + '/' + OUTPUT_FOLDER
    files = os.listdir(path)
    if filename not in files:
        file = open(OUTPUT_FOLDER + "/" + filename, "w")
        file.write(str(content))
    else:
        file = open(OUTPUT_FOLDER + "/" + name + "1" + str(".txt"), "w")
        file.write(str(content))
    file.close()


# Function to extract the page ID from the URL
def extractName(page):
    docID = page[len(BASE_URL):]
    docID = re.sub(r'[\W]*-*_*', '', docID)
    return docID


# Main function
def main():
    contentDictionary = getContent()
    for link in contentDictionary:
        writeFile(extractName(link), contentDictionary[link])
main()