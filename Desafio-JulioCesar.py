import requests as req
import json
import hashlib

token = 'afbb7e8316a0cf5adb316cfbc46bfab18bdda08f'

#recebe json via http e salva em disco
response = req.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=afbb7e8316a0cf5adb316cfbc46bfab18bdda08f')
msg = response.json()
with open('C:\\Users\\User_Techplus\\Desktop\\answer.json', 'w') as f:
     json.dump(msg, f)
response.close()

#abre json, decriptografa mensagem e salva json novamente
with open('C:\\Users\\User_Techplus\\Desktop\\answer.json', 'r') as f:
     msg = json.load(f)
cifrado = msg['cifrado']
try:
     n_casas = int(msg['numero_casas'])
except:
     print('Numero de casas invalido.')

lista = []
for i in range(len(cifrado)):
     if ord(cifrado[i]) >= ord('A') and  ord(cifrado[i]) <= ord('Z'):
          v = ord(cifrado[i]) - n_casas + 32
          if(v < ord('a')):
               v = v+26
          lista.append(chr(v))
     
     elif ord(cifrado[i]) >= ord('a') and  ord(cifrado[i]) <= ord('z'):
          v = ord(cifrado[i]) - n_casas 
          if(v < ord('a')):
               v = v+26
          lista.append(chr(v))
     else:
          lista.append(cifrado[i])

msg['decifrado'] = ''.join(lista)
with open('C:\\Users\\User_Techplus\\Desktop\\teste.json', 'w') as f:
     json.dump(msg, f)

#abre json e envia via metodo post
file = {'answer': open('C:\\Users\\User_Techplus\\Desktop\\answer.json','rb')}
print (file)
try:
    resp = req.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token='+token, files=file)
    print(resp.status_code)

except ValueError:
    print(ValueError)


