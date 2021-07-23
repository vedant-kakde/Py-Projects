# WORD COUNTER

# We want a program which can count the words from each text file automatically

# First we need a sample text file
!wget https://filesamples.com/samples/document/txt/sample1.txt

# Opening a file using read mode
f = open("/content/sample1.txt", "r")

# Empty List
c=[]

# Splitting all the words inside the text file and appending it to the list
for x in f:
 print(x)
 c.append(x.split(' '))
c

# Count of words inside the list c
d=0
for i in range(len(c)):
 d=d+1
d

len(c)