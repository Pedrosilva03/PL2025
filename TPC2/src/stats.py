from Obra import Obra

def sortComposers(lista_obras):
    compositores = []
    for obra in lista_obras:
        compositor = obra.getCompositor()
        if compositor not in compositores:
            compositores.append(compositor)

    return sorted(compositores)

def countMusicByPeriod(lista_obras):
    musicByPeriod = {}
    for obra in lista_obras:
        period = obra.getPeriodo()
        if period in musicByPeriod.keys():
            musicByPeriod[period] += 1
        else:
            musicByPeriod[period] = 1
    
    return musicByPeriod

def musicByPeriod(lista_obras):
    musicByPeriod = {}
    for obra in lista_obras:
        period = obra.getPeriodo()
        if period in musicByPeriod.keys():
            musicByPeriod[period].append(obra.getNome())
        else:
            musicByPeriod[period] = [obra.getNome()]

    return musicByPeriod