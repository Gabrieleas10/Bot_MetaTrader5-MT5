# Bot_MetaTrader5-MT5
 
 Bot identificador de oportunidades de comprar/vender ações da Bolsa Brasileira.

# Disclaimer:

O objetivo desses algoritmos são apenas para compartilhar informações e contribuir com a comunidade, e não tem a finalidade de fazer qualquer indicação de plataforma, indicador ou ativo.
# Objetivo:

A partir de análises quantitativas massiva de diversos ativos é possível identificar ações da B3 (bolsa brasileira) em que se encontram em bom momento para compra ou venda e executar assim operações conhecidas como swing trade.

# Pré-Requisitos:

1 - Possuir uma conta em uma corretora que tenha acesso a plataforma MetaTrader 5. (Eu uso a Corretora Clear)

2 - Instalar o software gratuito MetaTrader 5. link: https://www.metatrader5.com/pt/download

3 - Instalar as bibliotecas: MetaTrader5 e finta.

Documentação Oficial: https://www.mql5.com/pt/docs/integration/python_metatrader5

# Descrição:

Primeiro, vamos dar uma visão geral dos indicadores utilizados: Indice de Força Relativa(IFR ou RSI do inglês) e o conceito de médias móveis.

## Relative Strength Index (RSI) ou Indice de Força Relativa (IFR):

Esse indicador através de cálculos matemáticos levando em consideração os preços e sua variação ele estima quando um ativo está sobrevendido ou sobrecomprado. Ou seja, quando o mercado está com o caráter sobrevendido pode ser uma boa oportunidade de compra do ativo esperando uma possível recuperação do ativo e o contrário é verdadeiro para o sobrecomprado.

Segundo a literatura, por convenção, um ativo está sobrevendido quando seu RSI está menor que 30-25 e sobrecomprado quando maior que 75-80. Então, o algortimo mapeia em que dias esses eventos ocorrem para diversos ativos.

![Alt text](https://goldenbrokersmy.azureedge.net/726/kAgX5MPoCaAvJcuy-unnamed.png)

## Médias Móveis:

Outro indicador utilizado foram as médias móveis, amplamente conhecidas. Esse indicador tem a função de evidenciar uma tendência do ativo, ou seja quando a médias móveis estão crescendo o ativo tende a subir e o contrário é verdadeiro. É uma estratégia bastante utilizada a combinação de médias móveis de períodos distintos, pois essa combinação evidencia se a tendência de subir ou cair é de curto, médio ou longo prazo.

Uma estratégia que se utiliza para início de tendência de alta ou baixa é o cruzamento de médias móveis. E essa é a estratégia que o _script_ se utiliza. As médias utilizadas no estudo são 4, 17 e 55 períodos.

![Alt text](https://http2.mlstatic.com/D_NQ_NP_863494-MLB26543296838_122017-O.jpg)
