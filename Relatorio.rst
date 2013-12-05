
*************************************************************************************
Sintetizador controlável com a biblioteca AudioLazy (DSP em tempo real para o Python)
*************************************************************************************




Número do Projeto: 08

Data: 13 / novembro / 2013

Orientador(es):
Danilo de Jesus da Silva Bellini



Equipe de alunos:

8041394 – Elisa Tengan Pires de Souza

8041884 – Gabriela Souza de Melo

8042798 – José Henrique Camargo Leopoldo e Silva

7630594 – Rodolpho Yuiti Adamatsu



Resumo
======

O projeto a ser apresentado consiste na elaboração de um sintetizador controlável de áudio por meio de programação fazendo-se uso da linguagem Python. Neste sintetizador de áudio, o objetivo é de simular um som a partir de gravações feitas do som de um violão.

Para a criação deste sintetizador, é imprescindível que tenha-se conhecimento de conceitos relacionados à análise, processamento e síntese de sinais. Desse modo, a etapa inicial do projeto consiste no estudo destes elementos apresentados. 
O sintetizador baseia-se em um modelo de síntese no qual um algoritmo é aplicado e diversos controles de variáveis de um sinal são realizados para se obter o som similar ao de um violão desejado. Assim que é decidido como deve ser feita a síntese de áudio, é necessário realiza-la em forma de código. A linguagem utilizada é o Python, a qual apresenta várias ferramentas úteis ao projeto, além de ser fácil de ser compreendida em geral. Não obstante, uma biblioteca adicional chamada Audiolazy (criada pelo próprio orientador do projeto) é necessária para a execução do código, visto que ela possui diversos comandos que permitem a manipulação de sinais e também de visualização dos efeitos que cada variação nos parâmetros causa sobre uma onda por meio de gráficos e também pela própria reprodução do som sendo sintetizado. 

Para o sintetizador de áudio ser utilizado, é necessário implementar o programa criado em Python em uma interface básica para que qualquer indivíduo pudesse compreender seu funcionamento. Primeiramente, o meio a ser controlado pelo usuário do programa escolhido é um teclado musical MIDI, o qual é conectado ao computador por um cabo MIDI-USB. Entretanto,é necessário também que haja uma interface gráfica que relacione o programa ao teclado conectado e portanto foi criado um ambiente simples no qual o programa criado é rodado sendo assim possível fazer uso do sintetizador.

Por fim, o projeto apresenta uma interessante proposta que ilustra a possibilidade de aplicar conhecimentos de engenharia elétrica e computação não só sobre questões predominantemente científicas, mas também sobre a área de produção artística.








Conteúdo
========

1.Introdução
------------

1.1.Conceitos
^^^^^^^^^^^^^


Um sintetizador de áudio consiste em um instrumento eletrônico que gera e processa diferentes sons. Nesse projeto, o objetivo é criar tal instrumento por meio de programação e implementá-lo em uma interface básica para ter seu funcionamento em tempo real.

Sendo assim, primeiramente, deve-se pensar em como ocorre o processo de sintetização de áudio para depois poder descrevê-lo em forma de código. Para isso,é necessário que haja o conhecimento de diversos conceitos relacionados à análise, processamento e síntese de sinais. A análise e o processamento consistem no ato de observar e coletar informações importantes que permitam uma manipulação posterior do sinal em questão para cumprir o objetivo designado.

Já a síntese de sinais trata-se do ato de fabricar o sinal desejado, com as características antes analisadas por meio de manipulação matemática utilizando python, de forma a obtermos a equação do filtro que o corpo do violão produz sobre o som.

Após ter conhecimento sobre os processos necessários para a elaboração do sintetizador, foi necessário escolher um som a ser sintetizado. Graças à familiaridade do grupo com instrumentos musicais, foi escolhido o violão para ter suas notas sintetizadas a partir do software a ser criado. Assim, foram gravadas notas isoladas produzidas pelo instrumento em formato .wav (o melhor formato a ser utilizado uma vez que, ao contrário do formato .mp3, não há perdas de sinais de certas freqüências para compressão de arquivo, resultando em maior qualidade).
Após analisar-se as gravações, o próximo passo é sintetizar, de fato, o som desejado. Para isso, foi necessário ter conhecimento sobre a linguagem Python e a principal biblioteca a ser utilizada no projeto, a Audiolazy. Com suas ferramentas, sinais já existentes podem ser manipulados com aplicações de filtros prontos e também por filtros calculados pelo processo de análise das gravações feito anteriormente. Um filtro altera o sinal original (de forma linear ou não no tempo, isto é, os parâmetros desejados podem ser fixos ou variáveis no tempo) e quando aplicado corretamente, é um importante utensílio para se atingir o sinal determinado.

Para o modelo de síntese ser aplicável no projeto, escrevemos em Python o código do programa que realiza a síntese. Esse código é  de um meio de ordenar tanto as tarefas necessárias para realizar a síntese do som quanto o modo como ela vai ser aplicada na situação escolhida. Sendo assim, as etapas de associação da nota acionada com a síntese da mesma e também a execução dela são relacionadas, permitindo o funcionamento de um sintetizador em tempo real.
Entretanto, deve-se considerar ao criar o código em Python a interface a ser utilizada pelo usuário do sintetizador. Como foi escolhido pelo grupo um teclado musical com saída MIDI, houve a necessidade de pensar em um meio de conectá-lo ao computador e associá-lo ao programa. Assim, outra biblioteca adicional do Python chamada Pygame foi útil, visto que permite, de fato, a conexão do teclado com o programa, fazendo com que a cada tecla acionada, uma determinada nota seja executada. Para conectar o teclado musical ao computador, foi utilizado um cabo MIDI-USB.

A interface gráfica do sintetizador é bem simples, visto que o principal meio de entendimento do funcionamento do instrumento é através do próprio teclado conectado. Assim, foi feito um ambiente simplificado apenas para relacionar o código em Python à funcionalidade do sintetizador controlado pelo mesmo.
















1.2.Motivação e justificação
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

O projeto foi sugerido pelo orientador Danilo de Jesus da Silva Bellini (Engenheiro Eletricista pela Poli, Mestre em Computação pelo IME-USP e Músico pela ECA-USP). O grupo se interessou pelo projeto visto que ele envolvia a aplicação de conhecimentos relacionados à engenharia elétrica e de computação em um assunto associado à manipulação de áudio. Uma vez que os integrantes do grupo possuíam grande afinidade com questões principalmente musicais, foi natural que a curiosidade sobre o tema fosse despertada.

A idéia proposta pode ser desenvolvida de diversas maneiras, e o orientador deu liberdade ao grupo de escolher o som a ser sintetizado e também a interface a ser utilizada, dentre as diversas opções que ele mesmo sugeriu.

1.3.Metodologia
^^^^^^^^^^^^^^^

O projeto, em geral, foi feito a partir de um método de observação de exemplos apresentados pelo orientador e de tentativa de reprodução de idéias similares pelos integrantes do grupo. Durante a maior parte das reuniões, o processo consistia em pequenas aulas sobre os assuntos a serem conhecidos e esclarecimento de dúvidas quanto às etapas de própria execução do projeto. A partir dessas aulas, e de textos e exemplos adicionais, conseguimos começar a compreender como funcionaria o projeto, como ocorria a escrita de códigos em Python, quais os conceitos de processamento digital de sinais que precisávamos saber e como os utilizaríamos de forma a atingir o objetivo final. A partir do momento que já tínhamos alguma base teórica, começamos a escrever o código, nos baseando nos exemplos que já havíamos visto.










2.Cronograma e organização
--------------------------

2.1. Esquema do cronograma
^^^^^^^^^^^^^^^^^^^^^^^^^^
 

    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Etapa /Semana                | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
    +==============================+===+===+===+===+===+===+===+===+===+====+
    | Familiarização com Python    | X | X | X | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Familiarização com Audiolazy | X | X | X | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+ 
    | Estudo T. Processamento de S.| X | X | X | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Estudo de modelos de síntese | X | X | X | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Realização de Gravações      |   |   |   | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Análise de Gravações         |   |   |   | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Elaborar Modelo de Síntese   |   |   |   | X | X | X | X |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Escrita de Código em Python  |   |   |   | X | X | X | X | X | X |    |      
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Interface Gráfica            |   |   |   |   | X | X | X | X | X | X  |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Documentação                 | X | X | X | X | X | X | X | X | X | X  |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+

 
O cronograma para a realização do projeto foi elaborado da forma apresentada na tabela acima. Para um melhor entendimento, a definição de cada tarefa é apresentada abaixo:

•	Familiarização com o Python

Trata-se do início da aquisição de conhecimento sobre o funcionamento da linguagem Python, sendo enfatizado o aprendizado sobre seus comandos e ferramentas disponíveis que serão úteis para o desenvolvimento do projeto.

•	Familiarização com a Audiolazy

Trata-se da aquisição de conhecimento sobre os recursos da biblioteca para Python chamada Audiolazy. Foram realizados diversos exemplos de utilização de comandos de plotagem de resposta em freqüência, aplicação de filtros como o passa-baixas (“lowpass “) e o ressonador (“resonator”) sobre o ruído branco (“white noise”), além da visualização das diferenças existentes entre formas distintas de onda (senoidal, dente-de-serra, entre outras).

•	Estudo da Teoria de Processamento de Sinais

Consiste do estudo dos elementos relacionados à análise e à modificação de sinais com o intuito de torná-los apropriados para uma específica aplicação dos mesmos. No caso do projeto do sintetizador apresentado, é enfatizado um estudo sobre o processamento digital de sinais (DSP – Digital Signal Processing), no qual há a manipulação por técnicas matemáticas computacionais de dados apresentados em forma de sequências. A apresentação do conceito de Transformada Z e seu funcionamento na linguagem Python foi extremamente importante para a compreensão do que se trata, de fato, o processamento digital de sinais e sua utilidade para a elaboração do sintetizador.

•	Estudo de Modelos de Síntese

Consiste no estudo do modelamento de síntese através de exemplos já existentes. Um exemplo em particular, associado à síntese do som de um trompete  (Horner & Beauchamp, 1995) é estudado mais a fundo.

•	Realização de Gravações

Foram gravadas notas isoladas emitidas por um violão, em formato .wav, para servirem de base para o desenvolvimento do modelo de síntese do áudio captado.

•	Análise de Gravações

Na análise das gravações, foram obtidas a resposta em frequência, o gráfico do decaimento da intensidade do som analisado e o filtro associado ao formato do corpo do violão (o qual está relacionado à interferência que o formato impõe sobre o som obtido). Essa etapa , ao ser finalizada, permite a reflexão sobre os resultados e o início da criação do modelo de síntese baseando-se nas conclusões adquiridas.

•	Elaborar um modelo de síntese

Etapa da criação do modelo de síntese a ser utilizado para obter o som semelhante ao do violão previamente gravado. Por meio de testes, há a obtenção das manipulações necessárias e que devem ser transformadas em código.

•	Escrita de Código em Python

Etapa na qual foi realizada, de fato, a criação de um programa que permitisse o uso do modelo de síntese criado para reproduzir os sons criados por meio do teclado MIDI. O código consiste no reconhecimento do componente MIDI conectado, a implementação do modelo de síntese e também a lógica de funcionamento de resposta a ser devolvida a cada tecla do componente ser pressionada com o auxílio da biblioteca Pygame.

•	Projeto e Implementação da Interface Gráfica

Etapa na qual desenvolvemos a interface gráfica, por meio de programação em Python. A ideia da interface era algo simples, que pudesse deixar o programa mais user-friendly  e mais interativo.

•	Produção da documentação: relatórios e slides

Todo o processo de desenvolvimento do projeto deveria, como notificado, ser documentado, podendo ser observados pontos de evolução no andamento, dificuldades na execução, possíveis falhas e o desempenho em geral do grupo ao estudar os assuntos necessários e aplicar o conhecimento adquirido. Portanto, essa etapa ocupa todas as semanas disponíveis do projeto como uma importante tarefa que em nenhum momento deveria deixar de ser feita para ser possível, ao final, analisar como foi o progresso na execução do sintetizador controlável. Por tratar-se de uma proposta envolvendo escrita de códigos em Python,foram armazenados arquivos .txt com históricos do Shell interativo IPython, no qual foram testados exemplos dados pelo orientador, além dos gráficos obtidos pela análise das gravações,o processo da criação do modelo de síntese, da escrita do código e por fim,os slides elaborados para as apresentações parciais e final no projeto.


2.2.Execução do cronograma
^^^^^^^^^^^^^^^^^^^^^^^^^^

O cronograma inicialmente foi seguido conforme havia sido determinado. Entretanto, houve dificuldades na execução da etapa da criação do modelo de síntese. O grupo, ao finalizar a etapa da análise das gravações, conseguiu tirar conclusões sobre como o som sintetizado deveria ser, porém, não conseguiu rapidamente associar a um algoritmo que pudesse representar o processo de síntese necessário para atingir o resultado esperado.
Sendo assim, foi necessário que o cronograma fosse alterado, resultando em um adiamento em uma semana da etapa de Projeto e Implementação de Interface Gráfica, como pode ser visto no cronograma atualizado:

    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Etapa /Semana                | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
    +==============================+===+===+===+===+===+===+===+===+===+====+
    | Familiarização com Python    | X | X | X | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Familiarização com Audiolazy | X | X | X | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+ 
    | Estudo T. Processamento de S.| X | X | X | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Estudo de modelos de síntese | X | X | X | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Realização de Gravações      |   |   |   | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Análise de Gravações         |   |   |   | X | X | X |   |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Elaborar Modelo de Síntese   |   |   |   | X | X | X | X |   |   |    |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Escrita de Código em Python  |   |   |   | X | X | X | X | X | X |    |      
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Interface Gráfica            |   |   |   |   |   |   |   | X | X | X  |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
    | Documentação                 | X | X | X | X | X | X | X | X | X | X  |
    +------------------------------+---+---+---+---+---+---+---+---+---+----+
 



2.3.Divisão do trabalho
^^^^^^^^^^^^^^^^^^^^^^^

A princípio, todas as tarefas seriam feitas em conjunto por todos os membros do grupo. Entretanto, por motivos de falta de disponibilidade de horários em comum além das reuniões semanais para a elaboração do projeto, houve claramente a necessidade de dividir as tarefas entre os membros para que o cronograma fosse cumprido conforme estabelecido anteriormente.
As etapas de realização de gravações, análise de gravações, elaboração do modelo de síntese e escrita de código em Python e o implementação da interface gráfica foram feitas individualmente, sempre com o auxílio do orientador. Já as etapas de familiarização com Python e Audiolazy, estudo da teoria de processamento de sinais e de modelos de sínteses, e elaboração dos relatórios e documentação foram desenvolvidas em conjunto.

Relação de tarefas feitas individualmente por cada membro do grupo:

•	Elisa Tengan Pires de Souza: análise das gravações, elaboração do modelo de síntese

•	Gabriela Souza de Melo: realização das gravações, análise das gravações

•	José Henrique Camargo Leopoldo e Silva: elaboração do modelo de síntese, escrita de código em Python

•	Rodolpho Yuiti Adamatsu : implementação da interface gráfica















3.Projeto
---------

3.1.Especificação,  dimensionamentos, cálculos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para o desenvolvimento do software, foram estabelecidas as seguintes especificações:

•	Linguagem: A linguagem utilizada (Python) foi escolhida pelo próprio orientador e já havia sido deixado claro que seria feito o uso da mesma no próprio nome apresentado do projeto na planilha de propostas de orientadores disponibilizada no início do segundo semestre desse ano.

•	Bibliotecas auxiliares: Inicialmente, era sabido que a biblioteca Audiolazy,criada pelo próprio orientador, seria a principal biblioteca auxiliar a ser utilizada. Suas ferramentas permitem uma análise de gravações e permitem também a elaboração da síntese do som desejado. Além da Audiolzay, foi necessário o uso da biblioteca Pygame para realizar a conexão do teclado MIDI e coordená-lo com o programa feito em Python.














3.2.Materiais e orçamento
^^^^^^^^^^^^^^^^^^^^^^^^^

Os materiais necessários para o projeto estão listados abaixo com seus respectivos preços. É importante notificar que os integrantes do grupo já possuíam todos os itens necessários, resultando em um custo zero para a execução do projeto.

Item necessário	Preço

Teclado musical com entrada MIDI	        R$ 700

Cabo MIDI-USB	                                R$ 130

Caixas de som para demonstração do programa	R$ 200

Computador (Laptop)	                        R$ 1.800




3.3.Execução
^^^^^^^^^^^^

Para poder realizar o projeto, primeiramente foi necessário obter um embasamento teórico a respeito de filtros, Transformada Z e sinal. Isso foi realizado com a ajuda do Prof. Orientador em reuniões semanais. Simultaneamente também foi realizado um primeiro contato com a linguagem de programação Python, por meio de sites como codeacademy.com e stackoverflow.com, além de haver auxílio também nessas reuniões.
O próximo passo foi a escolha de um som a ser sintetizado, no caso, foi escolhido o som do violão. O som de várias notas foi gravado para que, por meio da biblioteca Audiolazy e outras ferramentas do Python, essas notas puderam ser analisadas. Feito isso, uma vez que apesar das diferentes frequências, todas elas seguem um formato semelhante, foi possível chegar a um filtro bastante próximo ao som do violão. Tal filtro foi obtido por meio de ferramentas matemáticas do Python e do Audiolazy, e o grupo optou por utilizar o modelo de síntese aditivo pela simples implementação.
Tendo o filtro iniciou-se o processo de escrita do código do sintetizador em si. Primeiramente, o código foi organizado de modo que recebendo  um número de 1 a 13 como entrada, que eram associadas a uma frequência/nota cada, o algoritmo a partir de um ruído branco qualquer, moldá-o com a frequência escolhida e aplica o filtro, devolvendo um som como saída do programa, de modo que esse som, após passar pelo filtro assemelha-se ao som da nota escolhida tocada em um violão.
Visto que uma das propostas do projeto era utilizar um teclado MIDI como entrada para o programa, o desenvolvimento do algoritmo passou então a focar-se na interface controlador/código. Para isso foi utilizada a biblioteca Pygame, pela praticidade e alta compatibilidade com diversos controladores, de joysticks a interfaces MIDI. Na parte inicial, muito foi feito utilizando um controle de XBOX, até que foi possível apertar um botão, atribuir uma frequência/nota específica para ele e tocá-la. Após isso, foi relativamente simples a substituição pelo teclado MIDI, onde apenas algumas funções da biblioteca tiveram de ser trocadas.
A parte final do projeto é a Interface Gráfica (GUI). 










4.Testes
--------

Para o teste final do projeto,foi conectado,de fato, o teclado MIDI ao computador e assim como foi feito previamente com o controle de Xbox, o programa foi testado para observarmos se as funções que controlavam a conexão MIDI estavam de acordo.
Com relação ao resultado final do projeto, é possível afirmar que o mesmo não foi completamente bem sucedido. Para a apresentação final, o código feito funcionava, as conexões do teclado MIDI foram feitas e ao acionar uma tecla do instrumento, o som sintetizado era tocado. Entretanto, quando as teclas eram acionadas seguidamente em um curto intervalo de tempo, o som obtido não era tocado como esperado. Havia algum tipo de interferência , causada pelo fato de a síntese de notas seguidas em tempo real exigir um processador consideravelmente potente . 
Outro problema foi a interface gráfica criada, a qual não foi feita de forma interativa e portanto,não era influenciada pelas ações do usuário ao tocar o teclado. 

O modelo de síntese atingido não se baseou no algoritmo dado no modelo do trompete de síntese aditiva que inicialmente era para servir de referência, apesar de um modelo simples desse tipo de síntese ter sido iniciado, e foi utilizada uma técnica de síntese subtrativa com o filtro obtido através da análise LPC aplicado. Esse problema se gerou tanto por motivos de talvez um entendimento falho do artigo no qual o modelo se encontrava, quanto por um gerenciamento de tempo para realização do projeto por parte do próprio grupo desfavorável. Além disso, se o modelo de síntese aditiva tivesse sido implementado, o problema da interferência dos sons causados pela velocidade necessária de processamento de notas seguidos seria reduzido. Por fim, pode-se dizer que o som sintetizado obtido e apresentado deixou a desejar.

Com relação ao código do programa em si, foi observado que sua finalização deveria ter sido mais levada em conta. Havia muitos elementos que necessitavam de um comentário, mas não o possuíam. O código deveria estar mais organizado e com algumas alterações que o tornassem mais “limpo” e que providenciasse um melhor entendimento.

5.Resultados, comentários e conclusões
--------------------------------------

Avaliação dos resultados:

O projeto em sua forma final, apesar de ter cumprido a meta inicial de sintetizar o som de um instrumento musical real e implementá-lo em um programa no qual o teclado MIDI era o meio de fazer uso do som obtido ficou abaixo das expectativas, visto que alguns pontos do código e do modelo de síntese em si poderiam ter sido alterados  de forma a otimizar o funcionamento como um todo.

Falhas:

Houve falhas na implementação da interface gráfica, a qual não era interativa com o programa. Por conta da velocidade de processamento em tempo real,houve falhas também na execução de notas seguidas ao serem acionadas as teclas do teclado MIDI, resultando em uma interferência de sons.

Dificuldades:

Com relação às dificuldades encontradas para a realização do projeto, pode-se citar primeiramente a pouca ou nenhuma familiaridade dos integrantes do grupo com a própria linguagem utilizada para criar o programa, o Python.Outro obstáculo encontrado foi a dificuldade em entender os conceitos de análise e processamento de sinais. Desde o início das reuniões realizadas, o orientador apresentou a parte teórica necessária para o desenvolvimento do sintetizador. Entretanto, todo o conteúdo em si foi bastante denso e levou várias semanas extras para ser compreendido. O projeto somente começou a apresentar progresso após os integrantes do grupo terem conseguido associar tudo o que foi apresentado em teoria com o objetivo de sintetizar um som.

Sugestões:

Para possíveis melhorias no projeto, seria interessante fazer com que a interface gráfica interagisse com as ações do programa criado. Um novo modelo de síntese, dessa vez do tipo aditiva, seria favorável para reduzir o problema da interferência de sons.

Agradecimentos:

Gostaríamos de agradecer nosso orientador Danilo, por toda a ajuda e suporte durante o semestre para a realização do projeto.





6.Bibliografia
--------------

Indique os itens de bibliografia citados ou que auxiliaram seus estudos para o projeto, usando o estilo:

Livros:
Oppenheim, Alan V.; Schafer, Ronald W., Buck, John R. - Discrete Time Signal Processing – Prentice Hall – Segunda Edição - 1998

Artigos:
Horner,Andrew ;Beauchamp,James – Synthesis of Trumpet TonesUsing a Wavetable
and a Dynamic Filter – Journal of Audio Engineering Society – vol 43/n.10 – páginas 799-812 – Editora – 1995
