import hashlib

class Tree(object):
    def __init__(self, name='root', children=None, hashed=True):
        self.name = self.hashed_name(name) if hashed else name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
                
    def __repr__(self):
        return self.name
    
    def __root__(self):
        sha256 = hashlib.sha256()
        sha256.update(str(self))
        return sha256.hexdigest()
    
    def hashed_name(self, name):
        sha256 = hashlib.sha256()
        sha256.update(name)
        return sha256.hexdigest()
    
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

    def display(self):
        #print self.name
        if self.children is not None:
            for child in self.children:
                print "|"
                child.display()
    
    def get_children(self):
        children = []
        if self.children is not None:
            children = {}
            children[self.name] = {}
            for child in self.children:
                children[self.name].update(child.get_children())
        return children
