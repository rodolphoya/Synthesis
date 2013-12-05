
*************************************************************************************
Sintetizador control�vel com a biblioteca AudioLazy (DSP em tempo real para o Python)
*************************************************************************************




N�mero do Projeto: 08

Data: 13 / novembro / 2013

Orientador(es):
Danilo de Jesus da Silva Bellini



Equipe de alunos:

8041394 � Elisa Tengan Pires de Souza

8041884 � Gabriela Souza de Melo

8042798 � Jos� Henrique Camargo Leopoldo e Silva

7630594 � Rodolpho Yuiti Adamatsu



Resumo
======

O projeto a ser apresentado consiste na elabora��o de um sintetizador control�vel de �udio por meio de programa��o fazendo-se uso da linguagem Python. Neste sintetizador de �udio, o objetivo � de simular um som a partir de grava��es feitas do som de um viol�o.

Para a cria��o deste sintetizador, � imprescind�vel que tenha-se conhecimento de conceitos relacionados � an�lise, processamento e s�ntese de sinais. Desse modo, a etapa inicial do projeto consiste no estudo destes elementos apresentados. 
O sintetizador baseia-se em um modelo de s�ntese no qual um algoritmo � aplicado e diversos controles de vari�veis de um sinal s�o realizados para se obter o som similar ao de um viol�o desejado. Assim que � decidido como deve ser feita a s�ntese de �udio, � necess�rio realiza-la em forma de c�digo. A linguagem utilizada � o Python, a qual apresenta v�rias ferramentas �teis ao projeto, al�m de ser f�cil de ser compreendida em geral. N�o obstante, uma biblioteca adicional chamada Audiolazy (criada pelo pr�prio orientador do projeto) � necess�ria para a execu��o do c�digo, visto que ela possui diversos comandos que permitem a manipula��o de sinais e tamb�m de visualiza��o dos efeitos que cada varia��o nos par�metros causa sobre uma onda por meio de gr�ficos e tamb�m pela pr�pria reprodu��o do som sendo sintetizado. 

Para o sintetizador de �udio ser utilizado, � necess�rio implementar o programa criado em Python em uma interface b�sica para que qualquer indiv�duo pudesse compreender seu funcionamento. Primeiramente, o meio a ser controlado pelo usu�rio do programa escolhido � um teclado musical MIDI, o qual � conectado ao computador por um cabo MIDI-USB. Entretanto,� necess�rio tamb�m que haja uma interface gr�fica que relacione o programa ao teclado conectado e portanto foi criado um ambiente simples no qual o programa criado � rodado sendo assim poss�vel fazer uso do sintetizador.

Por fim, o projeto apresenta uma interessante proposta que ilustra a possibilidade de aplicar conhecimentos de engenharia el�trica e computa��o n�o s� sobre quest�es predominantemente cient�ficas, mas tamb�m sobre a �rea de produ��o art�stica.








Conte�do
========

1.Introdu��o
------------

1.1.Conceitos
^^^^^^^^^^^^^


Um sintetizador de �udio consiste em um instrumento eletr�nico que gera e processa diferentes sons. Nesse projeto, o objetivo � criar tal instrumento por meio de programa��o e implement�-lo em uma interface b�sica para ter seu funcionamento em tempo real.

Sendo assim, primeiramente, deve-se pensar em como ocorre o processo de sintetiza��o de �udio para depois poder descrev�-lo em forma de c�digo. Para isso,� necess�rio que haja o conhecimento de diversos conceitos relacionados � an�lise, processamento e s�ntese de sinais. A an�lise e o processamento consistem no ato de observar e coletar informa��es importantes que permitam uma manipula��o posterior do sinal em quest�o para cumprir o objetivo designado.

J� a s�ntese de sinais trata-se do ato de fabricar o sinal desejado, com as caracter�sticas antes analisadas por meio de manipula��o matem�tica utilizando python, de forma a obtermos a equa��o do filtro que o corpo do viol�o produz sobre o som.

Ap�s ter conhecimento sobre os processos necess�rios para a elabora��o do sintetizador, foi necess�rio escolher um som a ser sintetizado. Gra�as � familiaridade do grupo com instrumentos musicais, foi escolhido o viol�o para ter suas notas sintetizadas a partir do software a ser criado. Assim, foram gravadas notas isoladas produzidas pelo instrumento em formato .wav (o melhor formato a ser utilizado uma vez que, ao contr�rio do formato .mp3, n�o h� perdas de sinais de certas freq��ncias para compress�o de arquivo, resultando em maior qualidade).
Ap�s analisar-se as grava��es, o pr�ximo passo � sintetizar, de fato, o som desejado. Para isso, foi necess�rio ter conhecimento sobre a linguagem Python e a principal biblioteca a ser utilizada no projeto, a Audiolazy. Com suas ferramentas, sinais j� existentes podem ser manipulados com aplica��es de filtros prontos e tamb�m por filtros calculados pelo processo de an�lise das grava��es feito anteriormente. Um filtro altera o sinal original (de forma linear ou n�o no tempo, isto �, os par�metros desejados podem ser fixos ou vari�veis no tempo) e quando aplicado corretamente, � um importante utens�lio para se atingir o sinal determinado.

Para o modelo de s�ntese ser aplic�vel no projeto, escrevemos em Python o c�digo do programa que realiza a s�ntese. Esse c�digo �  de um meio de ordenar tanto as tarefas necess�rias para realizar a s�ntese do som quanto o modo como ela vai ser aplicada na situa��o escolhida. Sendo assim, as etapas de associa��o da nota acionada com a s�ntese da mesma e tamb�m a execu��o dela s�o relacionadas, permitindo o funcionamento de um sintetizador em tempo real.
Entretanto, deve-se considerar ao criar o c�digo em Python a interface a ser utilizada pelo usu�rio do sintetizador. Como foi escolhido pelo grupo um teclado musical com sa�da MIDI, houve a necessidade de pensar em um meio de conect�-lo ao computador e associ�-lo ao programa. Assim, outra biblioteca adicional do Python chamada Pygame foi �til, visto que permite, de fato, a conex�o do teclado com o programa, fazendo com que a cada tecla acionada, uma determinada nota seja executada. Para conectar o teclado musical ao computador, foi utilizado um cabo MIDI-USB.

A interface gr�fica do sintetizador � bem simples, visto que o principal meio de entendimento do funcionamento do instrumento � atrav�s do pr�prio teclado conectado. Assim, foi feito um ambiente simplificado apenas para relacionar o c�digo em Python � funcionalidade do sintetizador controlado pelo mesmo.
















1.2.Motiva��o e justifica��o
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

O projeto foi sugerido pelo orientador Danilo de Jesus da Silva Bellini (Engenheiro Eletricista pela Poli, Mestre em Computa��o pelo IME-USP e M�sico pela ECA-USP). O grupo se interessou pelo projeto visto que ele envolvia a aplica��o de conhecimentos relacionados � engenharia el�trica e de computa��o em um assunto associado � manipula��o de �udio. Uma vez que os integrantes do grupo possu�am grande afinidade com quest�es principalmente musicais, foi natural que a curiosidade sobre o tema fosse despertada.

A id�ia proposta pode ser desenvolvida de diversas maneiras, e o orientador deu liberdade ao grupo de escolher o som a ser sintetizado e tamb�m a interface a ser utilizada, dentre as diversas op��es que ele mesmo sugeriu.

1.3.Metodologia
^^^^^^^^^^^^^^^

O projeto, em geral, foi feito a partir de um m�todo de observa��o de exemplos apresentados pelo orientador e de tentativa de reprodu��o de id�ias similares pelos integrantes do grupo. Durante a maior parte das reuni�es, o processo consistia em pequenas aulas sobre os assuntos a serem conhecidos e esclarecimento de d�vidas quanto �s etapas de pr�pria execu��o do projeto. A partir dessas aulas, e de textos e exemplos adicionais, conseguimos come�ar a compreender como funcionaria o projeto, como ocorria a escrita de c�digos em Python, quais os conceitos de processamento digital de sinais que precis�vamos saber e como os utilizar�amos de forma a atingir o objetivo final. A partir do momento que j� t�nhamos alguma base te�rica, come�amos a escrever o c�digo, nos baseando nos exemplos que j� hav�amos visto.










2.Cronograma e organiza��o
--------------------------

2.1. Esquema do cronograma
^^^^^^^^^^^^^^^^^^^^^^^^^^
 

    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Etapa /Semana                | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
    +==============================+===+===+===+===+===+===+===+===+===+====+
    | Familiariza��o com Python    | X | X | X | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Familiariza��o com Audiolazy | X | X | X | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+ 
    | Estudo T. Processamento de S.| X | X | X | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Estudo de modelos de s�ntese | X | X | X | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Realiza��o de Grava��es      |   |   |   | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | An�lise de Grava��es         |   |   |   | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Elaborar Modelo de S�ntese   |   |   |   | X | X | X | X |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Escrita de C�digo em Python  |   |   |   | X | X | X | X | X | X |    |      
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Interface Gr�fica            |   |   |   |   | X | X | X | X | X | X  |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Documenta��o                 | X | X | X | X | X | X | X | X | X | X  |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+

 
O cronograma para a realiza��o do projeto foi elaborado da forma apresentada na tabela acima. Para um melhor entendimento, a defini��o de cada tarefa � apresentada abaixo:

�	Familiariza��o com o Python

Trata-se do in�cio da aquisi��o de conhecimento sobre o funcionamento da linguagem Python, sendo enfatizado o aprendizado sobre seus comandos e ferramentas dispon�veis que ser�o �teis para o desenvolvimento do projeto.

�	Familiariza��o com a Audiolazy

Trata-se da aquisi��o de conhecimento sobre os recursos da biblioteca para Python chamada Audiolazy. Foram realizados diversos exemplos de utiliza��o de comandos de plotagem de resposta em freq��ncia, aplica��o de filtros como o passa-baixas (�lowpass �) e o ressonador (�resonator�) sobre o ru�do branco (�white noise�), al�m da visualiza��o das diferen�as existentes entre formas distintas de onda (senoidal, dente-de-serra, entre outras).

�	Estudo da Teoria de Processamento de Sinais

Consiste do estudo dos elementos relacionados � an�lise e � modifica��o de sinais com o intuito de torn�-los apropriados para uma espec�fica aplica��o dos mesmos. No caso do projeto do sintetizador apresentado, � enfatizado um estudo sobre o processamento digital de sinais (DSP � Digital Signal Processing), no qual h� a manipula��o por t�cnicas matem�ticas computacionais de dados apresentados em forma de sequ�ncias. A apresenta��o do conceito de Transformada Z e seu funcionamento na linguagem Python foi extremamente importante para a compreens�o do que se trata, de fato, o processamento digital de sinais e sua utilidade para a elabora��o do sintetizador.

�	Estudo de Modelos de S�ntese

Consiste no estudo do modelamento de s�ntese atrav�s de exemplos j� existentes. Um exemplo em particular, associado � s�ntese do som de um trompete  (Horner & Beauchamp, 1995) � estudado mais a fundo.

�	Realiza��o de Grava��es

Foram gravadas notas isoladas emitidas por um viol�o, em formato .wav, para servirem de base para o desenvolvimento do modelo de s�ntese do �udio captado.

�	An�lise de Grava��es

Na an�lise das grava��es, foram obtidas a resposta em frequ�ncia, o gr�fico do decaimento da intensidade do som analisado e o filtro associado ao formato do corpo do viol�o (o qual est� relacionado � interfer�ncia que o formato imp�e sobre o som obtido). Essa etapa , ao ser finalizada, permite a reflex�o sobre os resultados e o in�cio da cria��o do modelo de s�ntese baseando-se nas conclus�es adquiridas.

�	Elaborar um modelo de s�ntese

Etapa da cria��o do modelo de s�ntese a ser utilizado para obter o som semelhante ao do viol�o previamente gravado. Por meio de testes, h� a obten��o das manipula��es necess�rias e que devem ser transformadas em c�digo.

�	Escrita de C�digo em Python

Etapa na qual foi realizada, de fato, a cria��o de um programa que permitisse o uso do modelo de s�ntese criado para reproduzir os sons criados por meio do teclado MIDI. O c�digo consiste no reconhecimento do componente MIDI conectado, a implementa��o do modelo de s�ntese e tamb�m a l�gica de funcionamento de resposta a ser devolvida a cada tecla do componente ser pressionada com o aux�lio da biblioteca Pygame.

�	Projeto e Implementa��o da Interface Gr�fica

Etapa na qual desenvolvemos a interface gr�fica, por meio de programa��o em Python. A ideia da interface era algo simples, que pudesse deixar o programa mais user-friendly  e mais interativo.

�	Produ��o da documenta��o: relat�rios e slides

Todo o processo de desenvolvimento do projeto deveria, como notificado, ser documentado, podendo ser observados pontos de evolu��o no andamento, dificuldades na execu��o, poss�veis falhas e o desempenho em geral do grupo ao estudar os assuntos necess�rios e aplicar o conhecimento adquirido. Portanto, essa etapa ocupa todas as semanas dispon�veis do projeto como uma importante tarefa que em nenhum momento deveria deixar de ser feita para ser poss�vel, ao final, analisar como foi o progresso na execu��o do sintetizador control�vel. Por tratar-se de uma proposta envolvendo escrita de c�digos em Python,foram armazenados arquivos .txt com hist�ricos do Shell interativo IPython, no qual foram testados exemplos dados pelo orientador, al�m dos gr�ficos obtidos pela an�lise das grava��es,o processo da cria��o do modelo de s�ntese, da escrita do c�digo e por fim,os slides elaborados para as apresenta��es parciais e final no projeto.


2.2.Execu��o do cronograma
^^^^^^^^^^^^^^^^^^^^^^^^^^

O cronograma inicialmente foi seguido conforme havia sido determinado. Entretanto, houve dificuldades na execu��o da etapa da cria��o do modelo de s�ntese. O grupo, ao finalizar a etapa da an�lise das grava��es, conseguiu tirar conclus�es sobre como o som sintetizado deveria ser, por�m, n�o conseguiu rapidamente associar a um algoritmo que pudesse representar o processo de s�ntese necess�rio para atingir o resultado esperado.
Sendo assim, foi necess�rio que o cronograma fosse alterado, resultando em um adiamento em uma semana da etapa de Projeto e Implementa��o de Interface Gr�fica, como pode ser visto no cronograma atualizado:

    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Etapa /Semana                | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
    +==============================+===+===+===+===+===+===+===+===+===+====+
    | Familiariza��o com Python    | X | X | X | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Familiariza��o com Audiolazy | X | X | X | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+ 
    | Estudo T. Processamento de S.| X | X | X | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Estudo de modelos de s�ntese | X | X | X | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Realiza��o de Grava��es      |   |   |   | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | An�lise de Grava��es         |   |   |   | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Elaborar Modelo de S�ntese   |   |   |   | X | X | X | X |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Escrita de C�digo em Python  |   |   |   | X | X | X | X | X | X |    |      
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Interface Gr�fica            |   |   |   |   |   |   |   | X | X | X  |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Documenta��o                 | X | X | X | X | X | X | X | X | X | X  |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
 



2.3.Divis�o do trabalho
^^^^^^^^^^^^^^^^^^^^^^^

A princ�pio, todas as tarefas seriam feitas em conjunto por todos os membros do grupo. Entretanto, por motivos de falta de disponibilidade de hor�rios em comum al�m das reuni�es semanais para a elabora��o do projeto, houve claramente a necessidade de dividir as tarefas entre os membros para que o cronograma fosse cumprido conforme estabelecido anteriormente.
As etapas de realiza��o de grava��es, an�lise de grava��es, elabora��o do modelo de s�ntese e escrita de c�digo em Python e o implementa��o da interface gr�fica foram feitas individualmente, sempre com o aux�lio do orientador. J� as etapas de familiariza��o com Python e Audiolazy, estudo da teoria de processamento de sinais e de modelos de s�nteses, e elabora��o dos relat�rios e documenta��o foram desenvolvidas em conjunto.

Rela��o de tarefas feitas individualmente por cada membro do grupo:

�	Elisa Tengan Pires de Souza: an�lise das grava��es, elabora��o do modelo de s�ntese

�	Gabriela Souza de Melo: realiza��o das grava��es, an�lise das grava��es

�	Jos� Henrique Camargo Leopoldo e Silva: elabora��o do modelo de s�ntese, escrita de c�digo em Python

�	Rodolpho Yuiti Adamatsu : implementa��o da interface gr�fica















3.Projeto
---------

3.1.Especifica��o,  dimensionamentos, c�lculos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para o desenvolvimento do software, foram estabelecidas as seguintes especifica��es:

�	Linguagem: A linguagem utilizada (Python) foi escolhida pelo pr�prio orientador e j� havia sido deixado claro que seria feito o uso da mesma no pr�prio nome apresentado do projeto na planilha de propostas de orientadores disponibilizada no in�cio do segundo semestre desse ano.

�	Bibliotecas auxiliares: Inicialmente, era sabido que a biblioteca Audiolazy,criada pelo pr�prio orientador, seria a principal biblioteca auxiliar a ser utilizada. Suas ferramentas permitem uma an�lise de grava��es e permitem tamb�m a elabora��o da s�ntese do som desejado. Al�m da Audiolzay, foi necess�rio o uso da biblioteca Pygame para realizar a conex�o do teclado MIDI e coorden�-lo com o programa feito em Python.














3.2.Materiais e or�amento
^^^^^^^^^^^^^^^^^^^^^^^^^

Os materiais necess�rios para o projeto est�o listados abaixo com seus respectivos pre�os. � importante notificar que os integrantes do grupo j� possu�am todos os itens necess�rios, resultando em um custo zero para a execu��o do projeto.

Item necess�rio	Pre�o

Teclado musical com entrada MIDI	        R$ 700

Cabo MIDI-USB	                                R$ 130

Caixas de som para demonstra��o do programa	R$ 200

Computador (Laptop)	                        R$ 1.800




3.3.Execu��o
^^^^^^^^^^^^


Para poder realizar o projeto, primeiramente foi necessário obter um embasamento teórico a respeito de filtros, Transformada Z e sinal. Isso foi realizado com a ajuda do Prof. Orientador em reuniões semanais. Simultaneamente também foi realizado um primeiro contato com a linguagem de programação Python, por meio de sites como codeacademy.com e stackoverflow.com, além de haver auxílio também nessas reuniões.

O próximo passo foi a escolha de um som a ser sintetizado, no caso, foi escolhido o som do violão. O som de várias notas foi gravado para que, por meio da biblioteca Audiolazy e outras ferramentas do Python, essas notas puderam ser analisadas. Feito isso, uma vez que apesar das diferentes frequências, todas elas seguem um formato semelhante, foi possível chegar a um filtro bastante próximo ao som do violão. Tal filtro foi obtido por meio de ferramentas matemáticas do Python e do Audiolazy, e o grupo optou por utilizar o modelo de síntese aditivo pela simples implementação.
Tendo o filtro iniciou-se o processo de escrita do código do sintetizador em si.


Primeiramente, o código foi organizado de modo que recebendo um número de 1 a 13 como entrada, que eram associadas a uma frequência/nota cada, o algoritmo a partir de um ruído branco qualquer, moldá-o com a frequência escolhida e aplica o filtro, devolvendo um som como saída do programa, de modo que esse som, após passar pelo filtro assemelha-se ao som da nota escolhida tocada em um violão.
Visto que uma das propostas do projeto era utilizar um teclado MIDI como entrada para o programa, o desenvolvimento do algoritmo passou então a focar-se na interface controlador/código. Para isso foi utilizada a biblioteca Pygame, pela praticidade e alta compatibilidade com diversos controladores, de joysticks a interfaces MIDI. Na parte inicial, muito foi feito utilizando um controle de XBOX, até que foi possível apertar um botão, atribuir uma frequência/nota específica para ele e tocá-la. Após isso, foi relativamente simples a substituição pelo teclado MIDI, onde apenas algumas funções da biblioteca tiveram de ser trocadas.

A parte final do projeto é a Interface Gráfica (GUI).










4.Testes
--------

Para o teste final do projeto,foi conectado,de fato, o teclado MIDI ao computador e assim como foi feito previamente com o controle de Xbox, o programa foi testado para observarmos se as fun��es que controlavam a conex�o MIDI estavam de acordo.
Com rela��o ao resultado final do projeto, � poss�vel afirmar que o mesmo n�o foi completamente bem sucedido. Para a apresenta��o final, o c�digo feito funcionava, as conex�es do teclado MIDI foram feitas e ao acionar uma tecla do instrumento, o som sintetizado era tocado. Entretanto, quando as teclas eram acionadas seguidamente em um curto intervalo de tempo, o som obtido n�o era tocado como esperado. Havia algum tipo de interfer�ncia , causada pelo fato de a s�ntese de notas seguidas em tempo real exigir um processador consideravelmente potente . 
Outro problema foi a interface gr�fica criada, a qual n�o foi feita de forma interativa e portanto,n�o era influenciada pelas a��es do usu�rio ao tocar o teclado. 

O modelo de s�ntese atingido n�o se baseou no algoritmo dado no modelo do trompete de s�ntese aditiva que inicialmente era para servir de refer�ncia, apesar de um modelo simples desse tipo de s�ntese ter sido iniciado, e foi utilizada uma t�cnica de s�ntese subtrativa com o filtro obtido atrav�s da an�lise LPC aplicado. Esse problema se gerou tanto por motivos de talvez um entendimento falho do artigo no qual o modelo se encontrava, quanto por um gerenciamento de tempo para realiza��o do projeto por parte do pr�prio grupo desfavor�vel. Al�m disso, se o modelo de s�ntese aditiva tivesse sido implementado, o problema da interfer�ncia dos sons causados pela velocidade necess�ria de processamento de notas seguidos seria reduzido. Por fim, pode-se dizer que o som sintetizado obtido e apresentado deixou a desejar.

Com rela��o ao c�digo do programa em si, foi observado que sua finaliza��o deveria ter sido mais levada em conta. Havia muitos elementos que necessitavam de um coment�rio, mas n�o o possu�am. O c�digo deveria estar mais organizado e com algumas altera��es que o tornassem mais �limpo� e que providenciasse um melhor entendimento.

5.Resultados, coment�rios e conclus�es
--------------------------------------

Avalia��o dos resultados:

O projeto em sua forma final, apesar de ter cumprido a meta inicial de sintetizar o som de um instrumento musical real e implement�-lo em um programa no qual o teclado MIDI era o meio de fazer uso do som obtido ficou abaixo das expectativas, visto que alguns pontos do c�digo e do modelo de s�ntese em si poderiam ter sido alterados  de forma a otimizar o funcionamento como um todo.

Falhas:

Houve falhas na implementa��o da interface gr�fica, a qual n�o era interativa com o programa. Por conta da velocidade de processamento em tempo real,houve falhas tamb�m na execu��o de notas seguidas ao serem acionadas as teclas do teclado MIDI, resultando em uma interfer�ncia de sons.

Dificuldades:

Com rela��o �s dificuldades encontradas para a realiza��o do projeto, pode-se citar primeiramente a pouca ou nenhuma familiaridade dos integrantes do grupo com a pr�pria linguagem utilizada para criar o programa, o Python.Outro obst�culo encontrado foi a dificuldade em entender os conceitos de an�lise e processamento de sinais. Desde o in�cio das reuni�es realizadas, o orientador apresentou a parte te�rica necess�ria para o desenvolvimento do sintetizador. Entretanto, todo o conte�do em si foi bastante denso e levou v�rias semanas extras para ser compreendido. O projeto somente come�ou a apresentar progresso ap�s os integrantes do grupo terem conseguido associar tudo o que foi apresentado em teoria com o objetivo de sintetizar um som.

Sugest�es:

Para poss�veis melhorias no projeto, seria interessante fazer com que a interface gr�fica interagisse com as a��es do programa criado. Um novo modelo de s�ntese, dessa vez do tipo aditiva, seria favor�vel para reduzir o problema da interfer�ncia de sons.

Agradecimentos:

Gostar�amos de agradecer nosso orientador Danilo, por toda a ajuda e suporte durante o semestre para a realiza��o do projeto.





6.Bibliografia
--------------

Indique os itens de bibliografia citados ou que auxiliaram seus estudos para o projeto, usando o estilo:

Livros:
Oppenheim, Alan V.; Schafer, Ronald W., Buck, John R. - Discrete Time Signal Processing � Prentice Hall � Segunda Edi��o - 1998

Artigos:
Horner,Andrew ;Beauchamp,James � Synthesis of Trumpet TonesUsing a Wavetable
and a Dynamic Filter � Journal of Audio Engineering Society � vol 43/n.10 � p�ginas 799-812 � Editora � 1995
