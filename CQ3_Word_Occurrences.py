n = int(input())

Word_Count = dict()
Input_list = list()
for _ in range(n):
    word = input()
    if word in Word_Count:
        Word_Count[word] += 1
    else:
        Word_Count[word] = 1
        Input_list.append(word)
print(len(Input_list))
for i in Input_list:
    print(Word_Count[i],end=" ")