class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        pass
    
    def add_child(self, child):
        if child.value not in self.children:
            self.children.append(child.value)
    
    def get_children(self):
        return self.children
    
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
            return False
    return path[len(path)//2]

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