from tkinter import *
import csv


class Node(object):
	"""docstring for Board"""
	new_id = 0

	def __init__(self, board, nb_visits, nb_wins, parent_id = None, id = None):
		super(Node, self).__init__()
		if id == None and parent_id == None:
			self.board = board
			self.nb_visits = nb_visits
			self.nb_wins = nb_wins
			self.parent = None
			self.children = []
			self.parent_id = None
			self.children_ids = []
			self.id = Node.new_id
			Node.new_id += 1
		else:
			self.board = board
			self.nb_visits = nb_visits
			self.nb_wins = nb_wins
			self.parent = None
			self.children = []
			self.parent_id = parent_id
			self.children_ids = []
			self.id = id

	@classmethod
	def tree_from_file(cls, file):
		list_nodes = []
		with open(file, mode="r", encoding="utf-8") as f:
			text = f.read().split("\n")
			for line in text:
				list_line = line.split(";")
				if list_line[3] == "None":
					node = cls(list_line[0], int(list_line[1]), int(list_line[2]), None, int(list_line[5]))
				else:
					node = cls(list_line[0], int(list_line[1]), int(list_line[2]), int(list_line[3]), int(list_line[5]))
				list_nodes.append(node)
		for node in list_nodes:
			for node2 in list_nodes:
				if node2.parent_id == node.id:
					node.add_child(node2)
		return list_nodes[0]
				

	def add_child(self, child):
		child.parent = self
		self.children.append(child)
		child.parent_id = self.id
		self.children_ids.append(child.id)
		
	def get_level(self):
		level = 0
		p = self.parent
		while p:
			level += 1
			p = p.parent
		return level

	def to_string(self):
		res = self.board + ";" + str(self.nb_visits) + ";" + str(self.nb_wins) + ";" + str(self.parent_id) + ";" + "".join(str(self.children_ids)) + ";" + str(self.id)
		if self.children:
			for child in self.children:
				res += "\n" + child.to_string()
		return res

	def to_file(self, file):
		with open (file, mode="w", encoding="utf-8") as f:
			f.write(self.to_string())

if __name__ == '__main__':
	a = Node("000000000", 1, 0)
	b = Node("00000000X", 4, 1)
	c = Node("00000000X", 4, 1)
	a.add_child(b)
	a.add_child(c)

	a.to_file("board.txt")

	d = Node("000000000", 1, 0)

	e = Node.tree_from_file("board.txt")
	print(e.to_string())
	







#tkinter
"""
def print_board(board):
	return '\n'.join(' '.join(map(str,sl)) for sl in board)

window = Tk()

label = Label(window, text=print_board(starting_board()))
label.pack()

window.mainloop()
"""