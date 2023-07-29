# This script will help explaining how debuggers are used in vs code

def general_fibbonacci_sequence(sequence):
    i = sequence[0]
    return_sequence = [sequence[0]]
    for j in range(2, len(sequence)):
        i = sequence[j] + i
        return_sequence.append(i)
    return return_sequence

def main():
    sequence = [1, 2, 3, 5, 7, 9, 10]
    general_sequence = general_fibbonacci_sequence(sequence)
    print(general_sequence)
    return None

if __name__ == "__main__":
    main()