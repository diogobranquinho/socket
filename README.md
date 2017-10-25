# Exemplo de Socket em Python
Utilização da biblioteca socket para realizar a comunicação entre processos via socket.

## Pré-requisitos
Para esse exemplo funcionar é necessário o uso do Python 3 ou superior.

## Executando o exemplo UDP
Primeiramente abra um prompt de comando e execute o servidor UDP.
```
python server_udp.py 
```
Depois abra um novo prompt de comando e execute o cliente UDP.
```
python client_udp.py 
```
Entre com mensagens no cliente e observe as mensagens chegando no servidor, para sair pressione CTRL+X.

## Executando o exemplo TCP
Primeiramente abra um prompt de comando e execute o servidor TCP.
```
python server_tcp.py 
```
Depois abra um novo prompt de comando e execute o cliente TCP.
```
python client_tcp.py 
```
Entre com mensagens no cliente e observe as mensagens chegando no servidor, para sair pressione CTRL+X. Observe que apenas um cliente pode se conectar ao servidor por vez.
Mesma coisa para o exemplo com Thread, porém conecte mais de um cliente ao mesmo tempo, para visualizar o funcionamento da thread.

## Autor

* **Diogo Branquinho Ramos** - [diogobranquinho](https://github.com/diogobranquinho)