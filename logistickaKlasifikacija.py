import math
dataSet={'n1':[1,-890],'n2':[2,-1411],'n3':[2,-1560],'n4':[3,-2220],'n5':[3,-2091],'n6':[4,-2878],'n7':[5,-3537],'n8':[6,-3268],'n9':[6,-3920],'n10':[6,-4163],'n11':[8,-5471],'n12':[10,-5157]}
global o0
o0=100
global o1
o1=200
l=0.001
def sigmoid(x):
    return 1/(1+math.exp(-x))
def hyp(x):
    return(o0+o1*x)
def minimize():
    zbir=0
    for i in dataSet:
        zbir=zbir+(hyp(dataSet[i][0])-dataSet[i][1])
    return((1/(2*len(dataSet)))*zbir)

def gradDesc(m,n):
    global o0
    global o1
    for i in range(10000):
        m=m-l*minimize()
        n=n-l*minimize()
        o0=m
        o1=n
    print(o0)
    print(o1)
gradDesc(o0,o1)
print(hyp(2))
