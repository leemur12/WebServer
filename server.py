from http.server import BaseHTTPRequestHandler, HTTPServer
import os
#made a small change

class TimeLapseHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type','image/jpg')
        self.end_headers()

        cur= os.getcwd()
        print(cur)

        totalImage= len(os.listdir(cur+"/testImages"))

        Files=[]
        for i in range(1, totalImage+1):
            openPath=  cur+"\\testImages" +"\\image"+str(i)+".jpg"
            #print("opening file", openPath)

            with open(openPath,"rb") as file:

                data= file.read()
                Files.append(data)

        self.wfile.write(Files)


def run(server_class= HTTPServer, handler_class= TimeLapseHandler):
    server_adress= ("", 8081)
    httpd= server_class(server_adress, handler_class)
    try:
        print("running server")
        httpd.serve_forever()

    except KeyboardInterrupt:
        print('Keyboard interrupt received: EXITING')
    finally:
        httpd.server_close()

run()
