from random import *
import os
import time



def checks_in_vector(vector, arr_len, bot, top):
    num = randint(bot, top)
    for element in vector:
        if element == num:
            num = checks_in_vector(vector, arr_len, bot, top)

    return num

def randomize_vector(bot, top, arr_len):
    vector = []
    for x in range (0, arr_len ):
        value = checks_in_vector(vector, arr_len, bot, top)
        vector.append(value)
    return vector

def randomize_vector_repeat(bot, top, arr_len):
    vector = []
    for x in range (1, arr_len ):   
        vector.append(randint(bot, top))
    return vector


def insertion_sort( lista ):
  for i in range( 1, len( lista ) ):
    chave = lista[i]
    k = i
    while k > 0 and chave < lista[k - 1]:
        lista[k] = lista[k - 1]
        k -= 1
    lista[k] = chave

def float_vector(vector):
    for x in range(len(vector)):
        vector[x] = float(vector[x])

    return vector


def vector_arg(vector):
    arg = 0
    float(arg)
    for x in range(1, len(vector)):
        if((vector[x] != vector[x-1])):
            const = (1/(vector[x]-vector[x-1]))
        else:
            const = 1
        
        if vector[x] > vector[x-1]:
            aux = arg
            arg = aux + const
        else:
            aux = arg
            arg = arg + const
        
    
    return arg / (len(vector) - 1) 

#vector = []
#vector = float_vector(randomize_vector(1, 11, 10, vector))
#vector = float_vector(vector)

#print vector
#print(vector_arg(vector))
#vector = vector[::-1]
#print vector
#print(vector_arg(vector))
#insertion_sort(vector)
#print(vector)    
#print(vector_arg(vector))
        
#start_time = time.time()

def insertion_option():
    os.system('clear') 
    print("Criacao do vetor de ordenacao\n")
    print("Vetor com repeticao[1]")
    print("Vetor sem repeticao[2]")
    vectortype = input("Digite a opcao: ")
    if (vectortype == 1):
        arr_len = input("Digite a o tamanho desejado do vetor: ")
        bot = input("Digite a o limite inferior do vetor: ")
        top = input("Digite a o limite superior do vetor: ")
        if (top == bot):
            print("Intervalo de numeros deve ter ao menos 2 numeros\n")
            action = input("Digite 1 para tentar novamente: ")
            if action == 1:
                insertion_option()
            else:
                show_menu()
        else:
            arr = float_vector(randomize_vector_repeat(bot, top, arr_len))
            print(arr)
            arr2 = arr[::-1] 
            score = vector_arg(arr)
            os.system('clear') 
            print("Utilizando diretamente o Insertion Sort no vetor, o tempo necessario para ordenar foi: ")
            start_time1 = time.time()
            insertion_sort(arr)
            time1 = time.time() - start_time1
            print(time1)
            print("O escore do vetor inicial no algoritimo de ordenacao foi: ")
            print(score)
            if(score < 0):
                print("Como o escore foi negativo, o vetor foi invertido para a comparacao de resultado.")
                
                print("O tempo necessario para ordenar o vetor invertido foi: ")
                start_time2 = time.time()
                score = vector_arg(arr)
                insertion_sort(arr2)
                time2 = time.time() - start_time2
                print(time2)
                relation = 100 * time2 / time1
                print("A porcentagem de tempo em relacao a primeira ordenacao foi: ")
                print(relation)
            else:
                print("Como o escore foi positivo, nao ha necessidade de inversao do vetor.")

###########################################################################


###########################################################################
    elif (vectortype == 2):
        arr_len = input("Digite a o tamanho desejado do vetor: ")
        bot = input("Digite a o limite inferior do vetor: ")
        top = input("Digite a o limite superior do vetor: ")
        if (arr_len > (top - bot + 1)):
            print("Intervalo de numeros menor que tamanho do vetor\n")
            action = input("Digite 1 para tentar novamente: ")
            if action == 1:
                insertion_option()
            else:
                show_menu()
        else:
            arr = float_vector(randomize_vector(bot, top, arr_len))
            arr2 = arr[::-1] 
            score = vector_arg(arr)
            os.system('clear') 
            print("Utilizando diretamente o Insertion Sort no vetor, o tempo necessario para ordenar foi: ")
            start_time1 = time.time()
            insertion_sort(arr)
            time1 = time.time() - start_time1
            print(time1)
            print("O escore do vetor inicial no algoritimo de ordenacao foi: ")
            print(score)
            if(score < 0):
                print("Como o escore foi negativo, o vetor foi invertido para a comparacao de resultado.")
                
                print("O tempo necessario para ordenar o vetor invertido foi: ")
                start_time2 = time.time()
                score = vector_arg(arr)
                insertion_sort(arr2)
                time2 = time.time() - start_time2
                print(time2)
                relation = 100 * time2 / time1
                print("A porcentagem de tempo em relacao a primeira ordenacao foi: ")
                print(relation)
            else:
                print("Como o escore foi positivo, nao ha necessidade de inversao do vetor.")






def show_menu():
    os.system('clear') 
    print("================================================\n")
    print("================ Insertion Sort ================\n")
    print("================================================\n")

    print("           Selecione o Metodo de Ordenacao      \n")
    print("   1)Insertion Sort\n")

    print("================================================\n")
    print("      Felipe Campos e Joao Egewarth, EDA2       \n")
    print("================================================\n")

    option = input("Insira uma opcao valida: ")
    
    if option == 1:
        insertion_option()
    else:
        show_menu()



show_menu()
