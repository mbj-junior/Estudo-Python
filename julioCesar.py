import requests as req
import json as js
import hashlib
abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

res = req.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=83cd066d68ae03c1f444d534991cd61d43729a39')
mensagem = res.json()
print(mensagem)
numero_casas = mensagem['numero_casas']
frase_cripto = mensagem['cifrado']
print(frase_cripto)
for i in range(len(frase_cripto)):
     if frase_cripto[i] == " ":
         print(" ", end="")
     if frase_cripto[i] == ".":
         print(".", end="")
     for j in range(len(abc)):
         if frase_cripto[i] == abc[j]:
             new_index = j-numero_casas
             if new_index < len(abc):
                 print(abc[new_index], end="")
res.close()