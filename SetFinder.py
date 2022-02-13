class SetFinder:

	#initialize field variables
	def __init__(self):
		self.card_list = []

	#receives input from standard in and parses it into a 2-d array where each element represents a card,
	#and each card with 4 elements, each representing an attribute
	def input(self):
		line_count = input()

		for i in range(int(line_count)):
			curr_card = input().split()
			card = []

			if curr_card[0] == "blue":
				card.append("blue")
			elif curr_card[0] == "yellow":
				card.append("yellow")
			else:
				card.append("green")

			if curr_card[1][0] == "a" or curr_card[1][0] == "A" or curr_card[1][0] == "@":
				card.append("A")
			elif curr_card[1][0] == "s" or curr_card[1][0] == "S" or curr_card[1][0] == "$":
				card.append("S")
			else:
				card.append("H")

			if curr_card[1][0] == "a" or curr_card[1][0] == "s" or curr_card[1][0] == "h":
				card.append("lower")
			elif curr_card[1][0] == "A" or curr_card[1][0] == "S" or curr_card[1][0] == "H":
				card.append("upper")
			else:
				card.append("symbol")

			card.append(len(curr_card[1]))

			self.card_list.append(card)

	#outputting function that calls the set-finding functions
	def find_sets(self):
		self.input()

		sets = self.find_all_sets()
		print(len(sets))

		disjoint_sets = self.find_disjoint_sets(sets)
		max_set = max(disjoint_sets, key = len)
		print(len(max_set))

		for curr_set in max_set:
			curr_set.sort()
			print()
			for card in curr_set:
				print(self.convert_to_card(card))
		
	#helper function to convert card array form back into its original card form
	def convert_to_card(self, card):
		str_card = card[0] + " "

		if card[1] == "A":
			if card[2] == "lower":
				str_card += "a" * card[3]
			elif card[2] == "upper":
				str_card += "A" * card[3]
			else:
				str_card += "@" * card[3]
		elif card[1] == "S":
			if card[2] == "lower":
				str_card += "s" * card[3]
			elif card[2] == "upper":
				str_card += "S" * card[3]
			else:
				str_card += "$" * card[3]
		else:
			if card[2] == "lower":
				str_card += "h" * card[3]
			elif card[2] == "upper":
				str_card += "H" * card[3]
			else:
				str_card += "#" * card[3]
		
		return str_card

	#function finds all possible sets that can be made
	def find_all_sets(self):
		sets = []

		for i in range(len(self.card_list) - 2):
			for j in range(i + 1, len(self.card_list) - 1):
				for k in range(j + 1, len(self.card_list)):
					if self.are_set(self.card_list[i], self.card_list[j], self.card_list[k]):
						sets.append([self.card_list[i], self.card_list[j], self.card_list[k]])

		return sets

	#function recursively searches for all possible combinations of disjoint sets
	def find_disjoint_sets(self, sets):
		disjoint_combos = []

		if len(sets) == 0:
			return [[]]

		for this_set in sets:
			paths = self.find_disjoint_sets(self.remove_dupe_sets(this_set, sets))
			for path in paths:
				path.insert(0, this_set)
			disjoint_combos += paths

		return disjoint_combos

	#helper function to find_disjoint_sets() to remove all sets that contain cards already used
	def remove_dupe_sets(self, this_set, sets):
		no_dupes = []

		for other_set in sets:
			if not (other_set[0] == this_set[0] or other_set[0] == this_set[1] or other_set[0] == this_set[2]
			or other_set[1] == this_set[0] or other_set[1] == this_set[1] or other_set[1] == this_set[2]
			or other_set[2] == this_set[0] or other_set[2] == this_set[1] or other_set[2] == this_set[2]):
				no_dupes.append(other_set)

		return no_dupes

	#checks if the attributes of three cards are all the same
	def all_same(self, att1, att2, att3):
		if att1 == att2 and att2 == att3:
			return True
		else:
			return False

	#checks if the attributes of three cards are all different 
	def all_different(self, att1, att2, att3):
		if att1 != att2 and att2 != att3 and att1 != att3:
			return True
		else:
			return False

	#check if three cards make up a set
	def are_set(self, card1, card2, card3):
		for i in range(4):
			if self.all_same(card1[i], card2[i], card3[i]) or self.all_different(card1[i], card2[i], card3[i]):
				continue
			else:
				return False

		return True

sf = SetFinder()
sf.find_sets()




























