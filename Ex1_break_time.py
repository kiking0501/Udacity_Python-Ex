import time
import webbrowser

count = 0

print("This program started on "+time.ctime() )
while (count < 5):
    time.sleep(1)
    webbrowser.open("https://www.youtube.com/watch?v=IsI1GGX5Kos")
    count = count + 1

xrange
