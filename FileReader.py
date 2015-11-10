import re, string, random

class FileReader:
    fileName = ""
    listOfWords = []
    RADIUS = 2
    adjacencyMatrix = {}  # Example : { ("a","b","c") : {"a" : 0, "b" : 2, "c" : 3} }

    def __init__(self, fileName):
        self.fileName=fileName
        with open(fileName,'r') as f:
            for line in f:
                for word in line.split():
                    exclude = set(string.punctuation)
                    self.listOfWords.append((''.join(ch for ch in word if ch not in exclude)).lower())

    def constructAdjacency(self):
        for index, obj in enumerate(self.listOfWords):
            if index < self.RADIUS or index >= len(self.listOfWords) - self.RADIUS:
                continue #We don't need it to be here
            tupleKey = (self.listOfWords[index-1], self.listOfWords[index])
            insertWord = self.listOfWords[index+1]
            if tupleKey not in self.adjacencyMatrix:
                self.adjacencyMatrix[tupleKey] = {}
            if insertWord in self.adjacencyMatrix[tupleKey]:
                self.adjacencyMatrix[tupleKey][insertWord] += 1
            else:
                self.adjacencyMatrix[tupleKey][insertWord] = 1
        #print(self.adjacencyMatrix)
    def markovChain(self, tup, ct):
        s = tup[0] + " " + tup[1]
        while(tup in self.adjacencyMatrix and ct >= 0):
            ct-= 1
            d = self.adjacencyMatrix[tup]
            sum = 0
            for i in d:
                sum += d[i]

            n = random.random() * sum
            num = 0
            chosenWord = ""
            for i in d:
                num += d[i]
                if num > n:
                    s += " " + i
                    chosenWord = i
                    print(chosenWord)
                    break


            #print(tup[-1])
            tup = (tup[1], chosenWord)
            print(tup)
            print(s)