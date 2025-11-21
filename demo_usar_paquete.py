from mini_proyecto import sumar, duplicar_lista, mostrar, verificar, generar_numero


def demo():
    mostrar(f"5 + 7 = {sumar(5, 7)}")
    mostrar(f"Lista duplicada: {duplicar_lista([4, 5])}")

    # Demo no interactiva del juego
    secreto_ejemplo = 3
    intento = 3
    mostrar(f"Verificar ejemplo: secreto={secreto_ejemplo}, intento={intento} -> {verificar(secreto_ejemplo, intento)}")


if __name__ == "__main__":
    demo()
