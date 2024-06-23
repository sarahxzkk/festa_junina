class Aluno:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.notas = {'Elegância': [], 'Desenvoltura': [], 'Simpatia': [], 'Item Reciclável': []}
        self.jurados = []

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._notas} | {self._jurados}'

    def adicionar_nota(self, criterio, nota, jurado):
        if jurado in self.jurados:
            print(f"Jurado {jurado} já votou para {self.nome}.")
        else:
            self.notas[criterio].append(nota)
            self.jurados.append(jurado)
            print(f"Nota {nota} para {criterio} adicionada por {jurado}.")

    def calcular_media(self):
        medias = {criterio: sum(notas)/len(notas) if notas else 0 for criterio, notas in self.notas.items()}
        return medias

    def mostrar_resultado(self):
        medias = self.calcular_media()
        resultado = f'Aluno: {self.nome} ({self.categoria})\n'
        for criterio, media in medias.items():
            resultado += f'{criterio}: {media:.2f}\n'
        resultado += f'Jurados: {", ".join(self.jurados)}\n'
        print(resultado)