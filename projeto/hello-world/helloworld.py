print("Qual é o seu nome?")
usuario = input()
passed = False
while passed == False:
    if len(usuario) > 0:
        print(f"Hello, {usuario}!")
        passed = True
    else:
        print("Nome inválido, tente novamente")
        usuario = input()
    
if passed == True:
    print("Quantos anos você tem?")
    idade = int(input())
    if idade < 18:
        print("Você não está habilitado a utilizar esta parte do sistema")
    else:
        print()