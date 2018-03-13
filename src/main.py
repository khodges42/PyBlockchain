import hashlib
import datetime as date

class Block(object):
    def __init__(self,data=None, prev_block=None):
        self.data = data
        self.index = (prev_block.get_index() + 1) if prev_block else 0
        self.timestamp = date.datetime.now()
        self.prev_block = prev_block
        self.hash = self.hash_block()

    def hash_block(self):
        sha256 = hashlib.sha256()
        sha256.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.prev_block))
        return sha256.hexdigest()

    def get_blockinfo(self):
        return {"Hash": str(self.hash),
                "Index": str(self.index),
                "Timestamp": str(self.timestamp),
                "Prev_Block": str(self.prev_block.__repr__()),
                "Data_Hash": str(self.get_data_hash())}

    def __repr__(self):
        return self.hash
    
    def get_index(self):
        return self.index
    def get_data_hash(self):
        sha256 = hashlib.sha256()
        sha256.update(str(self.data))
        return sha256.hexdigest()
    
    def get_data(self):
        return self.data.get_children()

    def prev_block(self):
        return self.prev_block

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
                    
class Chain(object):
    def __init__(self, head=None):
        self.head = Block()
        
    def insert(self, data):
        new_block = Block(prev_block=(self.head), data=data)
        self.head = new_block

    def size(self):
        return self.head.get_index()
    
    def get_data(self, index = None):
        if index == None: index = self.size()
        current = self.head
        found = False
        while current and found is False:
            if current.index == index:
                found = True
            else:
                current = current.prev_block
        if current is None:
            raise ValueError("Data Not Found")
        return current.get_data()
        
    def display_hashes(self, length = None):
        current = self.head
        while current:
            print(current.hash)
            current = current.prev_block

    def search(self, hash):
        current = self.head
        found = False
        while current and found is False:
            if current.hash == data:
                found = True
            else:
                current = current.prev_hash
        if current is None:
            raise ValueError("Data Not Found")
        return current.index
    
    def get_blockinfo(self, index = None):
        if index == None: index = self.size()
        current = self.head
        found = False
        while current and found is False:
            if current.index == index:
                found = True
            else:
                current = current.prev_block
        if current is None:
            raise ValueError("Block Not Found")
        return current.get_blockinfo()

bc = Chain()
t = Tree('root', [Tree('Test'),
                  Tree('2'),
                  Tree('3', [Tree('4'),
                             Tree('OutHereMerkin')])])
bc.insert(t)
bc.insert(t)

def display_tree(t, depth=0):
    for k, v in t.iteritems():
        print ("    "*(depth)+"[{}]".format(k))
        if isinstance(v, dict) and bool(v):
            display_tree(v, depth=depth + 1)

display_tree(bc.get_data(index=1))
print(bc.head.get_blockinfo())
print(bc.get_blockinfo(index = 1))
        
