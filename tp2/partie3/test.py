from heap import maHeap
h=maHeap(15)
L=[62,77,99,25,35,10,15,66,14,13,101,75]
print(L)
h.entasser(L)
print(h.extraireMIN())
print(h.printheap())