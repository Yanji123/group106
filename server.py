import socketserver
import hashlib
import random

class MyTCPhandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                data = self.request.recv(1024)
                if len(data) == 0:
                    break
                
                # Assuming the received data is a string representing an integer
                data = int(data.decode())

                # Generate a random seed between 2^127 and 2^128
                seed = random.randint(2**127, 2**128)

                # Calculate the SHA-256 hash of the seed
                s = hashlib.sha256(str(seed).encode()).hexdigest()

                # Calculate k (assuming "up" is defined somewhere)
                k = up - data

                # Perform k iterations of SHA-256 hashing on the seed hash 's'
                c = s
                for i in range(k - 1):
                    c = hashlib.sha256(c.encode()).hexdigest()

                # Calculate the final signature hash
                sigc = hashlib.sha256(c.encode()).hexdigest()

                # Send the seed and the signature hash back to the client
                self.request.sendall(s.encode('utf-8'))
                self.request.sendall(sigc.encode('utf-8'))

            except ConnectionResetError:
                break

        self.request.close()

if __name__ == "__main__":
    # Assuming you have a server with IP address 'server_ip' and port 'server_port'
    server_ip = "0.0.0.0"
    server_port = 12345

    # Create the server with the custom handler
    server = socketserver.TCPServer((server_ip, server_port), MyTCPhandler)

    # Start the server to listen for incoming connections
    server.serve_forever()
