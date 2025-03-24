
# Sistema de Arquivos - Controle de Alunos e Notas

Trabalho desenvolvido para a matéria de Sistemas Operacionais


## Funcionalidades

- Adicionar aluno
- Listar todos os alunos
- Buscar aluno por ID
- Atualizar as notas do aluno
- Excluir aluno


## Documentação

### Arquivo .tiete

Na pasta bin é gerado o arquivo database.tiete responsável por armazenar as informações do sistema.

A cada nova inicialização esse arquivo é apagado.

### Adicionar aluno

Ao adicionar um novo aluno é criado um objeto *Student* e a partir desse objeto são escritos os dados binários no arquivo .tiete.

### Listar todos os alunos

A busca basicamente itera sobre o arquivo e monta um array de *Student* que será exibida ao usuário.

### Buscar aluno por ID

Nessa busca o usuário informa o ID e durante a iteração com o arquivo .tiete é retornado o objeto que tiver esse mesmo ID.

### Atualizar as notas do aluno

Essa funcionalidade permite que novas notas sejam atribuídas a um aluno já cadastrado. Ao informar seu ID é verificado a existência do aluno, se sim é realizada a atualização do objeto em memória, após é excluido o registro do arquivo e em seguida inserido o aluno atualizado, porêm ele estará no fim do arquivo, para resolver isso é feita a reordenação do arquivo pelo ID dos alunos.

### Excluir aluno

A exclusão reescreve o arquivo sem o item que se deseja remover.


## Autores

- [@ViniciusCN9](https://github.com/ViniciusCN9)

