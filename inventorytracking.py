class Footwear:
    """
      >>> f = Footwear('Sling-back', 8.5, '1234-0')
      >>> f.style
      'Sling-back'
      >>> f.size
      8.5
      >>> f.sku
      '1234-0'
      >>> f.type
      'Unspecified'
      >>> f.print_size()
      'size 8-1/2'
      >>> f2 = Footwear('Hightop', 10, '1234-19')
      >>> f2.print_size()
      'size 10'
      >>> print(f)
      Sling-back (size 8-1/2)
      >>> print(f2)
      Hightop (size 10)
    """
    def __init__(self, style, size, sku, shoetype='Unspecified'):
        self.style = style
        self.size = size
        self.sku = sku
        self.type = shoetype

    def print_size(self):
        if int(self.size) == self.size:
            return 'size {0}'.format(int(self.size))
        return 'size {0}-1/2'.format(int(self.size))

    def __str__(self):
        return '{0} ({1})'.format(self.style, self.print_size())


class Boot(Footwear):
    """
      >>> b = Boot('Hiking', 11.5, '1234-10')
      >>> print(b)
      Boot - Hiking (size 11-1/2)
    """
    def __init__(self, style, size, sku):
        Footwear.__init__(self, style, size, sku)

    def __str__(self):
        return "Boot - {0}".format(super().__str__())


class Shoe(Footwear):
    """
      >>> s = Shoe('Generic', 9.5, '1234-23')
      >>> print(s)
      Shoe - Generic (size 9-1/2)
    """
    def __init__(self, style, size, sku):
        Footwear.__init__(self, style, size, sku)
    def __str__(self):
        return "Shoe - {0}".format(super().__str__())


class DressShoe(Shoe):
    """
      >>> ds = DressShoe('Sling-back', 8.5, '1234-43')
      >>> print(ds)
      Dress Shoe - Sling-back (size 8-1/2)
    """
    def __init__(self, style, size, sku):
        Footwear.__init__(self, style, size, sku)
    def __str__(self):
        return "Dress {0}".format(super().__str__())

class CasualShoe(Shoe):
    """
      >>> cs = CasualShoe('Moccasin', 12.5, '1234-62')
      >>> print(cs)
      Casual Shoe - Moccasin (size 12-1/2)
    """
    def __init__(self, style, size, sku):
        Footwear.__init__(self, style, size, sku)
    def __str__(self):
        return "Casual {0}".format(super().__str__())


if __name__ == '__main__':
    import doctest
    doctest.testmod()

