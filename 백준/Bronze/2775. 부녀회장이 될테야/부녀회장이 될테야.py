import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for i in range(t):
        k = int(sys.stdin.readline())    
        n = int(sys.stdin.readline())    

        apartment = [i for i in range(1, n+1)]

        for i in range(k):
            temp = 0
            for j in range(len(apartment)):
                temp += apartment[j]
                apartment[j] = temp 

        print(apartment[-1])