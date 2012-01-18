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
    # initialize pattern list
    __patterns = []

    # add a pattern to the list of patterns
    def addPattern(self,pattern=""):
        self.__patterns.append(pattern)

    # actually do the searching
    def run(self,text=""):
        # split text string into its words
        wordlist = text.split(" ")

        # look for each pattern in the wordlist and return
        # the pattern and its following word in the list
        # this needs work!
        # - implement a range of following words to return
        # - write findings in a list of tuples and return this list
        #   instead of printing to stdout
        for pattern in self.__patterns:
            print "found", wordlist.count(pattern), "appearances of", pattern
            count = 0
            start = 0
            while count < wordlist.count(pattern):
                found = wordlist.index(pattern,start)
                start = found + 1
                count = count + 1
                try:
                    print wordlist[found],wordlist[start]
                except:
                    pass


### main program

# convert pdf input stream from stdin to text lines.
# We need to rely on pdftotext from xpdf-tools package
# because pyPdf's extractText Method is unriliable (and says so itself!)
p = os.popen("pdftotext -raw /dev/stdin -")
linebuff = p.readlines()
p.close()

# put lines together to a single string
text = ""
for line in linebuff:
    text = text + line

# replace carriage returns with blanks to make string splittable by blanks
# and keep it reliably searchable
text = string.replace(text, "\n"," ")

# instantiate indexer object
indexer = Indexer()
# add search patterns to indexer, this is intended to work
# with a cups test page
indexer.addPattern("CUPS")
indexer.addPattern("Page")
# now run the indexer and see the results :)
indexer.run(text)

