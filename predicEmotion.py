import pandas as pd
import nltk
import sys

#ler o ficheiro excel com as frases de treinamento
df=pd.read_excel('Hackaton Pegabot_Frases de treinamento.xlsx', sheet_name = 'Página1')

#eliminar as Stopwords que não acrescentam nada ao sentido da frase mas podem gerar ruído
stopwords=nltk.corpus.stopwords.words('portuguese')

#Remoção de sufixos para normalizar as palavras
def doStemmer(df):
    stemmer = nltk.stem.RSLPStemmer()
    phrasesStemming = []
    for i in range(df.shape[0]):
        phrase = df.iloc[i,2]
        emotion = df.iloc[i,4]
        comStemming = [str(stemmer.stem(p))
                       for p in phrase.split() if p not in stopwords]
        phrasesStemming.append((comStemming, emotion))
    return phrasesStemming


phrasesWithStemming = doStemmer(df)


def getWords(phrases):
    dictOfWords = []
    for (words, emotion) in phrases:
        for word in words:
            dictOfWords.append(word)
    return dictOfWords


words = getWords(phrasesWithStemming)

#calcular a frequência com que aparece cada palavra

def calcFrequency(words):
    words = nltk.FreqDist(words)
    return words

frequency = calcFrequency(words)

#obter um dicionário de palavras únicas
def getUnicWords(frequency):
    freq = frequency.keys()
    return freq

unicWords = getUnicWords(frequency)


#Retorna true ou false uma nova frase, caso a palavra seja encontrada ou não dentro do dicionário
def pullWords(doc):
    doc = set(doc)
    features = {}
    for words in unicWords:
        features['%s' % words] = (words in doc)
    return features


completeDataset = nltk.classify.apply_features(pullWords,phrasesWithStemming)

#construir a tabela de probabilidades
classifier = nltk.NaiveBayesClassifier.train(completeDataset) 

#print(classifier.labels())
#print(classifier.show_most_informative_features(5))


#função principal para avaliar a emoção
def predictEmotion(phrase):
    result = 'unknow'
    testStem = []
    stemmer = nltk.stem.RSLPStemmer()
    for (words) in phrase.split():
        comStem = [p for p in words.split()]
        testStem.append(str(stemmer.stem(comStem[0])))

    newPhrase = pullWords(testStem)
    distribution = classifier.prob_classify(newPhrase)
    for class_ in distribution.samples():
        print("%s: %f" % (class_, distribution.prob(class_)))
        if distribution.prob(class_) > 0.5:
            result = class_
    return result
    


def main(argv):
    phrase = ""

    try:
        phrase = sys.argv[1]
    except:
        print ('usage: predictEmotion.py "your phrase"')
        sys.exit()
    
    predEmotion = predictEmotion(phrase)
    print ('------------------------')
    print ('Resultado:', predEmotion)

if __name__ == "__main__":
   main(sys.argv[1:])

'''
#Frases de teste 
test = 'que maravilhoso ver este pessoal. Estou tão feliz! '   # Alegria
test = 'são todos uns ladrões'   # Raiva
test = 'que merda é esta. Não me apanham noutra' # Insatisfação
'''
