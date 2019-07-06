from pytube import YouTube

#stream de tn
#yt = YouTube('https://www.youtube.com/watch?v=-1xif50QMr4')
yt = YouTube('https://www.youtube.com/watch?v=IxNb1WG_Ido')

print(yt.title)
stream = yt.streams.first()
stream.download()

