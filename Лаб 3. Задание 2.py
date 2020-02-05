"""
Классы – Море, Континент, Государство, Остров, Суша;
Classes - Sea, Continent, State, Island, Land;
"""

class Sea:
    def __init__(self, area, name, island):
        self.name = name
        self.area = area
        self.listIsland = Sea.addListIsland(island)

    def addListIsland(island):
        listIsland = []
        if (type(island) == list):
            i = 0
            for i in range(len(island)):
                listIsland.append(island[i])
            return listIsland
        else:
            return island

    def __str__(self):
        return 'Море ' + self.name + ', площадь ' + str(self.area) + ' кв. км'

    def printListIsland(self):
        print("Список островов:")
        if (type(self.listIsland) == list):
            i = 0
            for i in self.listIsland:
                print(i)
        else:
            print(self.listIsland)
        print('\n')


class Land:
    def __init__(self, area, name, state):
        self.name = name
        self.area = area
        self.listState = Land.addListState(state)

    def addListState(state):
        listState = []
        if(type(state) == list):
            i = 0
            for i in range(len(state)):
                listState.append(state[i])
            return listState
        else:
            return state

    def printListState(self):
        print("Список государств:")
        if (type(self.listState) == list):
            i = 0
            for i in self.listState:
                print(i)
        else:
            print(self.listState)
        print('\n')

    #def __str__(self):
    #def addListIsland(self):
    #def addListContinent(self):


class Continent(Land):
    def __init__(self, area, name, state):
        Land.__init__(self, area, name, state)

    def __str__(self):
        return 'Континент ' + self.name + ', площадь ' + str(self.area) + ' кв. км'


class Island(Land):
    def __init__(self, area, name, state):
        Land.__init__(self, area, name, state)

    def __str__(self):
        return 'Остров ' + self.name + ', площадь ' + str(self.area) + ' кв. км'


class State:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    #def addListContinent(continent):

    #def addListIsland(island):


Ukraine = State("Ukraine")
Russia = State("Russia")
countries = [Ukraine, Russia]
Zenzic = Island(7, "Zenzic", countries)
print(Zenzic)
Zenzic.printListState()
Yeisk_spit = Island(9, 'Yeisk_spit', Ukraine)
print(Yeisk_spit)
Yeisk_spit.printListState()
islands = [Zenzic, Yeisk_spit]
Azov = Sea(100, 'Azov', islands)
print(Azov)