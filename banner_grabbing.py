#this code dose the banner grabbing for the web servers(port 80)
# To complete this assignment do the following steps
#create a file /my_detials.txt 
#enter your details 1) name ,2) roll no ,3) college 
#complete the code missing below
#run the server code first and then run this client code 
#Step 1) write the code for getting the IP address from the URL(using getostbyname funation)
#Step 2) write the code for cteaing the connection

import socket
#from socket import *
# code will start execution from here 
# read the remote server IP
Host = str(raw_input("Input the URL of Website: "))

try:
	#Step 1) Write code for Getting the IP addresss for the website
	host = socket.gethostbyname(Host)
	print host
except :
        print "[-] Cannot resolve '%s': Unknown host"%Host
	exit(0)



        #Step 2) create a conn socket object socket & connect calls

	#write code for creating socket object

conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.connect((host,80))

try:
	conn.send('GET HTTP/1.1 \r\n')
	ret=conn.recv(1024)
	print '[+]'+str(ret)
except Exception,e:
	print '[-] Unable to grab any information:'+ str(e)

conn.close()
