texto = input("Digite seu código para Criptografar ou Decriptar ")
modo = input("Encriptar(e)? ou Decriptar(d)? ")
modo = modo.upper()
if(modo == "E"):
  chave = int(input("Chave de Rotação: "))
CARACTERES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
convertido = ""
texto = texto.upper()


if modo == "E":
  for caractere in texto:
    if caractere in CARACTERES:
      num = CARACTERES.find(caractere)
      num = num + chave
      if num >= len(CARACTERES):
        num = num-len(CARACTERES)
      if num < 0:
        num = num+len(CARACTERES)
      convertido = convertido+CARACTERES[num]
  print("Seu texto encriptado: ",convertido)

elif modo == "D":
  for i in range(1,27):
    convertido = ""
    for caractere in texto:
        if caractere in CARACTERES:
            num = CARACTERES.find(caractere)
            num = num - i
        if num >= len(CARACTERES):
            num = num-len(CARACTERES)
        if num < 0:
            num = num+len(CARACTERES)
        convertido = convertido+CARACTERES[num]
    print(i,"- Seu texto decriptado: ",convertido)
        
else:
    print("E ou D e tu coloca outro coisa é?")
