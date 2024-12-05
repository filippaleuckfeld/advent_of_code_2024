class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parents = []
        pass
    
    def add_child(self, child):
        if child.value not in self.children:
            self.children.append(child.value)
            child.add_parent(self)
    
    def get_children(self):
        return self.children

    def add_parent(self, parent):
        if parent.value not in self.parents:
            self.parents.append(parent.value)

def parse_input(rows):
    pages = []
    tree_dict = {}
    pages_flag = False
    for elem in rows:
        if elem == '':
            pages_flag = True
            continue
        if not pages_flag:
            rule = elem.split("|")
            if rule[0] not in tree_dict:
                parent = Node(rule[0])
                tree_dict[rule[0]] = parent
            else:
                parent = tree_dict[rule[0]]
            if rule[1] not in tree_dict:
                child = Node(rule[1])
                tree_dict[rule[1]] = child
            else:
                child = tree_dict[rule[1]]
            parent.add_child(child)
        else:
            pages.append(elem.split(","))
    return tree_dict, pages
    
def check_path(tree, path):
    for index in range(len(path)-1):
        current_node = tree[path[index]]
        current_node_children = current_node.get_children()
        if path[index+1] in current_node_children:
            continue
        else:
            sorted_path = sort_path(tree, path)
            return sorted_path[len(path)//2]
    
    return False

def switch_places(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]

def sort_path(tree, path):
    sorted = 0
    
    while True:
        for index in range (len(path)-1):
            if path[index+1] in tree[path[index]].children:
                sorted += 1
                if sorted == len(path)-1:
                    return path
            else:
                if path[index+1] in tree[path[index]].parents:
                    switch_places(path, index, index+1)
        sorted = 0

def main():
    with open("input.txt", 'r') as file:
        rows = [row.strip() for row in file]

    tree_dict, pages = parse_input(rows)

    total = 0
    for path in pages:
        total += int(check_path(tree_dict, path))
        
    print(total)
    
        
if __name__ == "__main__":
    main()