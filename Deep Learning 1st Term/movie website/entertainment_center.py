# coding=utf-8
import fresh_tomatoes
import media
# crash course world history
World_History = media.Movie("Crash course world history",
                            "Ten minutes course about world history.",
                            "https://i.ytimg.com/vi/Z82q-n0BgjQ/maxresdefault.jpg",
                            "https://www.youtube.com/watch?v=Yocja_N5s1I&list=PLBDA2E52FB1EF80C9")

# crash course world history
Psychology = media.Movie("Crash course psychology",
                            "Ten minutes course about psychology.",
                            "http://img4.cache.netease.com/video/2014/12/4/20141204160454d771c.jpg",
                            "https://www.youtube.com/watch?v=vo4pMVb0R6M&list=PL8dPuuaLjXtOPRKzVLY0jJY-uHOH9KVU6")

# crash course world history
Philosophy = media.Movie("Crash course Philosophy",
                            "Ten minutes course about Philosophy.",
                            "https://i.ytimg.com/vi/BNYJQaZUDrI/maxresdefault.jpg",
                            "https://www.youtube.com/watch?v=1A_CAkYt3GY&list=PL8dPuuaLjXtNgK6MZucdYldNkMybYIHKR")

# 打印对象属性
World_History.toString()
Psychology.toString()
Philosophy.toString()

# 集成对象
movies = [World_History,Psychology,Philosophy]

# 调用鲜番茄模板
fresh_tomatoes.open_movies_page(movies)
