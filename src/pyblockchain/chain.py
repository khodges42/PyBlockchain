import block
class Chain(object):
    def __init__(self, head=None):
        self.head = block.Block()
        
    def insert(self, data):
        new_block = block.Block(prev_block=(self.head), data=data)
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
