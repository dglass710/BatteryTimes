def commaNumber(num):
    nStr = str(num)
    strList = []
    while len(nStr) > 0:
        strList.append(nStr[-3:])
        nStr = nStr[:-3]
    fStr = ''
    for i in range(len(strList)):
        fStr += strList.pop()
        if len(strList) > 0:
            fStr += ','
    return fStr
