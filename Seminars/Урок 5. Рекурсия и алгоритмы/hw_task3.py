# Напишите рекурсивную программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:* 
# 2+2 => 4; 
# 1+2*3 => 7; 
# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:* 
#     1+2*3 => 7; 
#     (1+2)*3 => 9;
# Тут может помочь библиотека re
import re
def compute_string(ariphm_string:str):
    numbers = re.findall(r"\d+",ariphm_string)
    operands = re.findall(r"\D",ariphm_string)
    print(numbers)
    print(operands)
    
    
ariphmetic_string = "(1+23)*3"
compute_string(ariphmetic_string)