import random
#1. Vytvoření pole s 10 náhodnými čísly
array = [74, 45, 0, 15, 3, 69, 46, 19, 85, 100]

print("--------------- Bubble sort ------------")
#2. Bubble sort 
def bubble_sort(array):
    #Délka pole
    n = len(array)
    #Pocházení celého pole
    for i in range(n):
        #Cyklus pro porovnání sousedních prvků
        for j in range(0, n-i-1):
            #Přehodí prvek vlevo s pravým prvkem, pokud je větší než prvek v pravo
            if array[j] > array[j+1]:
                #Výměna
                array[j], array[j+1] = array[j+1], array[j]
        #Po každé iteraci vypíše aktuální stav cylku ve vnitř
        print(array)
bubble_sort(array)

print("-------------- Bogo sort --------------")
#3. Bogo sort
def bogo_sort(array):
    #While not all opakuje smyčku, dokud pole není seřazené
    while not all(array[i] <= array[i + 1]
        #Kontroluje každou dvojici sousedních prvků
        for i in range(len(array) - 1)):
        #Pokud pole není seřazené tak se náhodně promíchá
        random.shuffle(array)
bogo_sort(array)
print("Seřazené pole:", array)

print("------------ Selection sort ---------")
#4. Selection sort
def selection_sort(array):
    #Délka pole
    a = len(array)
    #Procházení celého pole
    for i in range(a):
        #Min_index najde nejmenší hodnotu prvku od i do a
        min_index = i
        #Prohledává zbytek pole od indexu i+1
        for j in range(i + 1, a):
            #Pokud je aktuální prvek menší než dosud nejmenší, aktualizujeme min_index
            if array[j] < array[min_index]:
                #Nastavení nového indexu pro nejmenší prvek
                min_index = j
        # Prohodí nejmenší prvek se začátkem nezpracované části
        array[i], array[min_index] = array[min_index], array[i]

selection_sort(array)
print("Seřazené pole:", array)

print("------------ Insertion sort ---------")
#5. Insertion sort
def insertion_sort(array):
    #Prochází se pole od druhého indexového čísla (první je už seřazené)
    for i in range(1, len(array)):
        k = array[i]  #Aktuální prvek, který chceme vložit na správné místo
        j = i - 1       #Index předchozího prvku
        #Posunuje prvky, které jsou větší než 'k', doprava
        while j >= 0 and array[j] > k:
            #Posunuje prvek na pozici j o jednu doprava
            array[j + 1] = array[j]
            j -= 1 
        #Vložení "k" na správné místo                 
        array[j + 1] = k
        
insertion_sort(array)
print("Seřazené pole:", array)
