import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

edges = [(1,2,{'weight':223}), (1,5,{'weight':197}),
         (1,3,{'weight':58}), (1,4,{'weight':173}),
         (2,8,{'weight':75}), (2,5,{'weight':125}),
         (3,5,{'weight':90}), (3,6,{'weight':101}),
         (3,4,{'weight':66}), (4,3,{'weight':66}),
         (4,7,{'weight':193}), (5,2,{'weight':125}),
         (5,3,{'weight':90}), (5,8,{'weight':95}),
         (6,7,{'weight':73}), (6,8,{'weight':83}),
         (6,9,{'weight':195}), (6,10,{'weight':235}),
         (7,6,{'weight':73}), (7,10,{'weight':275}),
         (8,2,{'weight':75}), (8,5,{'weight':95}),
         (8,6,{'weight':83}), (8,9,{'weight':111}),
         (9,6,{'weight':195}), (9,8,{'weight':111}),
         (9,10,{'weight':118}) ]

G.add_edges_from(edges)
s = 1
t = 10
path = nx.dijkstra_path(G, s, t)

print("The shortest path from Switching Station", s, "to Packing Area", t, "is:")

for i in range(len(path)-1):
    node = path[i]
    print(node, end=" --> ")
print(destination)

prod_to_ss = (159 + 97 + 79 + 172) * 100
ss_to_packing = 100 * (58 + 101 + 235)
produc_stations = 18000 * 4
finish_station= 20000
ss = 52000

total_cost = prod_to_ss + ss_to_packing + produc_stations + finish_station + ss
print("The Total Optimal Cost i: $" + str(total_cost))
