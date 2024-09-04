import parte1 as p1

def printParte1():
    transmissions = ['./texts/transmission1.txt', './texts/transmission2.txt']
    mcodes = ['./texts/mcode1.txt', './texts/mcode2.txt', './texts/mcode3.txt']

    # Analizar cada archivo de transmisión
    for i, trans in enumerate(transmissions, start=1):
        print(f"Transmission {i}: ")
        for j, mcode in enumerate(mcodes, start=1):
            print(f"mcode{j}: ")
            p1.analyze_files(trans, mcode)
        print(" ")

def main():
    printParte1()

if __name__ == "__main__":
    main()

    