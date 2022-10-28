class Union:
    def __init__(self):
        self.id = {}
        self.sz = {}
        # for islands only
        self.count = 0

    def add(self, p):
        self.id[p] = p
        self.sz[p] = 1
        # for islands only
        self.count += 1

    def root(self, i):
        # returns root of i while compressing path to root
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def unite(self, p, q):
        i, j = self.root(p), self.root(q)
        if i == j:
            return
        if self.sz[i] > self.sz[j]:
            # weighting
            i, j = j, i
        self.id[i] = j
        self.sz[j] += self.sz[i]
        # for islands only
        self.count -= 1

ds = Union()
ds.add(1)
ds.add(2)
ds.add(17)
ds.add(89)
ds.add(98)
print(ds.sz, ds.id, ds.count)
ds.unite(1, 2)
print(ds.sz, ds.id, ds.count)
ds.unite(1, 17)
# by this line, we should have 1, 2, 17 in a group
print(ds.sz, ds.id, ds.count)
        
ds.unite(89, 98)
# by this line, we should have 89, 98 in a group
print(ds.sz, ds.id, ds.count)
        
ds.unite(89, 1)
print(ds.sz, ds.id, ds.count)
print()
print(ds.id)
print(ds.sz)
print(ds.root(1) == ds.root(2))
