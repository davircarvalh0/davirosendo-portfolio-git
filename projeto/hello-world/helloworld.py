usuario = input()
passed = False
while passed == False:
    if len(usuario) > 0:
        print(f"Hello, {usuario}!")
        passed = True
    else:
        print("Nome inválido, tente novamente")
        usuario = input()