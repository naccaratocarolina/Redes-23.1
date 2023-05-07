from socket import *

# Inicializa servidor na porta 12000
serverPort = 12000

# Cria o socket do servidor com protocolo TCP
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
  'port forwarding': 'encaminhamento de porta'
}

# Funcao para traduzir uma palavra baseada no dicionario
def translate(dic, word):
  for key, value in dic.items():
    if (key.lower() == word.lower()):
      return value
  return 'Word not found'

while True:
  # Aceita a conexao do cliente
  connectionSocket, addr = serverSocket.accept()

  # Palavra recebida do cliente
  sentence = connectionSocket.recv(1024).decode()

  # Traduz a palavra baseada no dicionario
  translated = translate(networkDict, sentence)

  # Envia a palavra traduzida de volta para o cliente
  connectionSocket.send(translated.encode())

  # Fecha a conexao com o cliente
  connectionSocket.close()