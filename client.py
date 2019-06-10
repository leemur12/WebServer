import urllib.request
import os

print("client has started")

imageFiles= urllib.request.urlopen(http://localhost:8081)

for i in range (len(imageFiles)):

    openPath2= cur+ "\\returnImages" +"\\SentImage"+str(i+1)+".jpg"
    #print("opening file", openPath2)

    with open(openPath2, "wb+") as file:
        print("sending file"+ str(i))
        file.write(imageFiles[i])
