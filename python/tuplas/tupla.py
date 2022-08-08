t1 = (1,2,3,4,5,6)
t2 = ('joao',27,True,'%')
t3 = t1 + t2

print(t1,t2,t3,sep='\n')

v1, v2, *v3, v7, v8, v9, v10 = t3

print(v1,v2,v3,v7,v8,v9,v10,sep='\n')

print(t1*5)