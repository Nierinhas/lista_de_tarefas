Lista de Tarefas (Python)

Projeto de terminal desenvolvido em Python para gerenciamento simples de tarefas.

Permite cadastrar tarefas, alterar status (pendente/concluída), remover itens, filtrar por status e ordenar por prioridade.

Funcionalidades

Adicionar tarefa com:

descrição

prioridade (baixa, media, alta)

status (pendente ou concluida)

Listar todas as tarefas

Marcar tarefa como concluída ou pendente

Remover tarefa pelo número

Mostrar apenas pendentes ou apenas concluídas

Ordenar tarefas por prioridade (maior ou menor)

Estrutura de dados utilizada

Cada tarefa é armazenada como um dicionário:

{
  "descricao": "estudar python",
  "prioridade": "alta",
  "status": "[ ]"
}


As tarefas são mantidas em uma lista chamada tarefas.

Conceitos praticados

Listas e dicionários

Funções

while + menu interativo

Validação de entradas

enumerate para exibir índice amigável ao usuário

Manipulação de strings (lower, strip)

Ordenação com sort + key=lambda

Como executar

Ter Python instalado

Executar no terminal:

python nome_do_arquivo.py

Próximas melhorias (opcional)

Persistência em arquivo (JSON)

Edição de tarefa (alterar descrição/prioridade)

Busca por palavra na descrição
