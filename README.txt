CS 6200 INFORMATION RETRIEVAL Fall '17'
Assignment 3

Submitted By : Srijit Ravishankar
NUID : 001282238

SUMMARY :
		** The given instructions contains software installations and running the program that is suitable in MAC environment ** 


GENERAL INSTRUCTIONS :
1. Install Python v.3.6.1


INSTRUCTIONS TO RUN THE PROGRAM : 
1. Open Terminal
2. Navigate to the desired directory
3. Enter the command "python GeneratingContent.py"
4. This creates a folder "URL_CONTENTS" which contains 1000 files.
5. Enter the command "python GeneratingCorpus.py"
6. This creates a folder "CORPUS" which contains 1000 files.
7. Now enter the command "python InvertedIndexer.py"
8. This generates 3 folders namely "INVERTED_INDEX", "TERM_FREQUENCY_TABLES", "DOCUMENT_FREQUENCY_TABLES", which has 3 files each for Unigram, Bigram and Trigram.



OTHER INSTRUCTIONS :

1. Folder "URL_CONTENTS" contains raw html data of each link.
2. The output for Task 1 is in folder "CORPUS" which contains texts after cleaning/processing. The process of cleaning is done by removing HTML tags, URLs, references to images, tables, formulas, and navigational components. Also, case-folding and punctuations are handled.
3. The output for Task 2 is in folder "INVERTED_INDEX" which contains N-Grams and their inverted indexes.
4. The output for Rask 3(a) is in folder "TERM_FREQUENCY_TABLES" which contains N-Grams and their term frequency tables.
5. The output for Rask 3(b) is in folder "DOCUMENT_FREQUENCY_TABLES" which contains N-Grams and their document frequency tables.
6. "STOP_LIST.txt" contains lists of stop words and instructions on how to determine the cut-off value, given a unigram term frequency data.