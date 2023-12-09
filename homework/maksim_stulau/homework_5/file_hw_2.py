#approach_1

result_1 = "результат операции: 42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"

ind_num_1 = result_1.index("42")
print(ind_num_1)
num_1 = result_1[20:22]
num_1 = int(num_1)
num_1 = num_1 + 10
print(num_1)

ind_num_2 = result_2.index("514")
print(ind_num_2)
num_2 = result_2[20:23]
num_2 = int(num_2)
num_2 = num_2 + 10
print(num_2)

ind_num_3 = result_3.index("9")
print(ind_num_3)
num_3 = result_3[28:29]
num_3 = int(num_3)
num_3 = num_3 + 10
print(num_3)


#approach_2

result = '"результат операции: 42", "результат операции : 514", "результат работы программы: 9"'

value_1 = result.index("42")
value_2 = result.index("514")
value_3 = result.index("9")

val_result = value_1, value_2, value_3
print(val_result)

num1 = int(result[21:23])
num2 = int(result[48:51])
num3 = int(result[83:84])

sum_1 = num1 + 10
sum_2 = num2 + 10
sum_3 = num3 + 10

print(sum_1, sum_2, sum_3)

