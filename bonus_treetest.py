#encoding: utf-8
#import bonus_bintree2_parents as bintree
import bonus_bintree2_parents2 as bintree

def testZeroToEight():
    tree = bintree.Bintree()
    assert(tree.height() == 0)     # bör ge 0
    assert(tree.isempty() == True)    # bör ge True

    for i in range(0, 8):
        tree.put(i)
        
    tree.printtree()               # skriv ut sorterat
    print("tree.height():", tree.height())           # ska ge 6 om insättningarna gjorts exakt enligt ovan
    print()

    print()
    tree.printtree()               # skriv ut sorterat
    print(tree.height())           # ska ge 6 om insättningarna gjorts exakt enligt ovan
    
def testRandom():
    import random
    tree = bintree.Bintree()
    assert(tree.height() == 0)     # bör ge 0
    assert(tree.isempty() == True)    # bör ge True
    
    seq = list(range(10))
    random.shuffle(seq)
    print("seq:", seq)
    for val in seq:
        tree.put(val)

    print("Before deleting value 4:")
    tree.printtree()
    tree.printtreewidthfirst()
    tree.deletevalue(4)
    print("After deleting value 4:")
    tree.printtree()
    tree.printtreewidthfirst()
    tree.deletevalue(8)
    print("After deleting value 8:")
    tree.printtree()
    tree.printtreewidthfirst()
    tree.deletevalue(6)
    print("After deleting value 6:")
    tree.printtree()
    tree.printtreewidthfirst()
if __name__ == "__main__":
    #testZeroToEight()
    testRandom()
