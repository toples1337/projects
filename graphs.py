#импортируем нужные нам библиотеки
import networkx as nx
import matplotlib.pyplot as plt
# создаём пока пустой класс с данными о графах, направлениях, и доп. атрибутах
G = nx.DiGraph()
# создаём пустой список для добавления графов
all_edges = []

def interface():
	# интерфейс
	print('Всего 6 точек: A, B, C, D, E, F\nВам необходимо ввести соединения и расстояния(от 1 до 15 соединений)\n')
	a = ''
	b = ''
	c = 0
	mark = True
	counter = 0
	while mark == True and counter < 15:
		while True:
			print('Введите первую точку:', end = ' ')
			a = input()
			a = a.upper()
			if a in 'ABCDEF':
				break
		while True:
			print('Введите вторую точку точку:', end = ' ')
			b = input()
			b = b.upper()
			if b in 'ABCDEF' and b != a:
				break
		while True:
			print('Введите расстояние между ', a, ' и ', b,': ',sep = '', end = ' ')
			c = int(input())
			if c >= 0:
				break
			else:
				print('Расстояние не может быть отрицательным')
		t = (a, b, c)
		all_edges.append(t)
		counter += 1
		print(all_edges)
		print('Ввести еще узел?(Да, Нет): ', end = '')
		mark = input()
		if mark.lower() == 'да' or mark.lower() == 'yes':
			mark = True
		else:
			mark = False
			print('От какой точки начать путь?:', end = ' ')
			while True:
				x = input()
				x = x.upper()
				if x in 'ABCDEF':
					break
				else:
					print('Нет такой вершины, введите точку еще раз:', end = ' ')
			print('До какой точки проложить путь?:', end = ' ')
			while True:
				y = input()
				y = y.upper()
				if y in 'ABCDEF':
					break
				else:
					print('Нет такой вершины, введите точку еще раз:', end = ' ')    

 #уже заданные точки
#задаём нужные нам точки и расстояния между ними
all_edges = [('A', 'B', 5), ('A', 'C', 4), ('A', 'D', 1), 
('D', 'B', 4), ('D', 'C', 2), ('D', 'E', 3), ('B', 'F', 3), ('C', 'F', 3), ('E', 'F', 4)]

x, y = 'A', 'F'  #x - начальная точка, y - конечная точка

#interface()

G.add_weighted_edges_from(all_edges)

pos = nx.circular_layout(G)
# рисуем вершины
nx.draw_networkx_nodes(G, pos, node_color='purple')
# рисуем грани
nx.draw_networkx_edges(G, pos)
# пишем названия вершин
nx.draw_networkx_labels(G, pos, font_color="whitesmoke")

# рисуем кратчайший путь
predecessors, _ = nx.floyd_warshall_predecessor_and_distance(G)
shortest_path_x_y = nx.reconstruct_path(x, y, predecessors)
edges = [(a,b) for a,b in zip(shortest_path_x_y, shortest_path_x_y[1:])]
nx.draw_networkx_edges(G, pos, edges, edge_color="g", width=2)

# рисуем расстояние между точками
weights = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, weights) 


plt.show()
