from itertools import chain, combinations, permutations

# return all possible permutation for a username
# exemple : ["john", "doe"] -> ("john", "doe", "johndoe", "doejohn", "john.doe", "doe.john") 
def get_permutations(self):
    self.items.append('.')
    combinations_list = list(chain(*map(lambda x: combinations(self.items, x), range(1, len(self.items) + 1))))   
    for combination in combinations_list:
        # Remove combinations that start or end by a dot
        for perm in list(permutations(combination)):
            if not perm[0] == "." and not perm[-1] == ".":
                self.permutations_list.append("".join(perm))