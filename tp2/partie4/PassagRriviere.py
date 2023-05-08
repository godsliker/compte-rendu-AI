from pile import maPile
class PassagRriviere:
    def __init__(self) -> None:
        pass
    etat=['flco;', 'flc;o', 'flo;c', 'fco;l', 'fl;co', 'fc;lo', 'fo;lc', 'f;lco',
    'lco;f', 'lc;fo', 'lo;fc', 'co;fl', 'l;fco', 'c;flo', 'o;flc', ';flco']
    etat_legal=["flco;","lo;fc","flo;c","l;fco","o;flc","flc;o","fco;l","c;flo","fc;lo",";flco"]
    arbre_etat={'flco;':['lc;fo','lo;fc','co;fl'],'flc;o':['l;fco','o;flc'],'flo;c':['l;fco','o;flc'],'fco;l':['o;flc','c;flo'],
                'fl;co':[';flco'],'fc;lo':[';flco'],'fo;lc':[';flco'],'f;lco':[';flco'],'lco;f':['flco;'],'lc;fo':['flco;','flc;o'],
                'lo;fc':['flco;','flo;c'],'co;fl':['flco;','fco;l'],'l;fco':['fl;co','flc;o','flo;c'],'c;flo':['fc;lo','flc;o', 'fco;l'],
                'o;flc':['fo;lc','flo;c','fco;l']}
    etat_explorer=[]
    fringe=maPile(15)
    def affiche(self):
        print(self.etat)
    def affichefinale(self):
        return (self.etat[-1])
    def afficheinitiale(self):
        return (self.etat[0])
    def authorise(self,etat):
        if(etat not in self.etat_legal):
            return False
        else:
            return True 
    def action(self,etats):
        return self.arbre_etat[str(etats)]
    def verif_etat(self,etat):
        if(etat in self.etat_explorer):
            return False
        else:
            return True
    def successeurs(self,etats):
        liste=[]
        for i in self.action(etats):
            if(self.authorise(i) and self.verif_etat(i) ):
                liste.append(i)
    def solution(self):
        self.fringe.empiler(self.afficheinitiale)
        while True:
            if self.fringe.pilevide():
                return 'shit'
            a=self.fringe.depiler()

            if a==self.affichefinale():
                return 'nice'
            else:
                for i in self.successeurs(a):
                    self.fringe.empiler(i)   
