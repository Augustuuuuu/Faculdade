def automato_divisivel_por_3(binario: str):
    if "," in binario:
        return print("Número decimal invalido")
    estado = "q0"
    print(f"Estado {estado}: Recebida string '{binario}'")

    estado = "q1"
    numero = int(binario, 2)
    print(f"Estado {estado}: '{binario}' em binário = {numero} em decimal")

    estado = "q2"
    resto = numero % 3
    print(f"Estado {estado}: {numero} ÷ 3 → resto = {resto}")

    if resto == 0:
        estado = "q5"
        print(f"Estado {estado}: Aceita ✅ (número é divisível por 3)")

    elif resto == 1:
        estado = "q3"
        print(f"Estado {estado}: Resto = 1 (não divisível)")
        estado = "q5"
        print(f"Estado {estado}: Rejeita ❌")

    elif resto == 2:
        estado = "q4"
        print(f"Estado {estado}: Resto = 2 (não divisível)")
        estado = "q5"
        print(f"Estado {estado}: Rejeita ❌")


automato_divisivel_por_3("3,5")
print("==============")
automato_divisivel_por_3("110")
print("==============")
automato_divisivel_por_3("101")
print("==============")
automato_divisivel_por_3("0")
print("==============")
automato_divisivel_por_3("1001")
print("==============")
