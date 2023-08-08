# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows=5, num_columns=5):
    columns_list = [item + 1 for item in range(num_columns)]
    row_list = [item + 1 for item in range(num_rows)]
    table = []
    if num_rows >= num_columns:
        for i in range(num_rows):
            row_list = [1*i+1 for item in row_list]
            table.append((list(map(operation,row_list,columns_list))))
    else:
        for i in range(num_columns):
            columns_list = [1*i+1 for item in columns_list]
            table.append((list(map(operation,row_list,columns_list))))
            
    for i in table:
        print(*[f"{x:>5}" for x in i])

    # print(list(map(operation(num_rows,num_columns),row_list)))

    # for i in range(1,num_columns):
    
print_operation_table(lambda x,y: x*y)
