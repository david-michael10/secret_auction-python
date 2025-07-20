● art.py:

    Arte em ASCII

--------------------------

● main.py:

    Arquivo principal

--------------------------

<img width="1351" height="598" alt="image" src="https://github.com/user-attachments/assets/3987d4d3-3eb4-4c98-bfd2-cc28c488ec06" />

● Importei a arte em ASCII e armazenei em uma variável

● Criei um dicionário para armazenar os inputs do usuário

● Criei os inputs do usuário que serão nomes e "lances"

● Adicionei o nome como key e o lance como value no dicionário

● fiz um outro input para saber se o usuário deseja continuar ou não

--------------------------

<img width="1284" height="572" alt="image" src="https://github.com/user-attachments/assets/8a8f6ded-5d32-4141-b620-e1add8e81e01" />

● Se o usuário não quiser:

    Então paro o loop com uma variável "False"

    Crio uma variável para contabilizar qual foi o maior lance e também uma outra variável para a key correspondente desse lance

    Faço um loop para cada key no dicionário e crio uma variável para armazenar o valor dessas keys

    Verifico se o valor é maior que a variável que criei e atualizo o valor dessa variável

    Pego essa ley e armazeno na variável vazia que criei antes

    Então imprimo a key (nome da pessoa) e o seu valor correspondente

● Caso o usuário queira continuar, apenas limpo a tela e o processo continua
