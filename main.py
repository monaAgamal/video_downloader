import os
from pytube import Playlist
playlists = [
    # Playlist("https://www.youtube.com/playlist?list=PL612CE2AB6F38DF9A"),
    Playlist("https://www.youtube.com/playlist?list=PLBD4C7FD29B0C6D0C"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJQNjkHZgwuAlfQ9tzmQDxjA"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJQWowhOG0-K-yI-bwRRmm3C"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJSMghTc2Qu0tk-lwY4ui7iY"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJRtXgdjQkYfYOHfsc-7Ar7Q"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJQqGHrpAloTec_lOKsG-foc"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJQ2vsW_hmyvVfO4GYWaaPp7"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJS1F-yeDwn16nsuYrpSYzaO"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJTmKzaSlCpGgi7qxgcRRs8h"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJSpZNZyDAzMm91RbCQRd2rK"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJQe0_9YJlN9S7ktkA8DI-fL"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJRa3VKt_eyZdJ_DitCz1cvQ"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJSUpKllt0btml02Zsc9U1VU"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJSssxplPGgKHZLgdzL5-O88"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJQFYY1KXNd2OBEnJgiyXDZf"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJR_EJRzVJ7R9u16crBaAWZd"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJRY7X-tMNDHPGdmfZyfHC7J"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJSNQjPsqYnPFfroE1coxysA"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJSmVwf28pEbVjwUVIf6eyKu"),
    Playlist(
        "https://www.youtube.com/playlist?list=PLbMVogVj5nJTEKLskRzwSJeD4KqXIWAbu"),
]

for playlist in playlists:
    print(f'Downloading: {playlist.title}')
    playListPath = rf'D:\downloades_from_py\{playlist.title}'
    if not os.path.exists(playListPath):
        os.makedirs(playListPath)
    for video in playlist.videos:
        print(video.title)
        st = video.streams.get_highest_resolution()
        st.download(output_path=f"{playListPath}")