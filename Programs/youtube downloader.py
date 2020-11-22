import pytube
url =  'https://www.youtube.com/watch?v=25ovCm9jKfA'

youtube = pytube.YouTube(url)
video = youtube.streams.get_by_itag(135)
video.download('F:\Video')
print('done')