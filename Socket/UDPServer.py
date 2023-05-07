from socket import *

# Inicializa servidor na porta 12000
serverPort = 12000

# Cria o socket do servidor com protocolo UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Vincula o socket do servidor ao endereço de loopback
serverSocket.bind(('', serverPort))

# Imprime mensagem
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
  # Palavra recebida do cliente
  message, clientAddress = serverSocket.recvfrom(2048)

  # Traducao da palavra baseado no dicionario
  translated = translate(networkDict, message.decode())
  # modifiedMessage = message.decode().upper()

  # Envia a mensagem modificada para o endereco do cliente que enviou a mensagem
  serverSocket.sendto(translated.encode(), clientAddress)