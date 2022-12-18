import csv

list = ["cachorro","gato","papagaio","serpente","cobra","urso","tigre","sapo",
        "peixe","tartaruga","passaro","pardal","corvo","leão","tubarão","capivara",
        "rato","calopsita","macaco","tatu"]

list.sort(reverse=True)

for i in list:
        print(i)


with open("animais.csv", "w", newline = "") as file:
        write = csv.writer(file)
        write.writerow(list)
