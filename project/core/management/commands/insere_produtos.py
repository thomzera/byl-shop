from django.core.management.base import BaseCommand

from project.core.models import Categoria, Marca, Produto


class Command(BaseCommand):
    help = 'Cria dados iniciais para produtos, categorias, marcas e estoque.'

    def handle(self, *args, **kwargs):
        # Cria categorias
        categoria1 = Categoria.objects.create(nome='Roupas Masculinas')
        categoria2 = Categoria.objects.create(nome='Roupas Femininas')

        # Cria marcas
        marca1 = Marca.objects.create(nome='Marca A')
        marca2 = Marca.objects.create(nome='Marca B')

        # Cria produtos
        produto1 = Produto.objects.create(
            nome='Camiseta Masculina ADIDAS',
            descricao='Descrição da camiseta masculina',
            preco=20.00,
            genero='masculino',
            categoria=categoria1,
            tamanho='M',
            comprimento=70.0,
            largura=50.0,
            cintura=80.0,
            busto=100.0,
            cor='Azul',
            disponibilidade=True,
            colecao='Primavera 2023',
            tecido='Algodão',
            material='Material A',
            marca=marca1
        )

        produto2 = Produto.objects.create(
            nome='Vestido Feminino VERA',
            descricao='Descrição do vestido feminino',
            preco=30.00,
            genero='feminino',
            categoria=categoria2,
            tamanho='S',
            comprimento=90.0,
            largura=60.0,
            cintura=70.0,
            busto=90.0,
            cor='Vermelho',
            disponibilidade=True,
            colecao='Outono 2023',
            tecido='Seda',
            material='Material B',
            marca=marca2
        )

        # Define a quantidade em estoque
        produto1.estoque_set.create(quantidade=100)
        produto2.estoque_set.create(quantidade=50)

        self.stdout.write(self.style.SUCCESS(
            'Dados iniciais criados com sucesso.'
        ))
