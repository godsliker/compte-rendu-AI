class maPile:
    def __init__(self, sizemax=None):
            self.pile=[]
            self.sizemax=sizemax

    def pilevide(self):
                return self.pile==[]


    def empiler(self,elt):
        return self.pile.append(elt)


    def depiler(self):
        return self.pile.pop()


    def pilepleine(self):
        return self.pile==self.sizemax



    def printPile(self,min=0,max=None):
        if max==None:
            max=len(self.pile)
        if min<0 or min>max:
            raise ValueError("min>max")
        return list(self.pile[min:max])
        