
##ITERATOR CREATED THROUGH A CLASS
import time

class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()


    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


my_sentence = Sentence('this is a test')

for letter in my_sentence:
    print(letter)


print()
time.sleep(1)


## CREO UNA FUNCION GENERADORA QUE TRABAJA IGUAL QUE EL ITERADOR, EL GENERADOR QUE SE CREA (my_sentence) 
#ES TAMBIEN UN ITERADOR
    
## GENERATOR FUNCTION, IS ALSO AN ITERATOR



def sentence(sentence):
    for word in sentence.split():
        yield word


my_sentence = sentence('Joa mañana juega contra Atenas')




#LOOP COMUN AL ITERADOR Y AL GENERADOR ITERADOR
for word in my_sentence:
    print(word)

print()
time.sleep(1)


##GENERADOR CREADO POR COMPREHENSION
x = (i for i in range(5))
print(x)

for n in x:
    print(n)

