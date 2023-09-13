import os
import requests

class Channel:
    """Класс для ютуб-канала"""

    API_KEY = os.environ.get('YOUTUBE_API_KEY')  # Получение ключа из переменных среды

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def get_channel_info(self) -> dict:
        """Запрос информации о канале через YouTube API и возврат данных в виде словаря."""
        url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_id}&key={self.API_KEY}'
        response = requests.get(url)
        data = response.json()
        return data

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        data = self.get_channel_info()
        if 'items' in data:
            channel_info = data['items'][0]
            snippet = channel_info['snippet']
            statistics = channel_info['statistics']
            print("Channel Name:", snippet['title'])
            print("Description:", snippet['description'])
            print("Published At:", snippet['publishedAt'])
            print("View Count:", statistics['viewCount'])
            print("Subscriber Count:", statistics['subscriberCount'])
            print("Video Count:", statistics['videoCount'])
        else:
            print("Channel not found or API key is invalid.")

if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    moscowpython.print_info()
