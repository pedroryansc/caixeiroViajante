import matplotlib.pyplot as plt

# Qualidade da melhor solução

agTradicional = [115, 161, 148, 121, 133, 153, 152, 147, 113, 121]
agComIlhas = [130, 115, 146, 113, 114, 132, 133, 154, 127, 130]

intervalo = list(range(1, 11))

plt.plot(intervalo, agTradicional, label="AG Tradicional")
plt.plot(intervalo, agComIlhas, label="AG com Ilhas")

plt.title("Qualidade da melhor solução fornecida pelos AGs")
plt.xlabel("Execução do algoritmo")
plt.ylabel("Tamanho do caminho da solução")
plt.legend()

plt.show()

# Fitness da melhor solução de cada geração

agTradicional = [239, 222, 205, 222, 210, 196, 184, 202, 208, 168, 186, 180, 201, 196, 216, 189, 189, 185, 169, 170, 157, 181, 189, 189, 191, 194, 190, 182, 201, 201, 182, 176, 183, 195, 188, 176, 185, 186, 193, 200, 188, 185, 192, 169, 194, 181, 182, 169, 187, 170, 152, 180, 171, 160, 182, 179, 185, 154, 154, 186, 182, 176, 156, 171, 181, 178, 189, 179, 182, 186, 179, 175, 175, 177, 173, 169, 195, 179, 140, 140, 140, 141, 157, 141, 149, 147, 150, 143, 144, 147, 133, 133, 134, 144, 132, 134, 133, 133, 133, 133]
agComIlhas = [218, 189, 203, 231, 216, 215, 196, 213, 220, 223, 191, 191, 191, 181, 181, 190, 191, 184, 175, 177, 177, 177, 175, 180, 181, 181, 169, 169, 169, 161, 169, 163, 149, 147, 140, 151, 162, 151, 162, 164, 146, 166, 159, 164, 157, 152, 140, 140, 140, 145, 145, 139, 139, 139, 139, 126, 139, 137, 132, 140, 136, 121, 134, 129, 130, 130, 127, 127, 124, 128, 123, 123, 123, 123, 123, 120, 120, 123, 123, 120, 120, 123, 120, 120, 115, 115, 120, 120, 119, 111, 108, 108, 110, 111, 108, 120, 120, 120, 120, 120]

intervalo = list(range(1, len(agTradicional) + 1))

plt.plot(intervalo, agTradicional, label="AG Tradicional")
plt.plot(intervalo, agComIlhas, label="AG com Ilhas")

plt.title("Fitness da melhor solução de cada geração")
plt.xlabel("Geração")
plt.ylabel("Fitness da melhor solução")
plt.legend()

plt.show()

# Tempo de execução

# Quantidade de cidades

agTradicional = [0.08658981323242188, 0.4612715244293213, 1.1004109382629395, 1.9937617778778076, 3.207961320877075, 4.9255211353302, 6.584523439407349, 8.310530662536621, 10.612380504608154, 13.30942964553833, 15.929293394088745]
agComIlhas = [0.0665738582611084, 0.4970386028289795, 1.0350978374481201, 1.9063169956207275, 3.039618968963623, 4.495414972305298, 6.1945641040802, 8.18353819847107, 10.498764753341675, 12.799108982086182, 16.077522039413452]

intervalo = list(range(30, 1031, 100))

plt.plot(intervalo, agTradicional, label="AG Tradicional")
plt.plot(intervalo, agComIlhas, label="AG com Ilhas")

plt.title("Tempo de execução (Quantidade de cidades)")
plt.xlabel("Quantidade de cidades")
plt.ylabel("Tempo (s)")
plt.legend()

plt.show()

# Tamanho da população

agTradicional = [0.05752968788146973, 0.7334208488464355, 1.6507704257965088, 2.927799701690674, 4.551983833312988, 6.3883795738220215, 8.461674928665161, 10.561224460601807, 13.014965057373047, 15.437031507492065, 18.663774251937866]
agComIlhas = [0.06911802291870117, 0.5616581439971924, 1.184537649154663, 1.9479060173034668, 2.6718673706054688, 3.510331153869629, 4.511466979980469, 5.69818902015686, 7.041088819503784, 8.822092294692993, 9.890801191329956]

intervalo = list(range(30, 2031, 200))

plt.plot(intervalo, agTradicional, label="AG Tradicional")
plt.plot(intervalo, agComIlhas, label="AG com Ilhas")

plt.title("Tempo de execução (Tamanho da população)")
plt.xlabel("Quantidade de indivíduos na população")
plt.ylabel("Tempo (s)")
plt.legend()

plt.show()

# Quantidade de gerações

agTradicional = [0.06550717353820801, 0.23674583435058594, 0.45776915550231934, 0.5931313037872314, 0.7827389240264893, 0.9501230716705322, 1.133202075958252, 1.3011107444763184, 1.4910156726837158, 1.6694741249084473, 1.8540799617767334]
agComIlhas = [0.0696558952331543, 0.247025728225708, 0.44002294540405273, 0.5919492244720459, 0.7824070453643799, 0.970160722732544, 1.111811876296997, 1.3078830242156982, 1.513296365737915, 1.6806745529174805, 1.8143863677978516]

intervalo = list(range(100, 3101, 300))

plt.plot(intervalo, agTradicional, label="AG Tradicional")
plt.plot(intervalo, agComIlhas, label="AG com Ilhas")

plt.title("Tempo de execução (Quantidade de gerações)")
plt.xlabel("Quantidade de gerações")
plt.ylabel("Tempo (s)")
plt.legend()

plt.show()