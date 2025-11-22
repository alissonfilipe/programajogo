# engine/batalha.py

def batalha(p1, p2):
    """
    Batalha simplificada 1v1:
    - Quem tem maior agilidade começa.
    - Turnos alternados, usando Pokemon.atacar().
    - Imprime eventos e retorna o vencedor (objeto Pokemon).
    """
    print(f"\n=== BATALHA INICIADA: {p1.nome} VS {p2.nome} ===\n")

    # decide quem começa pela agilidade (se empate, pelo que tem maior velocidade)
    if p1.agilidade != p2.agilidade:
        atacante, defensor = (p1, p2) if p1.agilidade > p2.agilidade else (p2, p1)
    else:
        atacante, defensor = (p1, p2) if p1.velocidade >= p2.velocidade else (p2, p1)

    turno = 1
    while p1.esta_vivo() and p2.esta_vivo():
        print(f"-- Turno {turno}: {atacante.nome} ataca --")
        dano = atacante.atacar(defensor)
        print(f"{atacante.nome} causou {dano} de dano em {defensor.nome}.")
        print(f"{defensor.nome}: {max(defensor.hp,0)} / {defensor.hp_max} HP\n")

        if not defensor.esta_vivo():
            print(f"🏆 {atacante.nome} venceu a batalha!\n")
            return atacante

        # troca atacantes
        atacante, defensor = defensor, atacante
        turno += 1

    # fallback (não deve chegar aqui)
    vencedor = p1 if p1.esta_vivo() else p2
    return vencedor
