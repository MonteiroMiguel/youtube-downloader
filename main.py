from pytube import YouTube, Playlist
def download_video(video_link:str, download_path: str): # recebe o link do vídeo e o caminho onde deseja baixar o arquivo(este segundo deve ser uma raw string-> r'caminho-do=download')
    video = YouTube(video_link) # coleta as informações do vídeo
    print(f"Title: {video.title}") # exibe o título do vídeo  
    high_res_video = video.streams.get_highest_resolution() # pega o vídeo na maior resolução disponível
    high_res_video.download(download_path) # baixa o vídeo no local desejado

def download_playlist(playlist_link: str, download_path: str): # recebe o link de uma playlist em vez de um único vídeo
    playlist = Playlist(playlist_link) # coleta as informações da playlist
    for playlist_video in playlist:
        download_video(playlist_video, download_path) # faz o download de cada um dos vídeos da playlist

download_video("video-link"
               , r"download-path")
download_playlist("playlist-link"
                  , r"download-path")