# Grupo 1A: Lêticia, Esther,  Lailson e Sophia.

# Plano - DESAFIO 1

**Definição do desafio:** 

Pensando especificamente no motor da nossa ferramenta, quais outras informações referentes aos usuários do Twitter seria possível extrair da API para melhorar nosso motor de análises? Nesse desafio, encaixam-se tanto a apresentação de uma análise teórica de quais parâmetros podem ser relevantes, bem como indicações de implementações que melhorem nosso motor atual. Entre informações que já utilizamos hoje, podemos citar o número de seguidores, últimos 100 tweets, horário de publicação, entre outros. Gostaríamos, portanto, de saber quais outras informações disponibilizadas pela API do Twitter podem agregar positivamente ao nosso motor de análises.


**Para início de conversa:**

- Aprender sobre as APIs do Twitter:
- As APIS estão divididas em 5 grupos:
Contas e usuários;
Tweets e respostas;
Mensagens diretas;
Anúncios;
Ferramentas de Publisher e SDKs.

**Perguntas norteadoras:**

- Quais grupos de servidores o Pegabot utiliza?
- Quais os critérios para identificar bots que o Pegabot utiliza atualmente? 
- Quais os dados disponibilizados pelo Twitter que podem servir para a identificação de bots?
- O que já existe em outros lugares, para detectar bots, e o Pegabot não faz?
- O que pode ser feito e ninguém fez ainda?

**Especificações:**

- Analisar detalhadamente os grupos de servidores do Twitter que o Pegabot utiliza;
- Embasar os resultados das pesquisas com fontes confiáveis.


# RESULTADOS DE PESQUISA:

MOTOR

**Dados mais utilizados: **
(informações retiradas do slide apresentado dia 02/09)
- Tempo mediano entre tweets;
- Retweets;
- Número de amigos;
- Tamanho do nome;
- Menor tempo entre tweets;
- Número de seguidores;
- Origem da postagem;
- Quantidade de hashtags.

**Informações detectadas:** 
(retiradas das planilhas disponibilizadas no drive do hackathon)

arquivo: handles_inct 
Variáveis: Indicam o comportamento dos usuários, identificam tipos de bots (foram feitas com base na consultoria da INCT.DD).

- TabelaAmostra. Link da conta no twitter.
- É bot? sim ou não;
- Se você fosse atribuir uma função, qual seria? Ex.: retweetar, publicar hashtags…
- Função #2? Ex.: atacar, publicar hashtag…
- Comportamento agressivo? sim ou não.
- Comportamento repetitivo com # ou menções? sim ou não.
- Parece só retweetar? sim ou não.
- Só compartilha links? sim ou não.
- Só faz comentários? sim ou não.
- Enaltece muito outros usuários? sim ou não.
- Faz muito uso de emojis? sim ou não.
- Tem muitos posts sem textos? sim ou não.
- handle. (nome de usuário).

arquivo: trends_dataclips_qijpjdyxutqsnrteglrjtwjhdjja
Variáveis: informações sobre trends do twitter

- id.
- trend_date_time. Dia (aaaa-mm-dd), horário (hh:mm:ss).
- trend. Nome da trend como hashtags ou palavras.
- user#_id. Ids dos usuários.
- tweet#. Texto do tweet referente ao id do usuário da coluna user#_id.

arquivo: inct_users
variáveis: análise de informações das contas do usuário.

- error. Ex.: usuário não encontrado, usuário foi suspenso.
- created_at. Data da criação da conta em dia (aaaa-mm-dd) e horário (hh:mm:ss).
- default_profile. Perfil padrão? verdadeiro ou falso.
- description. Bio do usuário.
- followers_count. Número de seguidores da conta.
- friends_count. Número de pessoas que está seguindo.
- handle. Nome de usuário da conta.
- lang. idioma.
- location. Cidade e país do usuário.
- name. Nome do perfil.
- profile_image. Imagem da conta.
- twitter_id. id da conta do twitter.
- twitter_is_protected. twitter protegido: verdadeiro ou falso.
- verified. Conta é verificada: verdadeiro ou falso.
- withheld_in_countries. (?)

arquivo: inct_timelines
variáveis: Análise dos tweets publicados.

- error.
- tweet_author. nome de usuário do autor do tweet.
- tweet_author_id. id da conta do usuário.
- tweet_contributors. Outros contribuidores do tweet.
- tweet_created_at. Data (aaaa-mm-dd) e horário (hh:mm:ss) de criação do tweet.
- tweet_favorite_count. Quantidade de likes no tweet.
- tweet_favorited. tweet marcado como favorito: verdadeiro ou falso.
- tweet_geo. 
- tweet_hashtags. hashtags usadas no tweet. 
- tweet_id. id do tweet.
- tweet_id_str. id em texto.
- tweet_is_retweet. O tweet é um retweet? verdadeiro ou falso.
- tweet_lang. Idioma do tweet.
- tweet_place. 
- tweet_retweeted. Tweet foi retweetado: verdadeiro ou falso.
- tweet_source. Tipo de dispositivo utilizado para criar o tweet.
- tweet_text. Texto do tweet.




**Dados a serem utilizados:**

**Objetivo:** Identificar a probabilidade de uma conta de usuário do twitter ser ou não um bot, além das formas já utilizadas, com o uso da análise de imagens.

**Dados: **

conteúdo de mídia dos tweets (vídeos e fotos).



