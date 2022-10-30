num = int(input("Введите количество элементов: "))
index1 = int(input("Введите индекс одного из множителей: "))
index2 = int(input("Введите индекс одного из множителей: "))
listN = [i for i in range (-num, num+1)]
mult = lambda listN,indax1,index2:listN[indax1] * listN[index2]
print(listN, 'произведение:', mult(listN,index1,index2))