from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao("gui", 10)
restaurante_praca.receber_avaliacao("gui", 8)
restaurante_praca.receber_avaliacao("gui", 5)



# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')

# restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
