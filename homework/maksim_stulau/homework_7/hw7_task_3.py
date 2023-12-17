result_1 = "результат операции: 42"
result_2 = "результат операции: 54"
result_3 = "результат работы программы: 209"
result_4 = "результат: 2"


def num_sum(result):

    ind_num = result.index(":") + 2
    num = int(result[ind_num:]) + 10
    print(result[:ind_num] + str(num))


num_sum(result_1)
num_sum(result_2)
num_sum(result_3)
num_sum(result_4)
