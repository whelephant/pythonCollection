# import package
from pytube import YouTube

url = input("Enter the URL of your YouTube video: ")
print("processing.....")

my_video = YouTube(url)

print("***************Video Title****************")
# get video title
print(my_video.title)
print("processing.....")
# set stream resolution
my_video = my_video.streams.get_highest_resolution()
print("downloading.....")
# set download location
my_video.download('/Users/danielgao/Downloads')
print("~/Downloads")

