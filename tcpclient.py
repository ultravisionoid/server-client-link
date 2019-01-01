import socket
def main():
	host = '127.0.0.1'
	port = 5000
	s=socket.socket()
	s.connect((host,port))
	message=input("->")
	while message!='q':
		d=message.encode('ASCII')
		s.send(d)
		data=s.recv(1024)
		print( "recieved from server "+ str(data))
		message=input('->')
	s.close()
if __name__ == '__main__':
	main()		