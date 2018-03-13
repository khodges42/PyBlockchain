from pyblockchain import tree, chain, block

bc = chain.Chain()
bc.insert(tree.Tree('root', [tree.Tree('Test'),
                  tree.Tree('2'),
                  tree.Tree('3', [tree.Tree('4'),
                             tree.Tree('OutHereMerkin')])]))
bc.insert(tree.Tree('root', [tree.Tree('42Test'),
                  tree.Tree('1232'),
                  tree.Tree('3', [tree.Tree('4'),
                             tree.Tree('OutHereMerkin')])]))
bc.insert("Test!")

def display_tree(t, depth=0):
    for k, v in t.iteritems():
        print ("    "*(depth)+"[{}]".format(k))
        if isinstance(v, dict) and bool(v):
            display_tree(v, depth=depth + 1)

display_tree(bc.get_data(index=1))
print(bc.head.get_blockinfo())
print(bc.get_blockinfo(index = 1))
