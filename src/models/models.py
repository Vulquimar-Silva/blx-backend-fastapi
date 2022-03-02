from pydantic import BaseModel
from typing import Optional, List


class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    produtos: List[Produtos]
    vendas: List[Pedido]
    pedidos: List[Pedido]


class Produto(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    nome: str
    preco: float
    detalhes: str
    disponivel: bool = False


class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'
