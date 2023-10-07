import datetime
from googleapiclient.discovery import build


# Базовый класс, содержащий общие атрибуты и метод show_best_video()
class PlaylistBase:
    def __init__(self, playlist_id, api_key):
        self.playlist_id = playlist_id
        self.api_key = api_key
        self.videos = self._get_playlist_videos()

    def _get_playlist_videos(self):

        youtube_service = build('youtube', 'v3', developerKey=self.api_key)

        # Запрос информации о видео в плейлисте
        playlist_videos = youtube_service.playlistItems().list(
            playlistId=self.playlist_id,
            part='contentDetails',
            maxResults=50,
        ).execute()

        # Получите все ID видеороликов из плейлиста
        video_ids = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        # Получите данные по каждому видео
        video_response = youtube_service.videos().list(
            part='contentDetails,statistics',
            id=','.join(video_ids)
        ).execute()

        videos = []
        for video_item in video_response.get('items', []):
            video = {
                'url': f'https://www.youtube.com/watch?v={video_item["id"]}',
                'duration': video_item['contentDetails']['duration'],
                'likes': int(video_item['statistics']['likeCount'])
            }
            videos.append(video)

        return videos

    def show_best_video(self):
        if not self.videos:
            return None

        # Найдем видео с наибольшим количеством лайков
        best_video = max(self.videos, key=lambda video: video['likes'])
        return best_video['url']


# Миксин для вычисления суммарной длительности
class DurationMixin:
    def total_duration(self):
        total_duration = datetime.timedelta()
        for video in self.videos:
            duration_str = video.get('duration', 'PT0S')  # PT0S - длительность по умолчанию (0 секунд)
            duration = datetime.datetime.strptime(duration_str, "PT%HH%MM%SS")
            total_duration += datetime.timedelta(
                hours=duration.hour,
                minutes=duration.minute,
                seconds=duration.second
            )
        return total_duration


# Класс PlayList, который наследуется от PlaylistBase и DurationMixin
class PlayList(PlaylistBase, DurationMixin):
    def __init__(self, playlist_id, api_key):
        super().__init__(playlist_id, api_key)


# Пример использования класса PlayList
if __name__ == '__main__':
    playlist_id = 'PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw'
    api_key = 'AIzaSyCmeF176p_td6JljSSx-ziWq63dZrnGdkg'

    pl = PlayList(playlist_id, api_key)

    print(f"Best Video URL: {pl.show_best_video()}")  # Самое популярное видео
    print(f"Total Duration: {pl.total_duration()}")
