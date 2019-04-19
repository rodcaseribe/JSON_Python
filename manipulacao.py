import sys
import json
import string
from pprint import pprint
import re
from json.decoder import JSONDecoder
import os

#---------------------------------------------------------------------------------------------------------------------------------
##MENU PRINCIPAL

def main():
    menu()

def menu():
    
    
    print "\n\n   Processo Seletivo Raccoon  -( T.I )\n"
    print "Candidato-> Rodolfo Casemiro Ribeiro    "
    print "¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨\n"
    print "Menu de Funções:\n\nDigite:"
    print "  (1)  para  Impressão e Substituição De Elementos [name] do JSON"
    print "  (2)  para  Impressão e Substituição De Elementos [price] do JSON"
    print "  (3)  para  Impressão e Checagem De Elementos [quantity] e gerar JSON Corrigido"
    print "  (4)  para  Ordenando por ordem alfabética a [category] seguido de seu [name]"
    print "   e   para  Ordenar por ordem numérica crescente o [id] seguido de seu [name]"
    print "  (5)  para  Calcular o Valor Total do estoque de cada categoria."
    entrada = raw_input(":")    
    if (entrada) == "1":
        decodificacao()
        funcao1()   
    if (entrada) == "2":
        decodificacao()
        funcao2()
    if (entrada) == "3":
        decodificacao()
        funcao3()
    if (entrada) == "4":
        decodificacao()
        funcao4()
    if (entrada) == "5":
        decodificacao()
        funcao5()   
    else:
        main()

#---------------------------------------------------------------------------------------------------------------------------------
##DECODIFICACAO

def decodificacao():  
    with open('broken-database.json') as json_file:                         #abrindo JSON e Carregando
        data = json.load(json_file)
        #data
        #print(data)                                                        #conferindo
        #print type(data)                                                   #conferindo type
        resultado = str(data)                                               #transformando em string
       
        resultado2 = resultado.replace("\\xf8", 'o')                        #Substituicao de elementos
        resultado2 = resultado2.replace("\\xe6", 'a')
        resultado2 = resultado2.replace("\\xa2", 'c')
        resultado2 = resultado2.replace("\\xe7", 'c')
        resultado2 = resultado2.replace("\\xe9", 'e')    
        resultado2 = resultado2.replace("\\xdf", 'b')
        resultado2 = resultado2.replace("\\xe3", 'a')
        resultado2 = resultado2.replace("\\xf4", 'o')
        resultado2 = resultado2.replace("\\u201d", ' ')
        resultado2 = resultado2.replace("\\xf3", 'o')
        resultado2 = resultado2.replace("'", '"')
        resultado2 = resultado2.replace('u"', '"')
                                              
        arquivo = open('broken-database-Limpo.json','w')                    #Gravando o arquivo total decodificado
        arquivo.write(resultado2)
        arquivo.close()
        #print "\nArquivo gerado com sucesso!\n"
           
#---------------------------------------------------------------------------------------------------------------------------------
##FUNCAO1
def funcao1():
    print "(1) - Impressão/Gravação/Substituição De Elementos (Name) do JSON\n" 
    with open('broken-database-Limpo.json') as json_file2:                  #Abrindo o arquivo e printando apenas [name]
        data = json.load(json_file2)
        open("Textos_Puros/name.txt", "w").close()                          #Limpando Arquivo
        for i in data:
           print (i['name'])                                                #Printando [name]
           arquivo = open('Textos_Puros/name.txt','a')                      #Gravando separacao(txt)
           arquivo.write(i['name']+"\n")
           arquivo.close()
        print "\nArquivo gerado: names.txt!\n"
        
#---------------------------------------------------------------------------------------------------------------------------------
##FUNCAO2
      
def funcao2():
    open("broken-database_price.json", "w").close()
    print "(2) - Impressão/Gravação/Substituição De Elementos (price) do JSON\n" 
    with open('broken-database-Limpo.json') as json_file2:                  #Abrindo o arquivo e printando apenas [price]
        data = json.load(json_file2)
        open("Textos_Puros/price.txt", "w").close()                         #Limpando Arquivo
        
        for i in data:
            print (i['price'])                                              #Printando [price]
            i['price'] = float(i['price'])                                  #Passando pra float, removendo aspas dupla
            with open("broken-database_price.json",'a') as json_file2:      #Modificando
                json.dump(i,json_file2)
                arquivo2 = open('Textos_Puros/price.txt','a')               #Gravando separacao(txt)
                arquivo2.write(str(i['price'])+"\n")       
                arquivo2.close()
        print "\nArquivo gerado com sucesso: price.txt!"
        print "Arquivo gerado com sucesso: broken-database_price.json!"
        
        
    
#---------------------------------------------------------------------------------------------------------------------------------
##FUNCAO3
def funcao3():
    print "(3) - Impressão/Gravação/Substituição De Elementos (quantity) do JSON\n" 
    with open('broken-database-Limpo.json') as json_file2:                  #Abrindo o arquivo e printando apenas [quantity]
        data = json.load(json_file2)
        open("Textos_Puros/quantity.txt", "w").close()                      #Limpando separacao(txt)

        arquivo3 = open("broken-database-final.json", "w")                  #Criando um ponto de Referencia no TOPO do JSON NOVO
        arquivo3.write("xxxxx")
        arquivo3.close()                                                    


        for i in data:
           try:                                       
              print(i['quantity'])
              i['price'] = float(i['price'])                                #Transformando em float removendo aspas dupla
              with open("broken-database-final.json",'a') as json_file2:    #Acrescentando no JSON NOVO
                 json.dump(i,json_file2)                                    #Gravando tudo de data
                 arquivo3 = open('broken-database-final.json','a')          #Gravando no JSON NOVO
                 arquivo3.write(',')                                        #Por isso uso replace p/ TOPO
                 arquivo3.close()
                 arquivo2 = open('Textos_Puros/quantity.txt','a')           #Gravando em texto puro(txt)
                 arquivo2.write(str(i['quantity'])+"\n")                
                 arquivo2.close()
           except KeyError:                                                 #Tratando excessão
              i['quantity'] = '0'
              i['quantity'] = int(i['quantity'])                            #Transformando em int, remover aspas dupla
              i['price'] = float(i['price'])                                #Transformando em float removendo aspas dupla
              with open("broken-database-final.json",'a') as json_file2:    #Acrescentando no JSON NOVO
                 json.dump(i,json_file2)
                 print(str(0))                                              #Printando 0
                 arquivo4 = open('broken-database-final.json','a')          #Gravando no JSON NOVO
                 arquivo4.write(",")       
                 arquivo4.close()
                 arquivo2 = open('Textos_Puros/quantity.txt','a')           #Gravando em texto puro(txt)
                 arquivo2.write(str(0)+"\n")       
                 arquivo2.close()
        print "\nArquivo gerado: quantity.txt!\n"

        
    with open('broken-database-final.json', 'r') as test:                   #Removendo ponto de Referencia no TOPO do JSON NOVO
          test=test.read().replace("xxxxx,", '[')                           #Adicionando [ com replace no TOPO
    with open('broken-database-final.json' , 'w') as f:
          f.write(test)

    arquivo4 = open('broken-database-final.json','a')     
    arquivo4.write("]")                                                     #Adicionando no final ] no final do JSON NOVO
    arquivo4.close()
    print "\nArquivo JSON gerado: broken-database-final.json!\n"


#---------------------------------------------------------------------------------------------------------------------------------
#FUNCAO4

def Func(i):
  return i['category']                                                      #Elemento principal de referencia1

def Func2(i):
  return i['id']                                                            #Elemento principal de referencia2

def funcao4():
    open("cat_nome.txt", "w").close()
    open("id_nome.txt", "w").close()
    with open('broken-database-final.json') as json_file2:                  #Abrindo o arquivo e carregando
        data = json.load(json_file2)
        data.sort(key=Func)                                                 #Chamando ponto de referencia1 na funcao
        print "\n-->Ordenando por ordem alfabetica a categoria seguido de seu nome!\n"
        for i in data:
            print (i['category']+"\n"+i['name']+"\n")
            arquivo2 = open('cat_nome.txt','a')                             #Gravando(txt)
            arquivo2.write(i['category']+"\n"+i['name']+"\n")       
            arquivo2.close()
    with open('broken-database-final.json') as json_file2:       
        data = json.load(json_file2)
        data.sort(key=Func2)                                                #Chamando ponto de referencia2 na funcao
        print "\n-->Ordenando por ordem numerica crescente o id seguido de seu nome!\n"
        for i in data:
            print (str(i['id'])+"\n"+i['name']+"\n")
            arquivo2 = open('id_nome.txt','a')                              #Gravando(txt)
            arquivo2.write(str(i['id'])+"\n"+i['name']+"\n")       
            arquivo2.close()
        print "\nArquivo gerado categoria e nome: cat_nome.txt"
        print "Arquivo gerado de id e nome: id_nome.txt"
#---------------------------------------------------------------------------------------------------------------------------------            
#FUNCAO5
            
def funcao5():
    open("estoque_categoria.txt", "w").close()
    open("estoque_total.txt", "w").close()
    with open('broken-database-final.json') as json_file2:                  #Abrindo o arquivo e carregando
        data = json.load(json_file2)
        c =0
        d =0
        for i in data:
            d += c
            a = (i['price'])
            a = float(a)
            b = (i['quantity'])
            b = float(b)
            c =a*b
            print "Valor total de estoque por categoria: ",i['category'],c
            arquivo2 = open('estoque_categoria.txt','a')                    #Gravando(txt)
            arquivo2.write(i['category']+"\n"+str(c)+"\n")
            arquivo2.close()
        print "\nValor total de todos os Estoques: ",d     
        arquivo2 = open('estoque_total.txt','a')                            #Gravando(txt)
        arquivo2.write(str(d))       
        arquivo2.close()
        print "\nArquivo gerado de estoque por categoria: estoque_categoria.txt"
        print "Arquivo gerado de estoque total: estoque_total.txt"
        
main()    
