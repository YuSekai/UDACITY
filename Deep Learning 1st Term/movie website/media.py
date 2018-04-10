# coding=utf-8
import webbrowser
class Movie():
    """ 创建movie类."""

    def __init__(self, title, movie_storyline, poster_image_url, trailer_url):
        """   
        input:title => 电影名称 
            movie_storyline => 电影简介
            poster_image_url => 电影海报链接
            trailer_url => 电影播放地址
        """
        self.title = title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url
    def toString(self):
        """打印对象的属性值"""
        print(self.title + ">>>" + self.movie_storyline + ">>>" + self.poster_image_url + ">>>" + self.trailer_url)

