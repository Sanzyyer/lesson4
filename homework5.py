immutable_var = [123,'a',True]
print(immutable_var)
immutable_var[0]=12 #Доступ к элементам кортежа осуществляется через указание индекса,если попытаться добавить к листу другой тип данный он не получится
immutable_var[1]="b"+"1"
immutable_var[2]= False
print(immutable_var)
mutable_list = [321,4,67,31]
mutable_list[0] = mutable_list[0] - 10 
print(mutable_list)