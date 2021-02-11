# převodnik římských čísel na arabská čísla

roman_numbers = ("I", "V", "X", "L", "C", "D", "M")
arabic_numbers = (1, 5, 10, 50, 100, 500, 1000)

roman_string = str(input("Zadej římské číslo: ")).upper()

firstNumber = secondNumber = 0
finalTransfer = 0

for letter in roman_string:
    print(letter)
    transferIndex = roman_numbers.index(letter)
    firstNumber = secondNumber
    secondNumber = arabic_numbers[transferIndex]

    if (0 < firstNumber) and (firstNumber < secondNumber):
        finalTransfer += firstNumber * (-1)
    else:
        finalTransfer += firstNumber

finalTransfer += secondNumber
print("Arabské číslo je : {0}".format(finalTransfer))