import csv
def read_csv():
    with open('hashtag_list.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        tags = []
        posts = []
        freqs = []
        sum1 = 0
        line_count = 0
        i = 0
        for row in readCSV:
            if line_count == 0:
                line_count+=1
            else:
                line_count+=1
                tag = row[1]
                post = row[2]
                freq = row[3]

                tags.append(tag)
                posts.append(post)
                freqs.append(freq)

        print(type(tags))
        print(type(posts))
        print(type(freqs))
        for i in range(line_count-1):
            string1 = posts[i]
            string1 = string1.replace(',', '')
            a = int(string1)
            string2 = freqs[i]
            string2 = string2.replace(',', '')
            b = int(string2)
            if b==0:
                b=1
            c = (b/a)*100
            print(c)
            sum1 = sum1 + c
        sum1 = sum1/(line_count-1)
        return sum1
a = read_csv()
print(a)
        
