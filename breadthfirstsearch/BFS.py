class Node:
    def __init__(self, val):
        self.value = val
        self.neighbors = []

    def set_left(self, n):
        return self.value

    def add_neighbor(self, node):
        self.neighbors.append(node)

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, value):
        node = Node(value)
        self.nodes.append(node)
        return node

    def get_nodes(self):
        return self.nodes

    def find_node(self, v):
        for n in self.get_nodes():
            if n.get_value() == v:
                return n
        raise ValueError("Node is not found")

star_systems = ['Aldebaran', 'Alderamin', 'Algol', 'Alioth', 'Aljanah', 'Alkaid', 'Alnair', 'Alnasl', 'Alpha Centauri', 'Altair', 'Ankaa', 'Antares', 'Arcturus', 'Ascella', 'Castor', 'Cor Caroli', 'Deneb', 'Denebola', 'Diphda', 'Fomalhaut', 'Hamal', 'Larawag', 'Markab', 'Menkalinan', 'Menkent', 'Merak', 'Muphrid', 'Musica', 'Nihal', 'Peacock', 'Phecda', 'Pollux', 'Procyon', 'Ran', 'Rasalhague', 'Regulus', 'Sabik', 'Sheratan', 'Sirius', 'Sol', 'Tarazed', 'Tau Ceti', 'Tiaki', 'Vega', 'Zaurak', 'Zosma']

hyperlanes = [['Aldebaran', 'Menkalinan'], ['Aldebaran', 'Pollux'], ['Alderamin', 'Cor Caroli'], ['Alderamin', 'Markab'], ['Alderamin', 'Vega'], ['Algol', 'Menkalinan'], ['Algol', 'Merak'], ['Algol', 'Phecda'], ['Alioth', 'Cor Caroli'], ['Aljanah', 'Markab'], ['Aljanah', 'Tarazed'], ['Alkaid', 'Markab'], ['Alkaid', 'Musica'], ['Alpha Centauri', 'Sol'], ['Alnair', 'Alpha Centauri'], ['Alnair', 'Ankaa'], ['Alnair', 'Muphrid'], ['Alnair', 'Tiaki'], ['Alnasl', 'Sabik'], ['Alnasl', 'Ascella'], ['Altair', 'Arcturus'], ['Altair', 'Fomalhaut'], ['Altair', 'Vega'], ['Ankaa', 'Denebola'], ['Ankaa', 'Sirius'], ['Antares', 'Ascella'], ['Antares', 'Larawag'], ['Arcturus', 'Muphrid'], ['Arcturus', 'Rasalhague'], ['Castor', 'Pollux'], ['Castor', 'Zaurak'], ['Deneb', 'Tarazed'], ['Denebola', 'Zosma'], ['Diphda', 'Fomalhaut'], ['Diphda', 'Hamal'], ['Diphda', 'Tau Ceti'], ['Fomalhaut', 'Sol'], ['Hamal', 'Phecda'], ['Larawag', 'Menkent'], ['Larawag', 'Peacock'], ['Menkent', 'Tiaki'], ['Nihal', 'Regulus'], ["Pollux", "Procyon"], ['Procyon', 'Ran'], ['Ran', 'Sirius'], ['Ran', 'Sol'], ['Ran', 'Tau Ceti'], ['Regulus', 'Zaurak'], ['Regulus', 'Zosma'], ['Sheratan', 'Tau Ceti']]

from collections import deque

galaxy = Graph()

for system in star_systems:
    galaxy.add_node(system)

for s1, s2 in hyperlanes:
    node_1 = galaxy.find_node(s1)
    node_2 = galaxy.find_node(s2)
    node_1.add_neighbor(node_2)
    node_2.add_neighbor(node_1)

def shortest_path(s1_name, s2_name):
    s1_node = galaxy.find_node(s1_name)
    s2_node = galaxy.find_node(s2_name)

    visited = []
    to_visit = deque([[s1_node]])
    visited.append(s1_node)

    while to_visit:
        path = to_visit.popleft()
        current = path(-1)

        print("Visiting", current.get_value(), [n.get_value() for n in path])

        if current == s2_node:
            print("Target acquired:", s2_node.get_value())
            return [n.get_value() for n in path]

        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.append(neighbor)
                new_path = path + [neighbor]
                to_visit.append(new_path)

    return None

def shortest_path_length(s1_name, s2_name):
    path = shortest_path(s1_name, s2_name)
    if path is None:
        return None
    return len(path) - 1






