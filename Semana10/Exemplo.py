from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[2]","ContarPalavrasStreming")

ssc = StreamingContext(sc, 10)

#Endereço VM ubunto localhost 3456 bridget
dados = ssc.socketTextStream("192.168.0.16",3456)

palavras = dados.flatMap(lambda linha: linha.split(" "))

pares = palavras.map(lambda palavra: (palavra, 1))

contagem = pares.reduceByKey(lambda x,y : x + y)

contagem.pprint()

