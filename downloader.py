import pytube

def download_video(url,resolution):
    myTag=choose_resolution(resolution)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(myTag)
    stream.download()
    return stream.default_filename

def download_multiple_videos(urls,resolution):
    for i in urls:
        download_video(i,resolution)

def download_playlist(url,resolution):
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls,resolution)

def choose_resolution(resolution):
    if resolution in ["low","360","360p"]:
        myTag = 18
    elif resolution in ["medium","720","720p","hd"]:
        myTag = 22
    elif resolution in ["high","1080","1080p","fullhd", "full_hd", "full hd"]:
        myTag = 137 
    elif resolution in ["very high","2160","2160p","4K","4k"]:
        myTag = 313 
    else:
        myTag = 18
    return myTag

def get_links():
    print("Enter the links of the videos:(end by entering STOP): ")
    links = []
    link = ""
    while(link.upper()!="STOP"):
        link = input()
        links.append(link)

    links.pop()
    return links
