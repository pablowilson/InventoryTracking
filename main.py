import random
import json
from footwear import Boot, DressShoe, CasualShoe


def make_catalog(n):
    styles = (("Cowboy", "Hiking", "Rain", "Riding"),
              ("Loafer", "Oxford", "Pump", "Sling-back", "Wing-tip"),
              ("Athletic", "Hightop", "Moccasin", "Sandal"))

    sizes = (5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5,
             12, 12.5, 13, 13.5, 14)

    catalog = []

    for i in range(n):
        fwtype = random.randint(0, len(styles)-1)
        style = random.choice(styles[fwtype])
        size = random.choice(sizes)
        sku = "1234-" + str(i)

        if fwtype == 0:
            catalog.append(Boot(style, size, sku))
        elif fwtype == 1:
            catalog.append(DressShoe(style, size, sku))
        else:
            catalog.append(CasualShoe(style, size, sku))

    return catalog


def get_catalog(fname):
    """Read catalog from json encoded fname file."""
    f = open(fname, "r")
    cat = json.loads(f.read())
    f.close()
    return json.dumps(cat)


def save_catalog(catalog, fname):
    """Write catalog to json encoded fname file."""
    f = open(fname, "w")
    catalog = [item.__dict__ for item in catalog]
    f.write(json.dumps(catalog))
    f.close()


def __eq__(self, other):
    """for j, k in self, other:"""

    return self.type == other.type and self.style == other.style and self.size == other.size and self.sku == other.sku
    """ONLY COMPARES FIRST SHOE, NEED A LOOP OR SMTHG TO COMPARE ALL"""

if __name__ == '__main__':
    import doctest
    doctest.testfile("warehouse_tests.txt")
