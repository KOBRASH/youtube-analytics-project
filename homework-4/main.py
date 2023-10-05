# main.py
import requests

# Создаем базовый класс Video
class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.title = None  # Заголовок видео
        self.url = None    # Ссылка на видео
        self.views = 0     # Количество просмотров
        self.likes = 0     # Количество лайков
        self.get_video_info()

    # Метод для получения информации о видео из YouTube API
    def get_video_info(self):
        api_key = 'AIzaSyCmeF176p_td6JljSSx-ziWq63dZrnGdkgY'
        base_url = 'https://www.googleapis.com/youtube/v3/videos'
        params = {
            'part': 'snippet,statistics',
            'id': self.video_id,
            'key': api_key
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            if 'items' in data and len(data['items']) > 0:
                video_info = data['items'][0]
                self.title = video_info['snippet']['title']
                self.url = f'https://www.youtube.com/watch?v={self.video_id}'
                self.views = int(video_info['statistics']['viewCount'])
                self.likes = int(video_info['statistics']['likeCount'])

    def __str__(self):
        return self.title

# Создаем класс PLVideo, который наследует атрибуты и методы класса Video
class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id  # ID плейлиста

if __name__ == '__main__':
    # Создаем два экземпляра класса
    video1 = Video('AWX4JnAnjBE')
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')

    # Выводим информацию о видео
    print(f"Video 1: {video1.title}")
    print(f"Video 2: {video2.title}")
    print(f"Playlist ID для Video 2: {video2.playlist_id}")
