#!/usr/bin/python
### import modules
import subprocess
import sys
import os
import string

### define classes

# Indexer object
# holds a list of patterns to search for and has
# a method to actually do the searching.
# List of applicable patterns is to be filled with Indexer.addPattern(pattern="").
# When Indexer.run(text="") is called, it expects a string in which it searches for each pattern.
# The string is split into a list of words by applying text.split(" "). The string containig the text
# to be searched must be cleaned from any non-printable characters a.s.o (for excample carriage return)
# by your main programm. You also need to strip out any surplus blanks.
class Indexer:
    # constants
    WORDS = 1
    LINES = 2

    # initialize pattern list
    __patterns = []
    __results = {}
    __text = []
    __active_pattern = {}

     # add a pattern to the list of patterns
    def addPattern(self, pattern, mode=WORDS, count=1):
        self.__patterns.append({'pattern': pattern, 'mode': mode, 'count': count})

    def __run_lines(self):
        pass

    def __run_words(self):
        # put lines together to a single string
        text = ""
        for line in self.__text:
            text = text + line

        # replace carriage returns with blanks to make string splittable by blanks
        # and keep it reliably searchable
        text = string.replace(text, "\n"," ")

        # split text string into its words
        wordlist = text.split(" ")

        pattern = self.__active_pattern['pattern']

        # look for each pattern in the wordlist and return
        # the pattern and its following word in the list
        # this needs work!
        # - implement a range of following words to return
        # - write findings in a list of tuples and return this list
        #   instead of printing to stdout

        # buffer to hold results for this pattern in a list
        resultbuffer = []
        # iteration counter
        count = 0
        # start index set to 0 to start at beginning of wordlist
        start = 0

        # search in wordlist for pattern until all where found, no point in searching to the end when all found
        while count < wordlist.count(pattern):
            #
            found = wordlist.index(pattern,start)
            start = found + 1
            count = count + 1
            resstring = ""
            for buff in wordlist[start:start + self.__active_pattern['count']]:
                resstring = resstring + " " + buff
            resstring = resstring.strip()
            if not resstring in resultbuffer:
                try:
                    resultbuffer.append(resstring)
                except:
                    print "error in resultbuffer"
        self.__results[pattern] = resultbuffer


    # actually do the searching

    def run(self,text=""):
        self.__text = text
        for pat in self.__patterns:
            self.__active_pattern = pat
            # create parser function dictionary, need to do this here, no way to use self outside of
            # object method. and no way to use __run_* without self
            # I even need to define this here, because python throws an exception, that there is no self.__active_pattern
            # when this is defined outside loop
            functions = {1: self.__run_words(), 2: self.__run_lines()}
            functions[self.__active_pattern['mode']]
        return self.__results


### main program

# convert pdf input stream from stdin to text lines.
# We need to rely on pdftotext from xpdf-tools package
# because pyPdf's extractText Method is unriliable (and says so itself!)
p = os.popen("pdftotext -raw /dev/stdin -")
linebuff = p.readlines()
p.close()

# instantiate indexer object
indexer = Indexer()
# add search patterns to indexer, this is intended to work
# with a cups test page
indexer.addPattern("Patient:")
indexer.addPattern("Entnahmedatum:", count=2)
indexer.addPattern("folgt")
# now run the indexer and see the results :)
results = indexer.run(linebuff)
print results

