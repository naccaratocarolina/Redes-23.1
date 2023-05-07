from socket import *

# Define o nome ou endereco IP do servidor
serverName = '127.0.0.1'

# Define a porta em que o servidor esta escutando
serverPort = 12000

# Cria um novo UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Recebe a mensagem do usuario
message = input('Input a word to be translated: ')

# Envia a mensagem para o endereco IP e porta do servidor
clientSocket.sendto(message.encode(),(serverName, serverPort))

# Recebe a mensagem modificada e o endereco do servidor que enviou a mensagem
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Imprime a mensagem modificada recebida do servidor
print(modifiedMessage.decode())

# Fecha a conexão socket do cliente
clientSocket.close()