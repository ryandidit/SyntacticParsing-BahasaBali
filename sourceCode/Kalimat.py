def getKal():
    file = "parse/script/Sentence.txt"
    if (file):
        f = open(file, "r")
        data = f.read().splitlines()
        return data

