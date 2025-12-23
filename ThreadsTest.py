import multiprocessing
import time

def mottagare(queue):
    """Denna funktion körs i en egen process och väntar på meddelanden."""
    print("Mottagare: Startad och väntar på meddelanden...")
    while True:
        # Hämtar meddelande från kön (blockerar tills ett finns)
        meddelande = queue.get()
        
        if meddelande == "STOPP":
            print("Mottagare: Avslutar...")
            break
            
        print(f"Mottagare: Aggerar på meddelandet: '{meddelande}'")
        time.sleep(1) # Simulerar arbete

def avsandare(queue):
    """Denna funktion körs i en annan process och skickar meddelanden."""
    meddelanden = ["Hej!", "Kör igång processen", "Optimera datan"]
    
    for m in meddelanden:
        print(f"Avsändare: Skickar '{m}'")
        queue.put(m)
        time.sleep(2)
    
    queue.put("STOPP")

if __name__ == "__main__":
    # Skapa en delad kö
    kommunikations_ko = multiprocessing.Queue()

    # Skapa de två processerna
    p1 = multiprocessing.Process(target=mottagare, args=(kommunikations_ko,))
    p2 = multiprocessing.Process(target=avsandare, args=(kommunikations_ko,))

    # Starta processerna
    p1.start()
    p2.start()

    # Vänta på att båda ska bli klara
    p1.join()
    p2.join()
    
    print("Programmet har avslutats.")


# import threading
# import time

# # Funktion för den första tråden
# def tråd_funktion_1():
#     print("Tråd 1: Startar...")
#     for i in range(5):
#         print(f"Tråd 1: {i}")
#         time.sleep(1) # Simulerar arbete
#     print("Tråd 1: Klar!")

# # Funktion för den andra tråden
# def tråd_funktion_2():
#     in_str = input("Tråd 2: Skriv något > ")
#     print(f"Tråd 2: Du skrev: {in_str}")
#     print("Tråd 2: Klar!")

# # --- Huvudprogrammet ---
# if __name__ == "__main__":
#     print("Huvudprogram: Skapar trådar.")

#     # Skapa trådobjekt
#     t1 = threading.Thread(target=tråd_funktion_1, name="MinTråd1")
#     t2 = threading.Thread(target=tråd_funktion_2, name="MinTråd2")

#     # Starta trådarna
#     t1.start() # Anropar tråd_funktion_1
#     t2.start() # Anropar tråd_funktion_2

#     print("Huvudprogram: Trådar är startade. Väntar på att de ska bli klara.")

#     # Vänta på att båda trådarna ska slutföras
#     t1.join()
#     t2.join()

#     print("Huvudprogram: Båda trådarna är färdiga. Programmet avslutas.")