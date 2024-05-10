texto = input("Digite seu cdigo para Criptografar ou Decriptar ")
modo = input("Decriptar(d)? ou Criptografar(c)? ")
modo = modo.upper()
if(modo == "C"):
  chave = int(input("Chave de Rotao: "))
CARACTERES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
convertido = ""
texto = texto.upper()


if modo == "C":
  for caractere in texto:
    if caractere in CARACTERES:
      num = CARACTERES.find(caractere)
      if modo == "C":
        num = num + chave
      if num >= len(CARACTERES):
        num = num-len(CARACTERES)
      if num < 0:
        num = num+len(CARACTERES)
      convertido = convertido+CARACTERES[num]
  if modo == "C":
   print("Seu texto criptografado ",convertido)

elif modo == "D":
  for i in range(1,27):
    convertido = ""
    for caractere in texto:
        if caractere in CARACTERES:
            num = CARACTERES.find(caractere)
        if modo == "D":
            num = num - i
        if num >= len(CARACTERES):
            num = num-len(CARACTERES)
        if num < 0:
            num = num+len(CARACTERES)
        convertido = convertido+CARACTERES[num]
    if modo == "D":
        print(i,"- Seu texto decriptado ",convertido)
        
else:
    print("Opo Invlida")