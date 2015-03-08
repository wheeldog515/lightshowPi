#!/usr/bin/env python

import sys, time
from daemon import Daemon
from webapp import app,env,hc,web



class MyDaemon(Daemon):
	def run(self):
		while True: 
			hc.initialize()
    			#web.config.debug = false  #Added to stop multiple instance of classes being created
			app.run()
    			hc.clean_up()

if __name__ == "__main__":
	daemon = MyDaemon(env+'/daemon-lightshowpi.pid')
	if (len(sys.argv) == 3 or len(sys.argv) == 2) :
		if len(sys.argv) ==2:
                      sys.argv.append('80')
		if  'start' == sys.argv[1]:                    
                    del sys.argv[1:2]
	            daemon.start()
	        elif 'stop' == sys.argv[1]:
		    daemon.stop()
	        elif 'restart' == sys.argv[1]:
		    daemon.restart()
	        else:
		    print "Unknown command"
		    sys.exit(2)
		    sys.exit(0)
	else:
		print "usage: %s start|stop|restart [Optional] port (default port is 80)" % sys.argv[0]
		sys.exit(2)
