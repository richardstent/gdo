import SocketServer
import time

if __name__ == '__main__':
    import socket

# Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 7654
    serverhost = "192.168.1.252"
    s.connect((serverhost, port))
#    print 'Connected to Server on %s: %d' serverhost, port

    # Send the data
    message = 'Toggle'
    print 'Sending : "%s"' % message
    len_sent = s.send(message)
    
    print 'Sleeping for 1 second'
    time.sleep(1)
    print 'Cleaning Up'
    
    # Clean up
    print 'Closing Socket'
    s.close()
    print('Exiting')