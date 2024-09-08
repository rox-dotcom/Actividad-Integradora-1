def longest_palindrome(text):
    n = len(transformed_text)
    P = [0] * n
    C = 0  
    R = 0  

    for i in range(n):
        mirror = 2 * C - i
        
        if i < R:
            P[i] = min(R - i, P[mirror])

        a = i + P[i] + 1
        b = i - P[i] - 1
        while a < n and b >= 0 and transformed_text[a] == transformed_text[b]:
            P[i] += 1
            a += 1
            b -= 1

        if i + P[i] > R:
            C = i
            R = i + P[i]

    max_len = max(P)
    center_index = P.index(max_len)

    start = (center_index - max_len) // 2
    end = start + max_len - 1

    return start + 1, end + 1  # Ajustar el índice para que empiece en 1


def analyze_palindrome_in_transmissions():
    transmission_files = ["transmission1.txt", "transmission2.txt"]
    
    for trans_file in transmission_files:
        with open(trans_file, mode='r') as file:
            trans = file.read().replace('\n', '')  # Eliminar saltos de línea

        start, end = longest_palindrome(trans)
        
        print(f"{start} {end}")

