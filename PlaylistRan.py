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

import randomize
import sort

print('-------------------------------')
print('Martin Barker VLC Playlist Tool')
print('-------------------------------')

filename = input('\nEnter target playlist (.xspf) filename [in same directory as this program]: ')
filename = filename + '.xspf'
print('randomizing the playlist file: ', filename)
#
#  valid()   CHECKS THAT PLAYLIST FILE EXISTS AND CAN BE OPENED
#


initial_i = 1
loop = 1
while loop == 1:
    print('\nWhat would you like to do to', filename, ' ?')
    print('1) Randomize  ')
    print('2) Sort by genre  ')
    print('0) exit  ')
    initial_i = input('')
    #error handle
    if initial_i == '1':
        ran_i = 1
        loop2 = 1
        while loop2 == 1:
            print('\n~~~Randomization~~~')
            print(' Would you like to:')
            print(' 1) Overwrite playlist ')
            print(' 2) Save to new playlist ')
            print(' 0) Go back to main menu ')
            ran_i = input('\n')
            if ran_i == '0':
                loop2 = loop2+1
            elif ran_i == '1':
                print("Overwrite playlist")
                randomize.ran(filename, filename)
            elif ran_i == '2':
                print("Save to new playlist")
                savename = 'x'
                print('     Enter the name of the output playlist file:')
                savename = input('      ')
                savename = savename + '.xspf'
                print('     Output Playlist: ', savename)
                # verify(savename)
                randomize.ran(filename, savename)
            else:
                print("Input was not correct, please enter a single number")

    elif initial_i == '0':
        loop = loop+1
         #quit
    elif initial_i == '2':
        ran_i = 1
        loop2 = 1
        while loop2 == 1:
            print('\n+++Sort By Genre+++')
            print(' Would you like to:')
            print(' 1) Overwrite playlist ')
            print(' 2) Save to new playlist ')
            print(' 0) Go back to main menu ')
            ran_i = input('\n')
            if ran_i == '0':
                loop2 = loop2+1
            elif ran_i == '1':
                print("Overwrite playlist")
                sort.genreSort(filename, filename)
            elif ran_i == '2':
                print("Save to new playlist")
                savename = 'x'
                print('     Enter the name of the output playlist file:')
                savename = input('      ')
                savename = savename + '.xspf'
                print('     Output Playlist: ', savename)
                # verify(savename)
                sort.genreSort(filename, savename)
            else:
                print("Input was not correct, please enter a single number")
        #overwrite? save to new? should be selection specific decision
    else:
        print("Input was not correct, please enter a single number")


print('\nexiting...')
