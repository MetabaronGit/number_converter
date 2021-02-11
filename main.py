# převodnik římských čísel na arabská čísla
romanNumbers = ("I", "V", "X", "L", "C", "D", "M")
arabicNumbers = (1, 5, 10, 50, 100, 500, 1000)


romanString = str(input("Zadej římské číslo: ")).upper()

firstNumber = secondNumber = 0
finalTransfer = 0
# cyklus A = 0 - len(romanString)-1
transferIndex = romanNumbers.index(romanString[A])
firstNumber = secondNumber
secondNumber = arabicNumbers[transferIndex]
if 0 < firstNumber < secondNumber:
    finalTransfer += firstNumber * (-1)
else:
    finalTransfer += firstNumber

print("Arabské číslo je : {0}".format(finalTransfer))