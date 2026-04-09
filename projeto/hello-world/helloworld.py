print("Qual é o seu nome?")
user = input()
passed = False
while passed == False:
    if len(user) > 0:
        print(f"Hello, {user}!")
        passed = True
    else:
        print("Nome inválido, tente novamente")
        user = input()
    
if passed == True:
    print("Quantos anos você tem?")
    age = int(input())
    if age < 18:
        print("Você não está habilitado a utilizar esta parte do sistema")
    else:
        print()

#Teste
    print(f"Sua idade é: {age}")