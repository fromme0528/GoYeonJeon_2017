import requests
from bs4 import BeautifulSoup
from blog.models import Video


# HTTP GET Request
req = requests.get('https://www.youtube.com/results?search_query=%EA%B3%A0%EB%A0%A4%EB%8C%80%ED%95%99%EA%B5%90+%EC%9D%91%EC%9B%90%EB%8B%A8+%EC%98%A8%EB%9D%BC%EC%9D%B8+%EC%9D%91%EC%9B%90OT')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

for tag in soup.find_all('h3', {'class': 'yt-lockup-title'}):
    for a_tag in tag.find_all('a'):
        href, title = a_tag.get('href'), a_tag.get('title')
        if 'watch' in href:
            title = title[0:-22]
            # print([href,title])
            Video.objects.create(title=title, video_url=href.replace('/watch?v=',''))

# 그냥 manage.py - shell에서 실행함