# převodnik římských čísel na arabská čísla

roman_numbers = ("I", "V", "X", "L", "C", "D", "M")
arabic_numbers = (1, 5, 10, 50, 100, 500, 1000)

first_number = second_number = 0
final_transfer = 0

roman_string = str(input("Zadej římské číslo: ")).upper()

for letter in roman_string:
    first_number = second_number
    second_number = arabic_numbers[roman_numbers.index(letter)]

    if (0 < first_number) and (first_number < second_number):
        final_transfer += first_number * (-1)
    else:
        final_transfer += first_number

final_transfer += second_number
print("Arabské číslo je : {0}".format(final_transfer))