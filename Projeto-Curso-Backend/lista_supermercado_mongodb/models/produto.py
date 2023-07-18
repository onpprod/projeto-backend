"""Modelos usados para a criação das tabelas no banco de dados"""

# Bibliotecas
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from typing import Optional

try:
    from models.PyObjectId import PyObjectId

except:
    from lista_supermercado_mongodb.models.PyObjectId import PyObjectId

class ProdutoModel(BaseModel):
    item: str
    descricao: str
    quantidade: int
    preco: Optional[float]
    tipo: str
       
    def as_dict(self):
        if self.tipo == "comida" or self.tipo == "bebida":  # Verifica se o tipo é válido
            print(self.tipo)
            return {
                "item": self.item,
                "descricao": self.descricao,
                "quantidade": self.quantidade,
                "preco": self.preco,
                "tipo": self.tipo
            }
        else:
            message = {"message": "O Tipo de produto não é válido!"}
            # Retorne ou faça algo com a mensagem de erro

class ProdutoUpdateModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    item: str = Field(..., title="Nome do item", max_length=50)
    descricao: str = Field(..., title="Descricao do item", max_length=800)
    quantidade: int = Field(..., title="Quantidade de itens")
    preco: float = Field(None, title="Preco unitário do item")
    tipo: str = Field(...,tittle="Tipo do item")

    def as_dict(self):
        return {"id": self.id,
                "item": self.item,
                "descricao": self.descricao,
                "quantidade": self.quantidade,
                "preco": self.preco,
                "tipo":self.tipo}

def ResponseModel(message, code):
    return JSONResponse(
        status_code = code,
        content = message,
    )