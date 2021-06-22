import re

string1 = input ("Введите ряд символов : ")
print ("Ваши данные: " + string1) 
numbers = re.findall(r"\d+", string1)
numbers=[int(i) for i in numbers] 
string1=re.findall("\D", string1)
string2="".join(string1)
print("Числа : " , numbers)
print ('Ряд без чисел : ', string2)
def capitalize(string2):
     string2, result = string2.title(), ""
     for word in string2.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]     
print ("Слова с заглавными буквами : ", capitalize(string2)) 
max_num=max(numbers)
print("Макс.Число : ", max_num) 
numbers_index = []
for i in range(len(numbers)):
            x=numbers[i]
            if(x!= max_num):
                numbers_index.append(x**i)
            else:
                continue
print ("Степени числа: ", numbers_index) 
