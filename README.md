# t3_projeto_otimizicao_algoritmos
## Os dominós
O jogo de dominós tem pecinhas retangulares com um número em cada ponta. Em nossa versão do jogo de dominó, a numeração em cada ponta pode ir de 0 a 10. Depois, as peças podem ser unidas, ponta com ponta, formando uma longa cadeia desde que os números nas pontas que estão sendo unidas sejam os mesmos.  
Sua missão é ler um conjunto de peças de dominó e dizer se existe uma forma de colocá-las todas em uma longa cadeia.  
Você deve escrever um algoritmo baseado em backtracking que leia a configuração do jogo via entrada padrão (como a que está ao lado) e responda se há maneira de resolver o problema, mostrando-a se existir. 

A entrada tem o seguinte formato:  
O número n de peças de dominó.  
Os dois números nas pontas de cada uma das n peças a serem lidas.  
Uma solução possível para o caso ao lado seria esta:  
6  
4 2  
3 4  
8 1  
1 7  
4 7  
2 8  
  
Uma solução esperada para o problema seria essa:  
34 47 71 18 82 24  
E a saída esperada é:    
344771188224  

Ou uma mensagem informando que não existe solução, se for o caso.
