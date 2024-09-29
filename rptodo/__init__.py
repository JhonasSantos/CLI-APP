__app_name__ = "Lista Atividades"
__version__ = "0.1.0"

(
    SUCESSO,
    DIR_ERRO,
    ARQ_ERRO,
    DB_READ_ERRO,
    DB_WRITE_ERRO,
    JSON_ERRO,
    ID_ERRO,
) = range(7)

ERROS = {
    SUCESSO: "Operação concluída com sucesso.",
    DIR_ERRO: "Diretório informado não existe.",
    ARQ_ERRO: "Arquivo inexistente.",
    DB_READ_ERRO: "Falha ao ler dados do arquivo.",
    DB_WRITE_ERRO: "Falha ao escrever dados no arquivo.",
    JSON_ERRO: "Falha ao gerar arquivo JSON.",
    ID_ERRO: "ID informado não existe.",
}
