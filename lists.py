#given_list = [7, 5, 4, 3, -1, -2, -3, -5]
marks = [60, 44, 91, 72, 93]
odd_mark = [mark for mark in marks if mark % 2 != 0]
print(odd_mark)
#total = 0
#total2 = 0
#i = 0
#total3 = 0
#for i in given_list:
 #   if i < 0:
  #      total += i
   #     i += i
#print(total)       

#while given_list[i] > 0:
 #   total2 += given_list[i]
  #  i += 1
#print(total2) 

#for i in given_list:
   # if i <= 0:
  #      break
 #   total3 += i
#print(total3)

##while True:
  #  total3 += given_list[i]
   # i += 1
   # if given_list[i] <= 0:
    #    break
#print(total3)

#total3 = 0
#j = len(given_list) - 1
#while given_list[j] < 0:
 #   total3 += given_list[j]
  #  j -= 1
#print(total3)


def process_data(data):
    result = ""
    for item in data:
        if isinstance(item, int) and item % 2 == 0:
            result += str(item * 2) + "-"
        elif isinstance(item, str) and len(item) > 3:
            result += item[:3].upper() + "-"
        else:
            result += "X-"
    return result

data_list = ["apple", 3, "cat", 4,7, "banana", 10, "dog", 6]
output = process_data(data_list)
print(output)