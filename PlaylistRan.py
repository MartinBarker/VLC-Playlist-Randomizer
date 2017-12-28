#Playlist randomizer for VLC media player
#Martin Barker
#python3

from random import randint

#linked list setup
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext

def size(self):
    current = self.head
    count = 0
    while current != None:
        count = count + 1
        current = current.getNext()
    return count

class UnorderedList:
    def __init__(self):
        self.head = None
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

def isEmpty(self):
    return self.head == None

def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)

import struct
from collections import namedtuple

filename = input('\nEnter playlist (.xspf) filename [in same directory as this program]: ')
filename = filename + '.xspf'
print('randomizing the playlist file: ', filename)

#read in playlist file in directory as text file
f = open(filename, 'r')                               #open file
message = f.read()                                    #store file contents as string message
last_open = message.rfind('<vlc:id>')                 #find last instance of vlc:id open tag
last_close = message.rfind('</vlc:id>')               #find last instance of vlc:id close tag
count_string = message[last_open+8:last_close]        #use found indexes to create track count string
count = int(count_string)                             #convert track count string to int

mylist = UnorderedList()                              #create unordered linked list

#print('number of tracks:', count)

for i in range (0, count+1):                          #for loop which runs through the number of tracks
#    print('were in loop number: ', i)
    vlcid_open = findnth(message, '<vlc:id>', i)      #finds i'th occurance of vlc:id open and close tag
    vlcid_close = findnth(message, '</vlc:id>', i)
     #track num occurs at index vlcid_open

#generate ran num from 0 to count
    rannum = randint(0, count)
#check that ran num is not in linked list
    while(mylist.search(rannum)):                     #if rannum is in linked list, re-generate
        rannum = randint(0, count)
    else:                                             #else add rannum to linked list
        mylist.add(rannum)
    #print('rannum generated: ', rannum, '\n')
#add ran num to linkedlist
    rannum_string = str(rannum)
#update message string to inlcude new ran num for track index
    message = message[:vlcid_open+8] + rannum_string + message[vlcid_close:]

f.close()
#write message to file
f = open(filename, 'w')
f.write(message)
f.close()
print('randomization completed, and has been writen to ', filename)
