class Video:
    def __init__(self, video_id, title=None, url=None, views=0, likes=0):
        self.video_id = video_id
        self.title = title
        self.url = url
        self.views = views
        self.likes = likes

    def __str__(self):
        return self.title

class PLVideo(Video):
    def __init__(self, video_id, playlist_id, title=None, url=None, views=0, likes=0):
        super().__init__(video_id, title, url, views, likes)
        self.playlist_id = playlist_id
