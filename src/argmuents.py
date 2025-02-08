import sys

def arguments():
    count = 0
    __ip__ = None
    __port__ = 21
    __output__ = None

    for i in range(len(sys.argv)):
        if sys.argv[i] == "-i" or sys.argv[i] == "-I":
            __ip__ = sys.argv[count+1]
        elif sys.argv[i] == "-o" or sys.argv[i] == "-O":
            __output__ = sys.argv[count + 1]
        elif sys.argv[i] == "-p" or sys.argv[i] == "-P":
            __port__ = sys.argv[count + 1]
        count = count + 1

    if __ip__ != None:
        return __ip__, __port__, __output__