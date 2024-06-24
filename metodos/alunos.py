class Aluno:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.notas = {'Elegância': [], 'Desenvoltura': [], 'Simpatia': [], 'Item Reciclável': []}
        self.jurados = []

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.notas} | {self.jurados}'
    
    def adicionar_notas(self, notas, jurado):
        if jurado in self.jurados:
            print(f'Jurado {jurado} já votou para {self.nome}.')
        else:
            for criterio, nota in notas.items():
                self.notas[criterio].append(nota)
            self.jurados.append(jurado)
            print(f'Notas {notas} adicionadas por {jurado}.')

    def calcular_media(self):
        medias = {criterio: sum(notas)/len(notas) if notas else 0 for criterio, notas in self.notas.items()}
        return medias

    def calcular_media_geral(self):
        total_notas = sum(sum(notas) for notas in self.notas.values())
        total_avaliacoes = sum(len(notas) for notas in self.notas.values())
        return total_notas / total_avaliacoes if total_avaliacoes else 0

    def mostrar_resultado(self):
        medias = self.calcular_media()
        media_geral = self.calcular_media_geral()
        resultado = f'Aluno: {self.nome} ({self.categoria})\n'
        for criterio, media in medias.items():
            resultado += f'{criterio}: {media:.2f}\n'
        resultado += f'Média Geral: {media_geral:.2f}\n'
        resultado += f'Jurados: {', '.join(self.jurados)}\n'
        print(resultado)