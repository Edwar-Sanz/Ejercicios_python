
def contador(string):
	conteo = {}
	for i in string:
		conteo.setdefault(i, 0)
		conteo [i] += 1


# otra solucion
from collections import Counter

def count(string):
    return Counter(string)


# otra solucion
def count(string):
    return {i: string.count(i) for i in string}


