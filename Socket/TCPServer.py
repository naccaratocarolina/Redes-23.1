from socket import *

# Inicializa servidor na porta 12000
serverPort = 12000

# Cria um novo TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Vincula o socket do servidor ao endereço de loopback
serverSocket.bind(('', serverPort))

# Prepara o servidor para receber requisicoes
serverSocket.listen(1)
print('The server is ready to receive')

# Dicionario de palavras
networkDict = {
  'router': 'roteador',
  'switch': 'comutador',
  'gateway': 'porta de entrada',
  'protocol': 'protocolo',
  'bandwidth': 'largura de banda',
  'IP address': 'endereço IP',
  'subnet mask': 'máscara de sub-rede',
  'MAC address': 'endereço MAC',
  'packet': 'pacote',
  'port forwarding': 'encaminhamento de porta'
}

def translate(dic, word):
  for key, value in dic.items():
    if (key == word.lower()):
      return value
  return 'Word not found'

while True:
  connectionSocket, addr = serverSocket.accept()

  # Palavra recebida do cliente
  sentence = connectionSocket.recv(1024).decode()

  # Traducao da palavra baseado no dicionario
  translated = translate(networkDict, sentence)
  connectionSocket.send(translated.encode())
  connectionSocket.close()