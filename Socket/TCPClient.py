from socket import *

# Vincula o socket cliente para o endereço de loopback
serverName = '127.0.0.1'

# Define a porta em que o servidor esta escutando
serverPort = 12000

# Cria um novo TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Estabelece a conexão
clientSocket.connect((serverName, serverPort))

sentence = input('Input a word to be translated: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())
clientSocket.close()
