file = open("gfg.txt","r")
frequwncy_word = ""
frequency = 0
words = []
for line in file:
    line_words = line.lower().replace(",","").replace(".","").split(" ")
    for w in line_words:
        words.append(w)
for i in range(0,len(words)):
    count = 1
    for j in range(i+1,len(words)):
        if(words[i] == words[j]):
            count += 1
        if(count>frequency):
            frequency = count
            frequwncy_word = words[i]
print("most repeated words : ",frequwncy_word)
print("frequency : ",str(frequency))
file.close()