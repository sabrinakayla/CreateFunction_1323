def Converts temperature(value, unit):
    if unit == 'C':
        return value * 9/5 + 32
    elif unit == 'F':
        return (value - 32) * 5/9

Input_value = int(input("Masukkan value : "))
Input_unit = input("Masukkan unit : ")

Konversi = Converts temperature(Input_value, Input_unit)

if Input_unit == 'C':
    print(Konversi)
else:
    print(Konversi)