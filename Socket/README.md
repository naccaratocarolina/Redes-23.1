# Comunicação Cliente-Servidor com UDP e TCP

- ```TCPServer.py``` e ```TCPClient.py```
- ```UDPServer.py``` e ```UDPClient.py```

## Principais diferenças entre os protocolos
As principais diferenças estão relacionadas à confiabilidade da comunicação e à forma como a conexão é estabelecida.

### Protocolo UDP
- A comunicação é não confiável, de forma que não há garantia de que a mensagem enviada pelo cliente chegará ao servidor, nem de que a resposta do servidor chegará de volta ao cliente
- O cliente pode enviar uma mensagem a qualquer momento, sem precisar esperar o servidor estar pronto para recebê-la

### Protocolo TCP
- A comunicação é confiável e orientada à conexão
- Antes de iniciar a troca de mensagens, é necessário estabelecer uma conexão entre o cliente e o servidor
- Durante a comunicação, o protocolo garante que as mensagens enviadas chegarão ao destinatário, e na ordem correta
- O protocolo garante que o cliente receberá uma resposta do servidor para cada mensagem enviada

## Principais diferenças de implementação
- Forma como a conexão é estabelecida e mantida
No caso do UDP, o servidor apenas cria um socket e fica esperando por mensagens enviadas pelos clientes. Já no caso do TCP, o servidor precisa criar um socket, bindá-lo a uma porta e depois esperar por conexões de clientes usando a função ```listen()```

- Forma como os dados são transmitidos
No UDP, os dados são transmitidos em datagramas, que têm um tamanho máximo fixo. Já no TCP, os dados são transmitidos em fluxo, ou seja, não há limitação no tamanho da mensagem enviada

- Forma como as mensagens são enviadas e recebidas
No caso do UDP, as mensagens são enviadas e recebidas usando as funções ```sendto()``` e ```recvfrom()```. Já no caso do TCP, as mensagens são enviadas e recebidas usando as funções ```send()``` e ```recv()```, e é necessário estabelecer uma conexão antes de iniciar a comunicação. Além disso, no caso do TCP, é necessário fechar a conexão com o cliente após cada mensagem recebida, usando a função ```close()```
