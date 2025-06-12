def login(Tentativa):
    def inserir_usuario():
       return input("Digite o Usuário: ")
        
    
    def inserir_senha():
        return input("Digite a senha: ")
        

    # agora sim: pega os retornos das funções
    usuario = inserir_usuario()
    senha = inserir_senha()
    

    if usuario == "Admin" and senha == "1234":
        print("Login bem sucedido")
        return True, Tentativa
    else:
        Tentativa -= int(1)
        print("Usuario ou senha incorreta")
        print("Tentativas Restantes: ", Tentativa)
        return False, Tentativa
    
Tentativa = int(3)        

while Tentativa > 0:
   sucesso, Tentativa = login(Tentativa)
   if sucesso:
       break
   else:
       print("Acesso Bloqueado.")
    
    

