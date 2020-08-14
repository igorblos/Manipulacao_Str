from extratorArgumentosUrl import  extratorArgumentosUrl
#"https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"
url2 = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=150"
argumento = extratorArgumentosUrl(url)
argumento2 = extratorArgumentosUrl(url2)

print(argumento==argumento2)
 