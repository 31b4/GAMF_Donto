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
    print('\n6. feladat:')
    if maxH is not -1:
        print(f'A {p} rendszámú autó a(z) {lDay.day}. napon {lDay.eHour}:{lDay.eSec}-órakor érkezett be legkésöbb.\n')
    else:
        print('Nincs ilyen rendszámú autó az adatbázisban.\n')
def EstimatedTime(h1,s1,h2,s2):
    time = []#[hour,min]
    if h1 == h2:
        time = [0,s2-s1]
    elif h1< h2:
        if s2<s1:
            time = [0,60-s1+s2]
        else:
            time = [h2-h1,s2-s1]
    return time
def AddTime(h1,s1,h2,s2):
    time =[h1+h2,0]
    if s1+s2 > 60:
        time[0] +=1
        time[1] = (s1+s2)-60
    else:
        time[1] = s1+s2
    return time
def Task7(d):
    cars = []
    for car in d:
        if not car.nPlate in cars:
            cars.append(car.nPlate)
    print('7. feladat:')
    for car in cars:
        days = {}
        for x in range(1,d[-1].day+1):
            days[x] = [0,0]
        for l in d:
            if l.nPlate == car:
                t = EstimatedTime(l.sHour,l.sSec, l.eHour,l.eSec)
                days[l.day] = AddTime(t[0],t[1],days[l.day][0],days[l.day][1])
        print(car)
        for x in days:
            if not (days[x][0]==0 and days[x][1]==0):
                print(f'{x}. nap: {days[x][0]} ora {days[x][1]} perc')
        print('')
def Main():
    dataList = ReadAll()
    Task2(dataList)
    Task3(dataList)
    days = Task4(dataList)
    print('5. feladat:')
    print('Kérem egy autó rendszámát: ', end='')
    nPlateInput = input().upper()
    Task5(nPlateInput,days)
    Task6(dataList,nPlateInput)
    Task7(dataList)
if __name__ == "__main__":
    Main()