from socket import *

# Define o nome ou endereco IP do servidor
serverName = '127.0.0.1'

# Define a porta em que o servidor esta escutando
serverPort = 12000

# Cria um novo TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Estabelece a conexão
clientSocket.connect((serverName, serverPort))

# Recebe a mensagem do usuario
sentence = input('Input a word to be translated: ')

# Envia a mensagem para o servidor
clientSocket.send(sentence.encode())

# Recebe a mensagem modificada enviada pelo servidor
modifiedSentence = clientSocket.recv(1024)

# Imprime a mensagem modificada recebida do servidor
print('From Server: ', modifiedSentence.decode())

# Fecha o socket do cliente
clientSocket.close()