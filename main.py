from pytube import YouTube, Playlist

video = YouTube("video-link") #substitua pelo link do vídeo que deseja baixar
print(f"Title: {video.title}")
high_res_video = video.streams.get_highest_resolution()
high_res_video.download(r'download-path') #substitua pelo caminho onde deseja baixar o arquivo


playlist = Playlist('playlist-link') #substitua pelo link da playlist que deseja baixar
for playlist_video in playlist:
    playlist_video = YouTube(playlist_video).streams.get_highest_resolution()
    print(f"Title: {playlist_video.title}")
    playlist_video.download(r"donwload-path") #substitua pelo caminho onde deseja baixar os arquivos

