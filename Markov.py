from FileReader import FileReader
if __name__ == "__main__":
    d = FileReader("fiftyshades.txt")
    d.constructAdjacency()
    d.markovChain(('my', 'thighs'), 15)