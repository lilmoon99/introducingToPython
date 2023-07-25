# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах

# VANYA
# n = int(input())
# max_number = 1000
# while n != 0:
#  n = int(input())
#  if max_number > n:
#  max_number = n
# print(max_number)

# PETYA
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n)


n : int = int(input("Enter a number > 0: "))
def Check(n: int) -> bool:
    is_good = False
    while n > 0:
        if n % 10 == 0:
            is_good = True
            break
        n = n // 10
    return is_good

def competite(number: int) -> list:
    temp =[]
    temp.append(number)
    while not Check(number):
        number = int(input("Try again!: "))
        temp.append(number)
        if Check(number):
            print("You win")
    return temp

numbers_list = competite(n)
print(f"Max of entered numbers is: {max(numbers_list)}")