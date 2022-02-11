class TaxiData:
    def __init__(self, nPlate, day, sHour, sSec, eHour, eSec, km):
        self.nPlate = nPlate
        self.day = day
        self.sHour = sHour
        self.eHour = eHour
        self.sSec = sSec
        self.eSec = eSec
        self.km = km
def ReadAll():
    l = []
    with open("input.txt") as f:
        for t in f.read().split('\n'):
            d = t.split(' ')
            l.append(TaxiData(d[0],int(d[1]),int(d[2]),int(d[3]),int(d[4]),int(d[5]),int(d[6])))
    return l
def Task2(d):
    maxH = -1
    maxS = -1
    winners = []
    for l in d:
        if l.sHour > maxH or l.sHour == maxH and l.sSec > maxS:
            winners = []
            maxH = l.sHour
            maxS = l.sSec
            winners.append(l)
        elif l.sHour == maxH and l.sSec == maxS:
            winners.append(l)
    print('2. feladat:')
    for w in winners:
        print(f'{w.nPlate} {w.sHour}:{w.sSec} {w.km}')
    print('')
def Task3(d):
    maxH = -1
    maxS = -1
    winners = []
    for l in d:
        if l.day != d[-1].day:
            continue # feltetelezzuk hogy sorban vannak nap szerint
        if l.eHour > maxH or l.eHour == maxH and l.eSec > maxS:
            winners = []
            maxH = l.eHour
            maxS = l.eSec
            winners.append(l)
        elif l.eHour == maxH and l.eSec == maxS:
            winners.append(l)
    print('3. feladat:')
    for w in winners:
        print(f'{w.nPlate} {w.eHour}:{w.eSec} {w.km}')
    print('')
def Task4(d):
    days = {}
    for x in range(1,d[-1].day+1):
        days[x] = []
    for a in d:
        days[a.day].append(a)
    print('4. feladat:')
    for d in days:
        print(f'{d}. nap : {len(days[d])} db fuvar')
    print('')
    return days
def Task5(p,days):
    allDay = True
    for x in days:
        inc = False
        for y in days[x]:
            if p in y.nPlate:
                inc = True
        if not inc:
            print(f'A hét {x}. napján nem volt forgalomban')
            allDay = False
    if allDay:
        print('Minden nap forgalomban volt.')
def Task6(d,p):
    maxH = -1
    maxS = -1
    for l in d:
        if l.nPlate == p:
            if l.eHour > maxH or l.eHour == maxH and l.eSec > maxS:
                maxH = l.eHour
                maxS = l.eSec
                lDay = l
    print('6. feladat:')
    print(f'A {p} rendszámú autó a(z) {lDay.day}. napon {lDay.eHour}:{lDay.eSec}-órakor érkezett be legkésöbb.\n')
    
def Main():
    dataList = ReadAll()
    Task2(dataList)
    Task3(dataList)
    days = Task4(dataList)
    print('Kérem egy autó rendszámát: ', end='')
    nPlateInput = input().upper()
    Task5(nPlateInput,days)
    Task6(dataList,nPlateInput)
if __name__ == "__main__":
    Main()