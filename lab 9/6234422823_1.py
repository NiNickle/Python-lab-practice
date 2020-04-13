with open('vector.txt') as f :
    vector_1 = [float(vector) for vector in f.readline().strip().split()]
    vector_2 = [float(vector) for vector in f.readline().strip().split()]
if len(vector_1)!=len(vector_2) :
    print("v1 =\n"+str(vector_1)+"\nv2 =\n"+str(vector_2))
    print("Incompatible size")
else :
    print("v1 =\n"+str(vector_1)+"\nv2 =\n"+str(vector_2))
    v,vDotPro=[],0
    for i in range(len(vector_1)):
        v.append(vector_1[i]+vector_2[i])
        vDotPro=vDotPro+(vector_1[i]*vector_2[i])
    print("v1+v2 =\n"+str(v)+"\nv1*v2 ="+str(vDotPro))
