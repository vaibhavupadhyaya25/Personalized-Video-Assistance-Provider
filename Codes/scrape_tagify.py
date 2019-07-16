import bs4 as bs
from urllib.request import Request, urlopen
#import urllib.request
#user_domain = input("please enter your domain name:  ")

def func1(user_domain):

    url = "http://best-hashtags.com/hashtag/" + user_domain + "/"
    #print(url)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = bs.BeautifulSoup(webpage,'lxml')
    #print(soup.prettify())
    
    line_print = soup.find_all("p")

    target1 = soup.find("div",{"class" : "tag-box tag-box-v3 margin-bottom-40"}).text
    #print(target1)
    return target1

def func2(user_domain):
    url = "http://best-hashtags.com/hashtag/" + user_domain + "/"
    #print(url)
    send2 = []
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = bs.BeautifulSoup(webpage,'lxml')
    line_print = soup.find_all("p")
    target2 = soup.find_all("h3",{"class" : "heading-xs list-unstyled save-job"})

    #print(type(target2))
    print(soup.find("h3").text)
    print(line_print[4].text)
    for div in target2:
        print(div.text)
        send2.append(div.text)
    return send2
func1("games")
#print(send1)
#print(send2)
#target_test = soup.find_all("h3")
#print("----------------------------------")
#print(target_test[1])
#print("----------------------------------")
#print(soup.find_all("h3"))
#print("----------------------------------")
#for item in target_test:
 #      target3 = item.find("<h3>")
 #      print(target3)
#print("----------------------------------")
#target3 = target2.find("a")
#target2 = target1['id':'encyclopedia']
#print(target1)
#print(target2)
#print(target3)
#for item in target2:
 #      print(item.find("a"))
#print(target2[1].find("a").text)
#print(target2[1].find("h3"))
#print(target2[1].find("h3"))
