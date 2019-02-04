# Python 2.7.10
# this will copy files from a list into a new directory
''' I used this to copy images to a new directory when I know file names, but
had a large number of images to scroll over so that they could be put in cybox
One thing to note is that if reading in from a csv you get a list of lists
If this happens you need to run the following loop to convert your list of
lists to a list of strings if you do not do this the in statement will
not work.'''
''' The following block of code will give you a list of strings from
your list of lists:

h = list()
for i in your_list:
	h.append(i[0])'''

''' To read in a CSV as a list from excel the following code is what I used:

with open('image_list.csv', 'rb') as f:
	reader = csv.reader(f)
	your_list = list(reader)
'''

# os.walk goes through a directory file by file
# shutil is a useful module for copying large amounts of data
import os
import shutil
for root,directories, files in os.walk(os.getcwd()):
    for f in files:
        if f in h:
            shutil.copy2(os.path.join(root, f),os.path.join("Copied_images", f))
