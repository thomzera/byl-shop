from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=100)


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    GENERO_CHOICES = (
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('unissex', 'Unissex'),
    )

    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tamanho = models.CharField(max_length=10)
    comprimento = models.DecimalField(max_digits=5, decimal_places=2)
    largura = models.DecimalField(max_digits=5, decimal_places=2)
    cintura = models.DecimalField(max_digits=5, decimal_places=2)
    busto = models.DecimalField(max_digits=5, decimal_places=2)
    cor = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='produtos/')
    disponibilidade = models.BooleanField(default=True)
    colecao = models.CharField(max_length=50)
    tecido = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    numero_telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('processando', 'Processando'),
        ('enviado', 'Enviado'),
        ('entregue', 'Entregue'),
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    endereco_entrega = models.TextField()

    def __str__(self):
        return f'Pedido #{self.id} - {self.cliente.nome}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()


class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()


class Avaliacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    avaliacao = models.PositiveIntegerField()
    comentario = models.TextField(blank=True)


class Cupom(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)


class HistoricoCompra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)


class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Estoque de {self.produto.nome}: {self.quantidade}'
