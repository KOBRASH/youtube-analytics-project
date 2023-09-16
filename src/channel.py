import os
import requests
import json

class Channel:
    """Класс для ютуб-канала"""

    API_KEY = os.environ.get('YOUTUBE_API_KEY')  # Получение ключа из переменных среды

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel_data = self.get_channel_info()  # Получаем данные о канале сразу при инициализации

    @classmethod
    def get_service(cls):
        """Метод класса для получения объекта для работы с YouTube API."""
        return cls.API_KEY  # В данном случае, просто возвращаем API ключ

    def to_json(self, filename):
        """Метод для сохранения значений атрибутов экземпляра Channel в файле JSON."""
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

    def get_channel_info(self) -> dict:
        """Запрос информации о канале через YouTube API и возврат данных в виде словаря."""
        url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_id}&key={self.API_KEY}'
        response = requests.get(url)
        data = response.json()
        return data

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        if 'items' in self.channel_data:
            channel_info = self.channel_data['items'][0]
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

    # Добавим свойства (properties) для атрибутов, которые вы хотите получить через объект
    @property
    def title(self):
        return self.channel_data['items'][0]['snippet']['title']

    @property
    def video_count(self):
        return self.channel_data['items'][0]['statistics']['videoCount']

    @property
    def url(self):
        return f'https://www.youtube.com/channel/{self.channel_id}'

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        if isinstance(other, Channel):
            # Возвращает сумму числа подписчиков текущего канала и другого канала
            return int(self.channel_data['items'][0]['statistics']['subscriberCount']) + int(
                other.channel_data['items'][0]['statistics']['subscriberCount'])
        else:
            raise ValueError("Можно складывать только объекты Channel.")

    def __sub__(self, other):
        if isinstance(other, Channel):
            # Возвращает разницу числа подписчиков текущего канала и другого канала
            return int(self.channel_data['items'][0]['statistics']['subscriberCount']) - int(
                other.channel_data['items'][0]['statistics']['subscriberCount'])
        else:
            raise ValueError("Можно вычитать только объекты Channel.")

    def __eq__(self, other):
        if isinstance(other, Channel):
            # Проверяет равенство числа подписчиков текущего канала и другого канала
            return int(self.channel_data['items'][0]['statistics']['subscriberCount']) == int(
                other.channel_data['items'][0]['statistics']['subscriberCount'])
        else:
            raise ValueError("Можно сравнивать на равенство только объекты Channel.")

    def __ne__(self, other):
        if isinstance(other, Channel):
            # Проверяет неравенство числа подписчиков текущего канала и другого канала
            return int(self.channel_data['items'][0]['statistics']['subscriberCount']) != int(
                other.channel_data['items'][0]['statistics']['subscriberCount'])
        else:
            raise ValueError("Можно сравнивать на неравенство только объекты Channel.")

    def __gt__(self, other):
        if isinstance(other, Channel):
            # Проверяет, больше ли число подписчиков текущего канала, чем у другого канала
            return int(self.channel_data['items'][0]['statistics']['subscriberCount']) > int(
                other.channel_data['items'][0]['statistics']['subscriberCount'])
        else:
            raise ValueError("Можно сравнивать только объекты Channel на больше чем.")

    def __ge__(self, other):
        if isinstance(other, Channel):
            # Проверяет, больше или равно ли число подписчиков текущего канала, чем у другого канала
            return int(self.channel_data['items'][0]['statistics']['subscriberCount']) >= int(
                other.channel_data['items'][0]['statistics']['subscriberCount'])
        else:
            raise ValueError("Можно сравнивать только объекты Channel на больше или равно.")

    def __lt__(self, other):
        if isinstance(other, Channel):
            # Проверяет, меньше ли число подписчиков текущего канала, чем у другого канала
            return int(self.channel_data['items'][0]['statistics']['subscriberCount']) < int(
                other.channel_data['items'][0]['statistics']['subscriberCount'])
        else:
            raise ValueError("Можно сравнивать только объекты Channel на меньше чем.")

    def __le__(self, other):
        if isinstance(other, Channel):
            # Проверяет, меньше или равно ли число подписчиков текущего канала, чем у другого канала
            return int(self.channel_data['items'][0]['statistics']['subscriberCount']) <= int(
                other.channel_data['items'][0]['statistics']['subscriberCount'])
        else:
            raise ValueError("Можно сравнивать только объекты Channel на меньше или равно.")

if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    # получаем значения атрибутов
    print(moscowpython.title)  # MoscowPython
    print(moscowpython.video_count)  # 685 (может уже больше)
    print(moscowpython.url)  # https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A

    # менять не можем
    # moscowpython.channel_id = 'Новое название'
    # AttributeError: can't set attribute

    # можем получить объект для работы с API вне класса
    print(Channel.get_service())  # Выведет значение API ключа

    # создаем файл 'moscowpython.json' с данными по каналу
    moscowpython.to_json('moscowpython.json')
