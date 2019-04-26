import requests
from bs4 import BeautifulSoup



def get_movies():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT6.1; Win64; x64)AppleWebKit/537.36 (KHTML,like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'Host': 'movie.douban.com'
    }
    movie_list = []
    ls=[]
    lm=[]
    for i in range(0,250,25):
        link = 'https://movie.douban.com/top250?start=%s'%i
        r = requests.get(link, headers=headers, timeout=10)

        soup = BeautifulSoup(r.text, "lxml")
        div_list = soup.find_all('div', class_='hd')
        div_de=soup.find_all('div',class_='bd')
        div_img=soup.find_all('div',class_='pic')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
        for   i in div_de:
              k=i.p.text

              ls.append(k)
        for i in div_img:
            k=i.a.img['src']
            lm.append(k)
    return  movie_list,ls,lm

movies,l1,l2 = get_movies()
for i in range(len(movies)):
    print(movies[i])
    print(l1[i])
    print(l2[i])