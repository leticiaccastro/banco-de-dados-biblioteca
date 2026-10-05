from app.database import engine, SessionLocal, Base
from app import models


# ==========================================
# CRIAÇÃO DAS TABELAS
# ==========================================

Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")


# ==========================================
# INSERÇÃO DOS DADOS
# ==========================================

db = SessionLocal()


try:

    # ======================================
    # 1º - GÊNEROS
    # ======================================

    generos = [
        models.Genero(nome="Ficção"),
        models.Genero(nome="Romance"),
        models.Genero(nome="Fantasia"),
        models.Genero(nome="Mistério")
    ]

    db.add_all(generos)
    db.commit()

    print("Gêneros inseridos com sucesso!")


    # ======================================
    # 2º - AUTORES
    # ======================================

    autores = [
        models.Autor(
            nome="Machado de Assis",
            nacionalidade="Brasileira"
        ),
        models.Autor(
            nome="J. K. Rowling",
            nacionalidade="Britânica"
        ),
        models.Autor(
            nome="George Orwell",
            nacionalidade="Britânica"
        ),
        models.Autor(
            nome="Clarice Lispector",
            nacionalidade="Brasileira"
        )
    ]

    db.add_all(autores)
    db.commit()

    print("Autores inseridos com sucesso!")


    # ======================================
    # 3º - LIVROS
    # ======================================

    livros = [
        models.Livro(
            titulo="Dom Casmurro",
            ano_publicacao=1899,
            disponivel=True,
            genero_id=2,
            autor_id=1
        ),

        models.Livro(
            titulo="Harry Potter e a Pedra Filosofal",
            ano_publicacao=1997,
            disponivel=True,
            genero_id=3,
            autor_id=2
        ),

        models.Livro(
            titulo="1984",
            ano_publicacao=1949,
            disponivel=True,
            genero_id=1,
            autor_id=3
        ),

        models.Livro(
            titulo="A Hora da Estrela",
            ano_publicacao=1977,
            disponivel=True,
            genero_id=2,
            autor_id=4
        ),

        models.Livro(
            titulo="Harry Potter e a Câmara Secreta",
            ano_publicacao=1998,
            disponivel=False,
            genero_id=3,
            autor_id=2
        ),

        models.Livro(
            titulo="Memórias Póstumas de Brás Cubas",
            ano_publicacao=1881,
            disponivel=True,
            genero_id=1,
            autor_id=1
        )
    ]

    db.add_all(livros)
    db.commit()

    print("Livros inseridos com sucesso!")


except Exception as erro:

    db.rollback()

    print("Erro ao inserir os dados:")
    print(erro)


finally:

    db.close()

    print("Conexão com o banco encerrada.")