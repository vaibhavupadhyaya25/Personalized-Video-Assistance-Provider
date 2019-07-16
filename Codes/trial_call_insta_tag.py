import insta_fetch_tag_trend as ifetcher
import time

list1 = []
number = int(input("Enter list length"))
print("Enter tags")
for i in range(number):
    data = input()
    list1.append(data)
#taglist = ['terrorism', 'pakistan', 'india','pkmb']
print(list1)
#def disp(list):
#    for x in list:
#        print(x)

start = time.time()
if __name__ == "__main__":
    ifetcher.perf(list1)
end = time.time()
print(end-start)

#disp(taglist)
