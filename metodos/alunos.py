class Aluno:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.notas_por_jurado = {}
        self.jurados = []

    def adicionar_notas(self, notas, jurado):
        if jurado in self.jurados:
            print(f"Jurado {jurado} já votou para {self.nome}.")
        else:
            self.notas_por_jurado[jurado] = notas
            self.jurados.append(jurado)
            print(f"Notas {notas} adicionadas por {jurado}.")

    def calcular_media_geral(self):
        total_notas = 0
        total_avaliacoes = 0
        for notas in self.notas_por_jurado.values():
            total_notas += sum(notas.values())
            total_avaliacoes += len(notas)
        return total_notas / total_avaliacoes if total_avaliacoes else 0

    def __str__(self):
        resultado = f'Aluno: {self.nome} ({self.categoria})\n'
        for jurado, notas in self.notas_por_jurado.items():
            notas_str = ', '.join([f'{criterio}: {nota:.2f}' for criterio, nota in notas.items()])
            resultado += f'Notas de {jurado}: {notas_str}\n'
        media_geral = self.calcular_media_geral()
        resultado += f'Média Geral: {media_geral:.2f}\n'
        return resultado