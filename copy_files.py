# Python 2.7.10
# this will copy files from a list into a new directory
''' I used this to copy images to a new directory when I know file names, but
had a large number of images to scroll over so that they could be put in cybox
One thing to note is that if reading in from a csv you get a list of lists
If this happens you need to run the following loop to convert your list of
lists to a list of strings if you do not do this the in statement will
not work.'''

import csv
import shutil
import os
# file directory you want to copy from 
Dir_copy = "C:\\Users\carroll1\Desktop\JPg_Images"
# list address
list_loc= "C:\\Users\carroll1\Desktop\Image_list2015.csv"
# location you want files to be copied
copy_loc = "C:\\Users\carroll1\Desktop\copied_images2015"
# make directory you want to copy to
os.mkdir(copy_loc)
# read in list from a csv of file names
with open(list_loc, 'rb') as f:
	reader = csv.reader(f)
	your_list = list(reader)

''' The following block of code will give you a list of strings from
your list of lists:'''

h = list()
for i in your_list:
	h.append(i[0])



# os.walk goes through a directory file by file
# shutil is a useful module for copying large amounts of data
for root,directories, files in os.walk(Dir_copy):
    for f in files:
        if f in h:
            shutil.copy2(os.path.join(root, f), copy_loc)
