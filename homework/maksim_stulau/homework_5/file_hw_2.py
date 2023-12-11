result_1 = "результат операции: 42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"

ind_num_1 = result_1.index(':') + 2
ind_num_2 = result_2.index(':') + 2
ind_num_3 = result_3.index(':') + 2

num_1 = int(result_1[ind_num_1:]) + 10
num_2 = int(result_2[ind_num_2:]) + 10
num_3 = int(result_3[ind_num_3:]) + 10

print(num_1, num_2, num_3, sep='\n')
