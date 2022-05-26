import os
import networkx as nx


os.chdir(r"D:\УЧЁБА\4 курс\Карпач\4")
#dir=r"D:\УЧЁБА\4 курс\Карпач\4"
G = nx.read_shp('roads_clip.shp').to_undirected()
#G = nx.read_shp('roads_4.shp').to_undirected() #c разными ориентировками
#nx.closeness_centrality(G) #возвращает словарь, где в качестве ключей вершины, а в качестве значений - значения центральности


#Центральность по близости
#заводим переменную для словаря
#closeness=nx.closeness_centrality(G) #словарь
#nx.set_node_attributes(G,closeness,"CC") #задаем имя атрибута в шейп файле
#nx.write_shp(G, dir)   #выгружаем полученные значения

#Центральность по степени
#dir=r"D:\УЧЁБА\4 курс\Карпач\4\DC2"
#d_c = nx.degree_centrality(G)
#nx.set_node_attributes(G, d_c, 'DC')
#nx.write_shp(G, dir)

#Центральность по промежуточности для вершин
#dir=r"D:\УЧЁБА\4 курс\Карпач\4\BC_n2"
#shn_betw_c = nx.betweenness_centrality(G)
#nx.set_node_attributes(G, shn_betw_c, 'BC_n')
#nx.write_shp(G, dir)

#Центральность по промежуточности для ребер
dir=r"D:\УЧЁБА\4 курс\Карпач\4\BC4"
she_betw_c = nx.edge_betweenness_centrality(G)
nx.set_edge_attributes(G, she_betw_c, 'BC_e')
nx.write_shp(G, dir)

#Центральность по гармонике
#dir=r"D:\УЧЁБА\4 курс\Карпач\4\HC2"
#harm_c = nx.harmonic_centrality(G)
#nx.set_node_attributes(G, harm_c, 'HC')
#nx.write_shp(G, dir)



#открываем в аргисе edges и nodes. у них колонка СС, по ней мы делаем градуированные символы
#центральность по промежуточности может расчитываться как для ребер, так и для вершин
