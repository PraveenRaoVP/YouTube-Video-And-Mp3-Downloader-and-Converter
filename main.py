import downloader,converter, pytube  
print("Welcome!")
print("What do you want to do?")
print("1.) Download YouTube videos")
print("2.) Download Youtube playlist")
print("3.) Download and convert to mp3")

choice = input("Enter choice: ")

if choice == "1" or choice == "2":
    res = input("Enter the quality(low, medium, high, very high): ")
    if choice=="2":
        link = input("Enter the link to the playlist: ")
        print("Your playlist is being downloaded...")
        downloader.download_playlist(link,res)
        print("Download completed successfully")
    if choice=="1":
        links = downloader.get_links()
        for link in links:
            print("Your video is getting downloaded...")
            downloader.download_video(link,res)
        print("Download completed successfully")

elif choice=="3":
    links = downloader.get_links()
    for link in links:
        print("The video is downloading...")
        filename = downloader.download_video(link,"low")
        print("Converting to Mp3...")
        converter.convert_mp3(filename)
else:
    print("Value Entered is invalid!!!")

