# tempo em horas.

tempo = int(input("Quanto tempo durou a viagem: "));

# Distancia em km.

distancia = int(input("Quantos kms foram percorridos: "));

# velocidade em km/h.

velocidade = int(input("Qual a velociade do seu veiculo: "));

# consumo dos veiculo em l/km

consumo = int(input("Qual o consumo do seu veiculo: "));

velocidade_media = (distancia/tempo);
print("Sua velociade media na viagem foi: ", velocidade_media);

tempo_viagem = (distancia/velocidade);
print("Seu tempo de viagem foi: ", tempo_viagem);

distancia_percorrida = (velocidade*tempo);
print("Sua distancia percorrida na viagem foi: ", distancia_percorrida);

litros_usados = (distancia/consumo);
print("Seu consumo foi: ", litros_usados);