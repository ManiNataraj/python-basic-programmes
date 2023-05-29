X = [[12,3],[7 ,8]]

Y = [[5,8],[4,5]]

result = [[0,0],[0,0]]


for i in range(len(X)):

   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)
