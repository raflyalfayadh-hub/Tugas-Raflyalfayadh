for i in range(1, 101):
    # Cek jika kelipatan keduanya (3 dan 5)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Cek jika kelipatan 3
    elif i % 3 == 0:
        print("Fizz")
    # Cek jika kelipatan 5
    elif i % 5 == 0:
        print("Buzz")
    # Jika bukan kelipatan ketiganya, tampilkan angka
    else:
        print(i)
