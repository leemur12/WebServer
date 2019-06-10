import os
import base64

cur= os.getcwd()
print(cur)


totalImage= len(os.listdir(cur+"/testImages"))


for i in range(1, totalImage+1):

    openPath=  cur+"\\testImages" +"\\image"+str(i)+".jpg"
    #print("opening file", openPath)

    with open(openPath,"rb") as file:

        data= file.read()


    openPath2= cur+ "\\returnImages" +"\\SentImage"+str(i)+".jpg"
    #print("opening file", openPath2)

    with open(openPath2, "wb+") as file:
        print("sending file"+ str(i))
        file.write(data)
