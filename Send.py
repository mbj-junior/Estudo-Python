import requests as req

file = {'answer': open('C:\\Users\\StrixJr\\Desktop\\00 - Desafio - JulioCesar\\answer.json','rb')}
print (file)

try:
    answer = req.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=83cd066d68ae03c1f444d534991cd61d43729a39',files=file)
    print(answer.status_code)

except ValueError:
    print(ValueError)