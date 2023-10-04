from src.video import Video, PLVideo

if __name__ == '__main__':
    # Создаем два экземпляра класса
    video1 = Video('AWX4JnAnjBE', 'GIL в Python: зачем он нужен и как с этим жить')
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC', 'MoscowPython Meetup 78 - вступление')
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'

    # Выводим информацию о видео
    print(f"Video 1: {video1.title}")
    print(f"Video 2: {video2.title}")
    print(f"Playlist ID for Video 2: {video2.playlist_id}")
