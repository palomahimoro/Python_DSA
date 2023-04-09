#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Condicionais if
if 5 > 2:
    print("A sentenca é verdadeira")


# In[2]:


#if, else
if 5 < 2:
    print("A sentenca é verdadeira")


# In[4]:


#if, else com variavel
dia = "terca"
if dia == "Segunda":
    print("Hoje faria sol:")
else:
    print("Hoje vai chover:")


# In[5]:


#podemos usar elif para validar mais de uma condicao
if dia == "Segunda":
    print("nao fara sol")
elif dia == "terca":
    print("vai chover")
else:
    print("sem previsao")


# In[6]:


#operadores relacionais (valor booleano)


# In[7]:


6 > 3


# In[8]:


3 > 7


# In[9]:


4 < 8


# In[10]:


4 >= 4


# In[11]:


if 5 ==5:
    print("testando")


# In[13]:


if True:
    print("parece ok")


# In[17]:


#atencao com a sintaxe (: margem e enter)
if 4 > 3:
    print("tudo ok")


# In[19]:


#condicionais aninhados
idade = 18
if idade > 17:
    print ("you can drive")


# In[28]:


nome = "bob"
if idade > 13:
    if nome == "bob":
        print("ok, bob")
    else:
        print("sorry bob")


# In[29]:


idade = 13
nome ="bob"
if idade >= 13 and nome == "bob":
    print("ok,bob")


# In[30]:


#operadores logicos
idade = 18
nome = "bob"
if idade > 17:
    print("you can drive")


# In[31]:


#operador and
numero = 4

if (numero >2) and (numero %2 == 0):
    print("isso esta 2 ok")


# In[32]:


numero = 4

if (numero >2) and (numero %2 == 0):
    print("isso esta 2 ok")
else:
    print("isso esta 2 nao")


# In[34]:


#operador or
numero = 4

if (numero > 5) or (numero % 2 == 0):
    print("isso esta 2 ok")


# In[35]:


#operador not
numero = 4

if (numero >2) and (numero %2 == 0):
    print("isso esta 2 ok")
else:
    print("isso esta 2 nao")


# In[37]:


#operador and, or e not

numero = 4

if (numero >2) and (numero %2 == 0) or (numero == 4):
    print("isso esta ok")


# In[38]:


#ex. com uso de variaveis

disciplina = 'data science'
nota_final = 70

if disciplina == 'data science' and nota_final >= 70:
    print("voce foi aprovado")
else:
    print("lamento, estudar mais")


# In[39]:


#usando mais de uma condicao na claususa if

disciplina = 'Data Science'
nota_final = 60

if disciplina == 'Data Science' and nota_final >= 70:
    print("voce foi aprovado")
else:
    print("lamento, estudar mais")


# In[50]:


#usando mais de uma condicao na clausula if e introduzindo placeholders (guardador de lugar)

disciplina = 'data science'
nota_final = 90
semestre = 2

if disciplina == 'data science' and nota_final >= 80 and semestre != 1:
     print("voce foi aprovado em %s com media final %r" %(disciplina, nota_fiscal)
else:
     print("lamento, estudar mais")           


# In[51]:


#loop for
#criando uma tupla 
tp = (2,3,4)
for i in tp:
    print(i)


# In[52]:


#criando uma lista
listadestrings = ["data", "science", "academy"]
for i in listadestrings:
    print(i)


# In[54]:


#valores no intervalo entre 0 e 5 
for contador in range (0,5):
    print(contador)


# In[55]:


#imprimindo os numeros pares da lista de numeros
lista = [1,2,3,4,5,6,7,8,9,10]
for num in lista:
    if num % 2 == 0:
        print(num)


# In[56]:


#listando os numeros no intervalo entre 0 a 101, com incremento em 2
for i in range (0, 101, 2):
    print (i)


# In[58]:


#strings tambem sao sequencias
for caracter in "Python legal":
    print(caracter)


# In[63]:


#loops aninhados

lista1 = [0,1,2,3,4]
lista2 = [1,2,3]

#loop externo
for elemento_lista1 in lista1:
    
    #loop interno
    for elemento_lista2 in lista2:
        
        print('\n', elemento_lista1 * elemento_lista2)
        
    print('----')


# In[3]:


#loop for aninhado
lista1 = [0,1,2,3,4]
lista2 =[1,2,3]


# In[2]:


#loop externo
for elemento_lista1 in lista1:
    
    #loop interno
    for elemento_lista2 in lista2:
        
        print('\n', elemento_lista1 * elemento_lista2)
        
        print('----')


# In[4]:


#o numero 47 aparece nas duas listas?

lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]

#loop externo
for elemento_lista1 in lista1:
    
    #loop interno
    for elemento_lista2 in lista2:
        
        #condicional
        if elemento_lista1 == 47 and elemento_lista2 == 47:
            
            print("O numero 47 foi encontrado nas duas listas")


# In[5]:


lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]
soma = 0

#loop externo
for lista in [lista1, lista2]:
    
    #loop interno
    for num in lista2:
        
        #condicional
        if num % 2 == 0:
            soma += num

print("O soma dos numeros pares das duas listas e igual a soma a", soma)


# In[6]:


#lista concatenada em python
lista1 + lista2


# In[7]:


#some os numeros pares da primeira lista com os numeros pares da segunda lista

lista1 =[10,16,24,39,47]
lista2 = [32,89,47,76,12]
soma = 0

for num in lista1 + lista2:
    if num % 2 == 0:
        soma += num
        
print("soma dos valores pares:", soma)


# In[9]:


#loop em lista de listas (matrizes) para encontrar o maior numero

matriz = [[42, 23, 34], [100,214, 114], [10.1, 98.7, 12.3]]
maior_numero= 0

#loop externo
for linha in matriz:
    
    #loop interno
    for num in linha:
        
        #condicional
        if num > maior_numero:
            maior_numero = num
print("maior numero:", maior_numero)


# In[12]:


#listando as chaves de um dicionario
dict = {'k1':'python','k2':'R', 'k3':'Scala'}
for item in dict:
    print(item)


# In[13]:


#imprimindo chave e valor do dicionario. Usando o metodo items(0) para retornar os  itens do dicionario
for k,v in dict.items():
    print(k,v)


# In[ ]:


#loop while

