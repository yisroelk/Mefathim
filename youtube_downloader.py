from pytube import YouTube 

# where to save 
SAVE_PATH = "/Users/yisroel/Downloads" #to_do 

# link of the video to be downloaded 
link = "https://www.youtube.com/watch?v=cCrsBYSae5Q"

try: 
    # object creation using YouTube 
    yt = YouTube(link) 
except: 
    #to handle exception 
    print("Connection Error") 

# Get all streams and filter for progressive files
mp4_streams = yt.streams.filter(progressive=True).all()
# get the video with the highest resolution
print(mp4_streams)
d_video = mp4_streams[-1]

try: 
    # downloading the video 
    d_video.download(output_path=SAVE_PATH)
    print('Video downloaded successfully!')
except: 
    print("Some Error!")





def count_what(a, b, n):
    i = 0
    j = 0
    s = 0
    while i < n and j < n:
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            s += 1
            i += 1
            j += 1
    return s

# קריאה לדוגמה לפונקציה עם הרשימות והערך n הרצוי
a = [8,7,2,14,5,17,6]
b = [3,4,2,1,8,9,10]
n = len(a)  # מספר האיברים ברשימות
result = count_what(a, b, n)
print(result)  # תדפיס את התוצאה