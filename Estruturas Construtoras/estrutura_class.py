#ESTRUTURA PARA CRIAR UMA CLASSE
class Aluno:
    def __init__(self, nome : str, media : float) -> None:
        '''
        nome : str() -> Propriedade nome do objeto a ser instanciado
        media : float() -> Propriedade nota do objeto a ser instanciado

        retorna -> None
        '''
        self.nome = nome
        self.media = media

    def verifica_media(self) -> None:
        '''
        Método que realiza uma ação condicionando ao valor da propriedade média do objeto instanciado
        '''
        if self.media >= 6:
            print(f'{self.nome} foi APROVADO')
        else:
            print(f'{self.nome} foi REPROVADO')
