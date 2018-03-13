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
