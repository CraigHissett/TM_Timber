import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import time
import os, sys
from Email import *

from tornado.options import define, options
#define("port", default=8000, help="run on the given port", type=int)
define("port", default=80, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
    
    def post (self):
        WebCommand = self.get_argument ('command', '')
        WebValue = self.get_argument ('value', '')
        
        if WebCommand == 'Pi':
            if WebValue == 'Shutdown':
                if sys.platform == 'win32':
                    os.system('shutdown /s')
                else:
                    os.system('shutdown -h now')
            elif WebValue == 'Reboot':
                if sys.platform == 'win32':
                    os.system('shutdown /r')
                else:
                    os.system('shutdown -r now')
            elif WebValue == 'Email':
                print('Send Test Email')
                SendEmail('Dustomatic - Test Email', "Triggered from Web GUI")
            else:
                print('No matching Pi Command')
                return
        else:
            print('Command not recognised')


if __name__ == "__main__":
    if sys.platform == 'win32':
        x=1
    else:
        x=2
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler)],
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates"))

    
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(options.port)
    print ("Listening on port:", options.port)
    main_loop = tornado.ioloop.IOLoop.instance()
    # Schedule event (5 seconds from now)
    #main_loop.call_later(5, UpdateIPs)
    # Start main loop
    main_loop.start()
