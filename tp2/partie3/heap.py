class maHeap:
    def __init__(self, sizemax=None):
            self.Heap=[]
            self.sizemax=sizemax
    def extraireMIN(self):
        return self.Heap[0]
    def entasser(self,L):
        while L:
            self.Heap.append(min(L))
            L.remove(min(L))
    def printheap(self,min=0,max=None):
        if max==None:
            max=len(self.Heap)
        if min<0 or min>max:
            raise ValueError("min>max")
        return list(self.Heap[min:max])