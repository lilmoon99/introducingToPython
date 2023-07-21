# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

dictionary = {"V": "S001", "V": "S002", "VI": "S001","VI": "S005", "VII": " S005 ", " V ":" S009 "," VIII":" S007 "}

print(dictionary)
sp = []



for values in dictionary.values():
    temp = values.strip()
    if temp not in sp:
        sp.append(temp)
        
print(sp)


