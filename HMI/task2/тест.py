class Node: # Класс представляюший вершину графа
    def __init__(self):
        self.connections = [] #связи каждого узла

class Edge: #Класс представляющий связь между узлами
    def __init__(self, start, end, distance=1):
        self.start = start #Начало
        self.end = end #конец
        self.distance = distance #Дистанция

class Graph: #Класс представляюший все узлы и рёбра
    def __init__(self):
        self.edges = []#ребра
        self.nodes = []#узлы

    def add_node(self, node): #Метод добаления узла
        if node not in self.nodes:#Проверка на сушествующие узлы
            self.nodes.append(node)

    def add_edge(self, edge):#Метод добавления ребра
        if not any(e for e in self.edges if {e.start, e.end} == {edge.start, edge.end}): #Проверка на сушествующие ребра
            self.edges.append(edge)
            self.add_node(edge.start)
            self.add_node(edge.end)

    def shortest_path(self, start, end):#метод для нахождения кратчайшего пути между узлами
        distances = {node: float('inf') for node in self.nodes}
        previous = {node: None for node in self.nodes}
        distances[start] = 0
        unvisited = set(self.nodes)

        while unvisited:#Находим узел с мин растоянием и делаем его текушим убирая из списка
            current = min(unvisited, key=lambda node: distances[node])
            unvisited.remove(current)

            if distances[current] == float('inf'):
                break

            for edge in self.edges: # Производим перебор всех ребер с исключением их из общего списка и записываем информацию пути
                neighbor = edge.end if edge.start == current else edge.start if edge.end == current else None
                if neighbor and neighbor in unvisited:
                    new_distance = distances[current] + edge.distance
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous[neighbor] = (current, edge)

        path_nodes, path_edges = [], []
        node = end
        while node != start:#Определяем конечный путь
            prev_node, edge = previous[node]
            path_nodes.insert(0, node)
            path_edges.insert(0, edge)
            node = prev_node
        path_nodes.insert(0, start)

        return path_nodes, path_edges

class StationNode(Node):#Класс названия станции
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class MetroEdge(Edge):#Класс описания ребр с растояниями
    def __init__(self, start, end, distance):
        super().__init__(start, end, distance)

# Тестирование
map2 = Graph()
n1, n2, n3, n4, n5 = Node(), Node(), Node(), Node(), Node()
map2.add_edge(Edge(n1, n2))
map2.add_edge(Edge(n2, n3))
map2.add_edge(Edge(n2, n4))
map2.add_edge(Edge(n3, n4))
map2.add_edge(Edge(n4, n5))
assert len(map2.edges) == 5, "Неверное число связей в списке edges класса Graph"
assert len(map2.nodes) == 5, "Неверное число вершин в списке nodes класса Graph"
map2.add_edge(Edge(n2, n1))
assert len(map2.edges) == 5, "Метод add_edge добавил связь Edge(n2, n1), хотя уже имеется связь Edge(n1, n2)"
path = map2.shortest_path(n1, n5)
s = sum([e.distance for e in path[1]])
assert s == 3, "Неверная суммарная длина маршрута, возможно, некорректно работает свойство distance"

# Тестирование для карты метро
map2 = Graph()
s1, s2, s3, s4, s5 = StationNode("1"), StationNode("2"), StationNode("3"), StationNode("4"), StationNode("5")
map2.add_edge(MetroEdge(s1, s2, 1))
map2.add_edge(MetroEdge(s2, s3, 2))
map2.add_edge(MetroEdge(s2, s4, 7))
map2.add_edge(MetroEdge(s3, s4, 3))
map2.add_edge(MetroEdge(s4, s5, 1))
assert len(map2.edges) == 5, "Неверное число связей в списке edges класса Graph"
assert len(map2.nodes) == 5, "Неверное число вершин в списке nodes класса Graph"
path = map2.shortest_path(s1, s5)
assert str(path[0]) == '[1, 2, 3, 4, 5]', path[0]
s = sum([e.distance for e in path[1]])
assert s == 7, "Неверная суммарная длина маршрута для карты метро"
