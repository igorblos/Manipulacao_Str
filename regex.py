import re
email1 = "Meu numero é 434233434 testetetete 4449-3330 testetestetetsts 44559"
padrao = "[0-9]{4,5}[-]*[0-9]{4}"

retorno = re.findall(padrao,email1)
print(retorno)


padrao = "[a]{1,20}[ ] [0-9]{3}"
frase1 = "podemos marcar de sair sabado 23h"
frase2 = "acho que quinta 21h é a melhor hora para a gente ir lá"
frase3 = "“terca 19h é um bom momento para sairmos"
retorno = re.findall(padrao,frase3)
print(retorno)