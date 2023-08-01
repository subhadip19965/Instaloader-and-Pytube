from pytube import YouTube
link = input("Please paste YouTube video Link here---->")
# link = "https://youtu.be/7bDGCTnWt2Q" #You can try this song. it's very good song.
yt = YouTube(link)
inp = input("Please enter/Type - Audio, Video, Or Thumbnail--->")
if inp == "Thumbnail":
    print("If Thumbnail is requered then here is the Downloadable link ---->", yt.thumbnail_url)
elif inp == "Video":
    videos = yt.streams.filter(only_video=True)
    vid = list(enumerate(videos))
    for i in vid:
        print(i)
    print()
    strm = int(input("Enter Number You Want to Download --->"))
    videos[strm].download()
    print("Your Video File is Downloaded")
elif inp == "Audio":
    audios = yt.streams.filter(only_audio=True)
    aud = list(enumerate(audios))
    for i in aud:
        print(i)
    print()
    strm = int(input("Enter Number You Want to Download --->"))
    audios[strm].download()
    print("Your Audio File is Downloaded")