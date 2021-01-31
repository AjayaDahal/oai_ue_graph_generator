'''Created by Ajaya Dahal
Mississippi State Universtity
A python script that plots graph for the OAI UE test
'''
from itertools import cycle


import matplotlib.pyplot as plt


def index(a_list, value):
    try:
        return a_list.index(value)
    except ValueError:
        return None

def Average(a_list):
    return sum(a_list) / len(a_list)


fileName = "data.txt"  # Our input is in this file
file = open('data.txt', 'r') #read mode

Lines = file.readlines()

bitrateCollection = []
titleCollection = []

#                                           Test1      Test2  ....
# This will hold all the tests in a list [[1,2,3,4], [1,2,3,4],....]
tests = []

# Lines for each test which will be resetted everytime it detects a new test in the file
testLines = []

location = 0
size = len(Lines)
topic = []
while location < (size - 1):
    first = ""
    try:
        first = (Lines[location].split(' ')[0])
        if(first == 'Test'):
            i = 1
            while Lines[location+i]=="\n":
                i+=1

            if Lines[location + i] != "\n":
                topic.append(Lines[location + i])


    except:
        pass

    if first != 'Test' :
        if Lines[location]!='\n':
            testLines.append(Lines[location])
    else:
        if(len(testLines)>5):
            tests.append(testLines)
            testLines=[]
    location+=1
#last test is not appended, so lets append it!
tests.append(testLines)


location = 0
testNumber = 0
for test in tests:
    if location%6==0:
        testNumber+=1
        print(testNumber)
    title = "Test: " + str(testNumber) + " " + topic[location].strip('\n')
    transfer = []
    bitrate = []

    for line in test:

        if (line != ''):
            line = line.strip('\n')
            words = line.split(' ')
            indBitrate = index(words, 'Mbits/sec')  # Bitrate or Bandwidth
            if indBitrate != None:
                bitrate.append(float(words[indBitrate - 1]))

    average = float(Average(bitrate))
    for i in bitrate:
        if float(i) > average+2:
            bitrate.remove(i)
    maxi = max(bitrate)
    #plt.plot(transfer)
    plt.plot(bitrate)
    plt.xlim(0,115)
    plt.ylim(0, 35)
    #print('Transfer: ',len(transfer))
    #print('Bandwidth: ', len(bitrate))
    plt.ylabel('Transfer in MBits/sec')
    plt.legend(["Bandwidth"])
    plt.title(title)

    path = 'Outputs/'+"Test"+str(testNumber) + " " + topic[location].strip('\n')
    plt.savefig(path)
    plt.show()
    location+=1
