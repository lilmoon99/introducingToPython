# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Пример:
k = 'shamsullin'
# # 12

rus_str_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
points_dict_rus = {}
points_dict_rus[1] = ['а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т']
points_dict_rus[2] = ['д', 'к', 'л', 'м', 'п', 'у']
points_dict_rus[3] = ['б', 'г', 'ё', 'ь', 'я']
points_dict_rus[4] = ['й','ы']
points_dict_rus[5] = ['ж', 'з', 'х', 'ц', 'ч']
points_dict_rus[8] = ['ш','э','ю']
points_dict_rus[10] = ['ф','щ','ъ']

points_dict_eng = {}
points_dict_eng[1] = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r']
points_dict_eng[2] = ['d','g']
points_dict_eng[3] = ['b','c','m','p']
points_dict_eng[4] = ['f','h','v','w','y']
points_dict_eng[5] = ['k']
points_dict_eng[8] = ['j','x']
points_dict_eng[10] = ['q','z']

points = [1,2,3,4,5,8,10]
def select_language(string):
    lower_string = string.lower()
    summary_of_coincidence = 0
    for i in range(len(lower_string)):
        for j in range(len(rus_str_lower)):
                if lower_string[i].__eq__(rus_str_lower[j]):
                    summary_of_coincidence += 1
                    
    if summary_of_coincidence == len(lower_string):
        return True
    else:
        return False
# hello = 'привет'

def calculate_points(string,language_dict):
    lower_string = string.lower()
    total = 0
    for i in range(len(lower_string)):
        for j in points:
            if language_dict[j].__contains__(lower_string[i]):
                total += j
                
    return total

if select_language(k):
    print(calculate_points(k,points_dict_rus))
else:
    print(calculate_points(k,points_dict_eng))