# 0 1 1 2 3 5 8 13 21 34
def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

with open('in_nums.txt','r') as file:
       line = file.read()
       incoming_numbers = line.split()
       fibo_list = []
       for k in incoming_numbers:
           last_character = k[len(k) - 1]
           fibo_number = fibo(int(last_character))
           fibo_list.append(str(fibo_number))

with open('out_nums.txt', 'w') as file:
        file.write('\n'.join(fibo_list))
        file.close()












