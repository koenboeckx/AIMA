# Searching with heuristics

arad = 'Arad'
oradea = 'Oradea'
zerind = 'Zerind'
sibiu = 'Sibiu'
timisoara = 'Timisoara'
lugoj = 'Lugoj'
mehadia = 'Mehadia'
drobeta = 'Drobeta'
craiova = 'Craiova'
pitesti = 'Pitesti'
fagaras = 'Fagaras'
bucharest = 'Bucharest'
rimnicu = 'Rimnicu Vilcea'
neamt = 'Neamt'
iasi = 'Iasi'
vaslui = 'Vaslui'
urziceni = 'Urziceni'
giurgiu = 'Giurgiu'
eforie = 'Eforie'
hirsova = 'Hirsova'

romania = {	arad:		[(zerind, 75), (sibiu, 140), (timisoara, 118)],
			oradea:		[(zerind, 71), (sibiu, 151)],
			zerind:		[(arad, 75), (oradea, 71)],
			sibiu:		[(oradea, 151), (arad, 140), (fagaras, 99), (rimnicu, 80)],
			timisoara:	[(arad, 118), (lugoj, 111)],
			lugoj:		[(timisoara, 111), (mehadia, 70)],
			mehadia:	[(lugoj, 70), (drobeta, 75)],
			drobeta:	[(mehadia, 75), (craiova, 120)],
			craiova:	[(drobeta, 120), (rimnicu, 146), (pitesti, 138)],
			pitesti:	[(craiova, 138), (rimnicu, 193), (bucharest, 101)],
			fagaras:	[(sibiu, 99), (bucharest, 211)],
			bucharest:	[(giurgiu, 90), (pitesti, 101), (fagaras, 211), (urziceni, 85)],
			rimnicu:	[(sibiu, 80), (pitesti, 97), (craiova, 146)],
			neamt:		[(iasi, 87)],
			iasi:		[(neamt, 87), (vaslui, 92)],
			vaslui:		[(iasi, 92), (urziceni, 142)],
			urziceni:	[(bucharest, 85), (vaslui, 142), (hirsova, 98)],
			giurgiu:	[(bucharest, 90)],
			eforie:		[(hirsova, 86)],
			hirsova:	[(urziceni, 98), (eforie, 86)]}

sld_heuristic = {	arad:		366,
					oradea:		380,
					zerind:		374,
					sibiu:		253,
					timisoara:	329,
					lugoj:		244,
					mehadia:	241,
					drobeta:	242,
					craiova:	160,
					pitesti:	100,
					fagaras:	176,
					bucharest:	0,
					rimnicu:	193,
					neamt:		234,
					iasi:		226,
					vaslui:		199,
					urziceni:	80,
					giurgiu:	77,
					eforie:		161,
					hirsova:	151}

class Node:
	"Container class for elements of search tree."
	def __init__(self, state, parent, cost):
		self.state = state
		self.parent = parent
		self.cost = cost

def a_star_eval(node):
	"Returns evaluation as sum of current path cost and sld heuristic."
	return node.cost + sld_heuristic[node.state]

def best_first_eval(node):
	"Returns evaluation as sld heuristic."
	return sld_heuristic[node.state]
	
def expand(node, graph):
	"Returns different successor states of node."
	return graph[node.state]

def search(start, goal, evaluation):
	"""Searches for path from start to goal. Next node is chosen
	according to evalutaion fucntion. Returns final node of path."""
	frontier = [Node(state=start, parent=None, cost=0)]
	explored = []
	while len(frontier) != 0:
		node = frontier.pop(0)
		if node.state == goal: return node
		explored.append(node.state)
		for state, cost in expand(node, romania):
			if state not in explored:
				frontier.append(Node(state=state, parent=node, cost=node.cost+cost))
		frontier = sorted(frontier, key=evaluation)
	return False
		
if __name__ == '__main__':
	node = search(start=arad, goal=bucharest, evaluation=best_first_eval)
	path = [node]
	while node.parent:
		node = node.parent
		path.append(node)
		
	for node in reversed(path):
		print node.state, node.cost
