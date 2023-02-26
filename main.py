import numpy as np
print("Topic: Copy")
var = np.array([1,2,3,4])
co = var.copy()
print("var : ",var)
print("copy :",co)

print()
print("Topic: view")
x = np.array([2,3,4,5,6])
vi = x.view()
print("x : ",x)
print("view :",vi)



