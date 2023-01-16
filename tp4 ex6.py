liste=[5,2,4,8,1,3]
n= len(liste)
for i in range(n):
    for j in range (n-i-1):
        if liste[j] > liste[j+1]:
         liste[j], = liste[j+1] = liste[j+1]
         print(liste)


         print("autre methode)")

         liste = []
         for i in range(N):
             liste.append(random.randint(0, 100))
         print(sorted(liste))