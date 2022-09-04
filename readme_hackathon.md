# Identificar Emoções

## Descrição

Este pequeno projeto foi desenvolvido para responder ao desafio do Hackathon da Pegabot.
O nosso desafio estava voltado para a categoria 3, das Narrativas sobre Automação & Desinformação. 

Depois de ficarmos por dentro do projeto do Pegbot, vimos uma oportunidade de trazer valor ao projeto criando um mecanismo baseado em Machine Learning para avaliar a emoção associada a uma mensagem de twitte.

## Software usado

Foram usados as seguintes versões de uma solução em python: <br>
	- python 3.7.9<br>
	- panda 1.3.5<br>
	- nltk 3.6.7<br>

Mas deve funcionar em versões mais recentes.

## Como está organizado

É muito simples, tem apenas 4 ficheiros

| Ficheiro | Descrição |
| ----------- | ------------ |
| predicEmotion.py | Contém todo o código do algoritmo. Lê as informações do dataset externo (no caso um excel), prepara os mesmos em vetores e calcula probabilística. Depois do modelo criado tem uma função "predictEmotion" que retorna a label classificada, caso tenha uma probabilidade maior de 50% ou "unknow" para evitar falsas respostas. |
| Hackaton Pegabot_Frases de treinamento.xlsx | Representa o nosso dataset com apenas 37 frases de twittes recolhidos e classificados por nós numa das 3 categorias (raiva, insatisfação e alegria) |
| readme_hackathon.md | Este mesmo ficheiro que mostra um resumo do projeto na vertente técnica. |
| Resultado_Testado.PNG | É uma imagem de teste com novas frases que não fazem parte das frases que foram usadas para treinar o modelo probabilístico |

De realçar que o projeto, apesar de estar pronto a funcionar, ainda necessita de trabalho na construção de um dataset bem maior (com milhares de frases e equilibrado pelas emoções) e talvez alargar a novas emoções.

Dado o número de frases ser muito pequeno, por volta de ~10 frases por cada emoção, se as novas frases forem completamente descontextualizadas a performance de acerto poderá ser desastrosa. Por isso que é tão importante ter volume no treinamento do modelo, onde poderá ser reservado 80% das frases para treino e 20% para validação do processo. Algo que não foi feito devido ao tempo curto que tínhamos e ao tamanho do nosso dataset.

O código está preparado para ser integrado em uma API do pegabot, bastando fazer importe do ficheiro.

É provável que tenha que instalar o dataset para a língua em português da biblioteca nltk:
> nltk.download('rslp')

Todo o código está comentado por forma a simplificar a compreenção do mesmo, seguindo as boas práticas de nomenclatura dos nomes. Apesar dos comentários estarem em português, todo o código está escrito em inglês.

## Roadmap

Embora já tenha dado a entender anteriormente alguns pontos, segue aqui uma sugestão para próximos passos:

* Aumentar drasticamente o dataset, e classificar as labels (emoções)
* Validar se não faz sentido criar novas emoções, olhado para as mensagens dos twittes
* Dado o twitter funcionar com outros mídias,  como video/imagem/voz, criar conversor destes formatos para texto a fim de poderem ser submetidos ao algorítmo

## Equipa

A equipa é composta por:

* Adriana Melo - adrianapoletime@gmail.com
* Maria Carolina - s.mcarolinam@gmail.com
* Sofia Figueira - figueira.b.sofia@gmail.com
* Domingos Lemos - dalemos1@gmail.com

## Conclusão

É possível simplificar o código neste tipo de projeto, recorrendo a ML. 

Dado o pouco tempo, não nos foi possível explorar outras técnicas ou ter um processo de recolha dinâmica de twittes. Mas dentro dos limites dá para ver resultados positivos.

Estes resultados, de poder classificar um twitte em relação à emoção pode agregar valor em conjunto com outras features que já trabalham, por forma a estudarem o comportamento dos humanos versos bots. Podem também usar para colocar mais uma informação no vosso relatório do pegabot e por fim, para ajudar a automatizar a classificação de novos datasets que vos possam ser solicitados para análise. 

![image](https://user-images.githubusercontent.com/76813386/188335327-2ae5e1b9-3c8d-4a2d-899b-22ec0eaa9f29.png)
