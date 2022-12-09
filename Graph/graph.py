"""
Обратите внимание: элемент «в ы ~ (you) отображается на массив. Следовательно,
результатом выражения graph[ "you"] является массив всех ваших
соседей.
"""
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anja', 'saja']
graph['alice'] = ['peggy']
graph['anja'] = []
graph['yulia'] = []
graph['marin'] = []
print(graph)