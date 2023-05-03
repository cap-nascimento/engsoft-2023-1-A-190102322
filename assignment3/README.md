### ChamadaPy
#### REQUISITOS 
##### Funcionais:

Interação:

1. O aluno poderá marcar a presença apenas com o *full_name* da imagem gerada pelo sistema (A API da NASA Mars será utilizada). O *full_name* será disponibilizado pelo administrador;
1. A busca pela imagem aleatória é exclusividade do administrador;
    - A imagem e o *full_name* poderão ser atualizados a qualquer momento pelo administrador do sistema;
1. O administrador poderá exportar uma listagem dos alunos presentes. A listagem deverá conter também a data em que será exportada;
    - O administrador deverá definir os horários e a data em que deseja verificar a presença dos alunos;

Cadastro de dados:

1. O usuário administrador deverá cadastrar a lista de alunos;
1. O administrador poderá remover alunos que trancaram ou retiraram a disciplina;
1. Nenhum aluno poderá cadastrar dados.

Login:

1. O login de aluno será feito com o número de matrícula cadastrado pelo adminstrador;
1. O login de administrador será feito com o CPF do administrador;

##### Não funcionais:

1. A matrícula deverá estar no formato ‘00/0000000’;
1. O CPF deverá estar no formato ‘000.000.000-00’;
1. Uma classe ‘User’ deverá ser implementada;
    - A classe possuirá um atributo ‘ROLE’, que dirá se o usuário é ‘USER’ ou ‘ADMIN’;
1. Uma classe ‘Attendance’ deverá ser implementada;
    - A classe possuirá um atributo do tipo timestamp correspondente à marcação de presença de um usuário;
    - O registro de uma marcação de presença deverá conter um campo createdAt;
    - A classe está diretamente associada à classe ‘USER’;
1. Testes unitários deverão ser implementados;
1. A página de login do usuário comum deverá ser acessada pela rota ‘/’;
    - Em caso de erro, uma mensagem deverá ser mostrada;
1. A página de login do administrador deverá ser acessada pela rota ‘/admin’;
1. O Token deverá ter 8 caracteres, entre alfanuméricos e símbolos especiais;
1. O formulário de envio do Token deve alertar ao usuário nos seguintes cenários:
    - *full_name* incorreto;
1. O formulário de carregamento da planilha deverá alertar o usuário nos seguintes cenários:
    - Erro no upload da planilha;
    - Erro na formatação da planilha;
1. A lista gerada na aba seção de listagem deve ser baixada em formato .PDF.

##### [Link](https://www.figma.com/proto/CF5wbHkFCRVcfInC9Xk2lN/chamadapy?node-id=1-2&scaling=scale-down&page-id=0%3A1&starting-point-node-id=1%3A2&show-proto-sidebar=1) para protótipo no FIGMA.
