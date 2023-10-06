import datetime

# Базовый класс, содержащий общие атрибуты и метод show_best_video()
class PlaylistBase:
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.videos = []  # Список видео в плейлисте

    def add_video(self, video):
        self.videos.append(video)

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
            duration_str = video.get('duration', '0:00:00')
            hours, minutes, seconds = map(int, duration_str.split(':'))
            video_duration = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
            total_duration += video_duration
        return total_duration

# Класс PlayList, который наследуется от PlaylistBase и DurationMixin
class PlayList(PlaylistBase, DurationMixin):
    def __init__(self, id):
        title = "Moscow Python Meetup №81"
        url = "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"
        super().__init__(title, url)

# Пример использования класса PlayList
if __name__ == '__main__':
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    # Добавим видео с информацией о длительности и лайках
    pl.add_video({'url': 'https://youtu.be/cUGyMzWQcGM', 'duration': '0:25:30', 'likes': 1000})
    pl.add_video({'url': 'https://youtu.be/abc123', 'duration': '0:30:45', 'likes': 1500})
    pl.add_video({'url': 'https://youtu.be/xyz456', 'duration': '0:20:15', 'likes': 800})

    assert pl.title == "Moscow Python Meetup №81"
    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"

    duration = pl.total_duration()
    assert str(duration) == "1:16:30"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 4590.0

    assert pl.show_best_video() == "https://youtu.be/abc123"  # Самое популярное видео
