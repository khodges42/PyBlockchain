import hashlib
import json

class Radix_Tree(object):
    def __init__(self, name='root', children=None, hashed=True):
        if children is not None:
            self.children = self.add_child(self.hash_children(children)) if hashed else self.add_child(children)

    def hash_children(self, children, _tlist = []):
        for child in children:
            _tlist.append(self.hash_item(child))
        return _tlist

    def hash_item(self, item):
        sha256 = hashlib.sha256()
        sha256.update(item)
        return sha256.hexdigest()
    
    def add_child(self, nodes):
        return self._recurse_trie(nodes)

    def _recurse_trie(self, nodes, root = {}):
        for itm in nodes:
            cur_root = root
            for byte in itm:
                cur_root = cur_root.setdefault(byte, {})
            cur_root['___'] = '___'
        return root

    def display(self):
        data = json.dumps(self.children, sort_keys=True)
        print data

    def is_in(self, item):
        cur_root = self.children
        for byte in item:
            if byte in cur_root:
                cur_root = cur_root[byte]
            else:
                return False
        return True if '___' in cur_root else False
