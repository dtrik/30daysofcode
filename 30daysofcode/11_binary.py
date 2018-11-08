if __name__ == '__main__':
    n = int(input())
    bin_n = "{0:b}".format(n)
    #print(bin_n)
    consec = 0
    max_consec = [0]
    for digit in bin_n:
        if digit == '1':
            consec +=1
        else:
            max_consec.append(consec)
            consec = 0
    max_consec.append(consec)
    print(max(max_consec))