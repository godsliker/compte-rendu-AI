class maFile:
    def __init__(self, sizemax=None):
            self.file=[]
            self.sizemax=sizemax

    def filevide(self):
                return self.file==[]


    def emfiler(self,elt):
        return self.file.insert(0,elt)


    def defiler(self):
        return self.file.pop()


    def filepleine(self):
        return self.file==self.sizemax



    def printfile(self,min=0,max=None):
        if max==None:
            max=len(self.file)
        if min<0 or min>max:
            raise ValueError("min>max")
        return list(self.file[min:max])
        