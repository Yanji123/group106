import socket
import hashlib

def generate_proof(p, d):
    for i in range(d - 1):
        p = hashlib.sha256(p.encode()).hexdigest()
    return p

if __name__ == "__main__":
    server_ip = "localhost"  # Assuming the server is running on the same machine
    server_port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    while True:
        sdata = input('请输入出生年份：')
        client.send(sdata.encode('utf-8'))
        s = client.recv(1024).decode()
        print('从服务器收到种子：', s)
        sigc = client.recv(1024).decode()
        print('从服务器收到签名哈希：', sigc)

        d = int(input("请输入要验证的出生年份："))
        d1 = d - int(sdata)
        p = generate_proof(s, d1)

        c = p
        d2 = 2100 - d
        for i in range(d2 - 1):
            c = hashlib.sha256(c.encode()).hexdigest()

        sig = hashlib.sha256(c.encode()).hexdigest()
        if sig == sigc:
            print("Bob检验结果：", True)
        else:
            print("Bob检验结果：", False)

        client.close()
