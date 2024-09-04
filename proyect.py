import parte1 as p1


def main():
    print("Transmission 1: ")
    print("mcode1: ")
    p1.analyze_files('./texts/transmission1.txt','./texts/mcode1.txt')
    print("mcode2: ")
    p1.analyze_files('./texts/transmission1.txt','./texts/mcode2.txt')
    print("mcode2: ")
    p1.analyze_files('./texts/transmission1.txt','./texts/mcode3.txt')
    
    print(" ")
    print("Transmission 2: ")
    print("mcode1: ")
    p1.analyze_files('./texts/transmission2.txt','./texts/mcode1.txt')
    print("mcode2: ")
    p1.analyze_files('./texts/transmission2.txt','./texts/mcode2.txt')
    print("mcode3: ")
    p1.analyze_files('./texts/transmission2.txt','./texts/mcode3.txt')

if __name__ == "__main__":
    main()

    