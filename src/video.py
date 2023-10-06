from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.title = None
        self.url = None
        self.views = 0
        self.likes = 0
        self.get_video_info()

    def get_video_info(self):
        try:
            youtube_api = build('youtube', 'v3', developerKey='AIzaSyCmeF176p_td6JljSSx-ziWq63dZrnGdkg')
            response = youtube_api.videos().list(
                part='snippet,statistics',
                id=self.video_id
            ).execute()

            if 'items' in response and len(response['items']) > 0:
                video_info = response['items'][0]
                self.title = video_info['snippet']['title']
                self.url = f'https://www.youtube.com/watch?v={self.video_id}'
                self.views = int(video_info['statistics']['viewCount'])
                self.likes = int(video_info['statistics']['likeCount'])
        except HttpError as e:
            print(f"An error occurred: {e}")

    def __str__(self):
        return self.title

class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

if __name__ == '__main__':
    # Создаем два экземпляра класса
    video1 = Video('AWX4JnAnjBE')
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')

    # Выводим информацию о видео
    print(f"Video 1: {video1.title}")
    print(f"Video 2: {video2.title}")
    print(f"Playlist ID для Video 2: {video2.playlist_id}")
