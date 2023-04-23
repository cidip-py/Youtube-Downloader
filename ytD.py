import pytube
from youtubesearchpython import VideosSearch 

# path to download the video
PATH = '/path/to/download/video'

def get_video():
    # get user input for the video to be downloaded
    link = input("Enter a video: ")
    lim = int(input("Enter a limit of videos: "))

    # search for the video on YouTube
    vidS = VideosSearch(link, limit=lim)
    results = vidS.result()["result"]
    

    # display the search results
    for i in range(len(results)):
        print(results[i]['link'])
        print(results[i]['title'])
        print(results[i]['channel']['name'])
        print(results[i]['duration'])
        url = results[i]['link']

        
    return url

def dwn_video(link):
    R = int(input("1)yes\n2)no\nDo you want to download?: "))
    if R == 1:
        try:
            # create a YouTube object for the given URL
            vd = pytube.YouTube(link)
    
            # get the highest resolution stream
            stream = vd.streams.get_highest_resolution()
    
            # download the video to the specified path
            stream.download(output_path=PATH)

            print("Downloaded successfully!")
        except Exception as e:
            print("Error: ", e)
    elif R == 0:
        print("Operation canceled")
    else:
        print("Unknown command...")

#  Channel name
def get_channel_name():
    Name = input("Enter the channel name: ")

def get_channel_videos(channel_name):
    videos = []
    channel_id = None

    # Search for the channel
    results = YoutubeSearch(channel_name, max_results=1).to_dict()
    if results:
        channel_id = results[0]['channelId']

    # If the channel was found, search for its videos
    if channel_id:
        videos = YoutubeSearch(f'channel:{channel_id}', max_results=10).to_dict()

    return videos

def print_channel_videos(channel_name):
    videos = get_channel_videos(channel_name)
    for video in videos:
        print(f"Title: {video['title']}")
        print(f"URL: {video['url']}")
# End Channel name

def Main():
    D = int(input("Search by:\n1)link/name\n2)channel\n"))
    if D == 1:
        dwn_video(get_video())
    elif D == 2:
        get_channel_videos(get_channel_name())


Main()
