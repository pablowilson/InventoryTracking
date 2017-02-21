class BinItem:
    """A warehouse bin item consisting of a sku number and quantity."""
    def __init__(self, sku, quantity):
        self.sku = sku
        self.quantity = quantity

    def __str__(self):
        return "SKU {0}: {1}".format(self.sku, self.quantity)


class Bin:
    """A location for storing BinItems."""
    def __init__(self, name):
        self.name = name
        self.contents = []

    def __str__(self):
        s = "Bin {0}:".format(self.name)
        for item in self.contents:
            s += '\n  ' + item.__str__()
        return s
class Warehouse:
    """a location for storing Bins"""
    def __init__(self, name):
        self.name = name
        self.bis = []
    
    def addbi(self, bi):
        self.bis.append(bi)

    def rmbi(self, bi):
        self.bis.remove(bi.name)
        
    def add(self, bi, item):
        for index, value in enumerate(bi.contents):
            if value.sku == item.sku:
                value.quantity += item.quantity
                break
            if value.sku < item.sku:
                continue
            else:
                bi.contents.insert(index, item)
                break
        else:
            bi.contents.append(item)
            a_bin,

    def sell(bi, item):
        for index, amount in enumerate(bi.contents):
            if amount.sku == item.sku:
                if amount.quantity - item.quantity == 0:
                    bi.contents.remove(amount)
                    break
                else:
                    bi.contents.remove(amount)
                    bi.add(BinItem(item.sku, amount.quantity - item.quantity))
                    break
                
if __name__ == '__main__':
    import doctest
    doctest.testfile("bin_tests.txt")
