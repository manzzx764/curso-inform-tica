"""Trilha ampliada da NEXA Academia Digital: conteúdo educacional gratuito."""

RAW_LESSONS = [
(8, "Montagem de computadores: compatibilidade e segurança", "Hardware", "75 min", "Aprenda a planejar uma montagem, verificar compatibilidade e trabalhar com segurança contra danos físicos e eletrostáticos.", [
("Planejamento", "Antes de comprar peças, liste o uso pretendido, orçamento, dimensões do gabinete e possibilidade de upgrades. Confira as especificações nos manuais dos fabricantes; nomes parecidos não garantem compatibilidade."),
("Placa-mãe e processador", "O soquete precisa ser compatível com a CPU, mas chipset, versão da BIOS e lista de processadores suportados também importam. O formato da placa-mãe deve caber no gabinete."),
("Memória e armazenamento", "Confira geração DDR, capacidade máxima, quantidade de slots e configurações recomendadas. SSD SATA e NVMe usam interfaces diferentes; um M.2 físico não garante suporte a todos os protocolos."),
("Energia e segurança", "Calcule o consumo aproximado, escolha fonte de qualidade com conectores adequados e nunca abra a fonte. Desligue da tomada antes de montar, evite carpetes e manuseie placas pelas bordas."),
], ["Monte uma tabela com CPU, placa-mãe, RAM, GPU, SSD, gabinete e fonte para um PC de estudo.", "Consulte o manual da placa-mãe e identifique soquete, memória suportada e conectores de armazenamento.", "Crie uma checklist de segurança antes de instalar qualquer componente."], [
("Qual informação não pode ser ignorada ao escolher uma CPU?", ["A cor do gabinete", "Soquete, chipset e suporte de BIOS", "A marca do monitor", "O tamanho do mouse"], 1, "A compatibilidade depende do soquete e do suporte específico da placa-mãe/BIOS."),
("O que fazer antes de instalar uma placa?", ["Deixar o PC ligado", "Desligar e desconectar a alimentação", "Abrir a fonte", "Tocar nos contatos dourados"], 1, "Desconectar a alimentação e reduzir risco eletrostático são medidas básicas de segurança."),
("Um conector M.2 garante que qualquer SSD funcione?", ["Sim, todos são iguais", "Não; é preciso conferir protocolo e suporte", "Só se o gabinete for grande", "Somente em notebooks"], 1, "M.2 descreve formato; SATA e NVMe são interfaces/protocolos diferentes."),
]),
(9, "BIOS/UEFI, POST e inicialização", "Hardware", "60 min", "Entenda o que acontece entre apertar o botão de ligar e chegar à área de trabalho.", [
("POST", "Ao ligar, o firmware realiza verificações iniciais e inicializa componentes. Beeps, LEDs de diagnóstico e códigos variam conforme a placa e ajudam a localizar falhas."),
("BIOS e UEFI", "UEFI é o firmware moderno que inicializa hardware e entrega o controle ao carregador do sistema. As configurações podem incluir ordem de boot, virtualização, Secure Boot e perfis de memória."),
("Partições e modo de boot", "Instalações modernas costumam usar UEFI com disco GPT. Sistemas antigos podem usar BIOS legado e MBR. Alterar o modo sem entender a instalação pode impedir o Windows de iniciar."),
("Atualização responsável", "Atualize firmware apenas quando houver motivo claro, usando arquivo e procedimento oficiais. Uma interrupção durante a gravação pode inutilizar a placa; siga o manual e não desligue o equipamento."),
], ["Entre no firmware apenas para observar as telas e anote o modelo da placa-mãe.", "Identifique no manual como consultar LEDs ou códigos de diagnóstico.", "Explique a diferença entre firmware, carregador de inicialização e sistema operacional."], [
("Qual é a função do POST?", ["Editar vídeos", "Verificar e inicializar componentes no início", "Substituir o sistema operacional", "Limpar arquivos temporários"], 1, "O POST faz verificações iniciais de hardware durante a partida."),
("O que pode acontecer ao trocar aleatoriamente o modo UEFI/Legacy?", ["Aumentar a RAM", "O sistema instalado pode deixar de iniciar", "Melhorar sempre o FPS", "Mudar o tamanho do monitor"], 1, "O modo de boot deve corresponder ao modo e à estrutura usados na instalação."),
("Qual é a melhor prática para atualizar firmware?", ["Usar qualquer arquivo encontrado", "Seguir instruções oficiais e garantir alimentação estável", "Interromper no meio", "Atualizar sem necessidade e sem ler o manual"], 1, "Firmware deve ser atualizado com cuidado, fonte oficial e procedimento correto."),
]),
(10, "Armazenamento, partições e backup", "Sistemas", "70 min", "Compare HDD, SSD SATA e NVMe e aprenda a organizar volumes e cópias de segurança.", [
("HDD e SSD", "HDD usa discos mecânicos e costuma oferecer boa capacidade por preço; SSD não tem partes móveis e tende a ter menor latência. A diferença real depende do modelo e da carga de trabalho."),
("SATA e NVMe", "SATA é uma interface comum em HDDs e SSDs. NVMe usa PCIe e pode oferecer maior desempenho em tarefas paralelas; para uso cotidiano, latência, capacidade e qualidade também contam."),
("Partições e sistemas de arquivos", "Particionar divide logicamente o armazenamento. NTFS é comum no Windows; exFAT facilita troca entre sistemas; FAT32 tem limitações, incluindo tamanho máximo de arquivo individual de 4 GiB menos um byte."),
("Backup 3-2-1", "Uma estratégia conhecida mantém três cópias dos dados, em dois tipos de mídia, com uma cópia fora do local principal. Sincronização não substitui backup se exclusões e corrupção também forem sincronizadas."),
], ["Compare espaço usado e livre no Explorador de Arquivos.", "Desenhe um plano de backup para documentos, fotos e projetos de programação.", "Pesquise o sistema de arquivos de um pendrive sem formatá-lo."], [
("Qual é uma limitação conhecida do FAT32?", ["Não suporta pastas", "Não aceita arquivos individuais de 4 GiB ou maiores", "Só funciona em SSD", "Exige internet"], 1, "O limite de tamanho de arquivo do FAT32 é inferior a 4 GiB."),
("Sincronização em nuvem é sempre um backup completo?", ["Sim", "Não; exclusões e alterações podem sincronizar também", "Só em computadores novos", "Somente com FAT32"], 1, "Um backup deve permitir recuperar versões ou cópias independentes."),
("Qual estratégia ajuda a reduzir risco de perda?", ["Uma única cópia", "3-2-1, com cópia fora do local principal", "Guardar tudo na Área de Trabalho", "Desativar histórico"], 1, "A estratégia 3-2-1 diversifica cópias e reduz pontos únicos de falha."),
]),
(11, "Windows: usuários, permissões e ferramentas administrativas", "Windows", "80 min", "Use ferramentas integradas para administrar contas, processos, serviços e registros com prudência.", [
("Contas e privilégios", "Contas padrão reduzem o impacto de ações acidentais. Use elevação administrativa somente para tarefas que realmente precisam dela e mantenha senhas individuais."),
("Gerenciador de Tarefas", "Permite observar processos, consumo de CPU, memória, disco, rede e inicialização. Um processo com uso alto deve ser investigado pelo nome, contexto e comportamento antes de encerrá-lo."),
("Serviços e inicialização", "Serviços oferecem funções de sistema e aplicativos. Desativar serviços desconhecidos pode quebrar recursos ou segurança; documente alterações e prefira configurações recomendadas pelo fornecedor."),
("Visualizador de Eventos", "Os registros ajudam a correlacionar erros com horários e mudanças. Um evento isolado não prova a causa; observe fonte, ID, frequência e contexto."),
], ["Abra o Gerenciador de Tarefas e registre quais recursos são exibidos.", "Encontre o Visualizador de Eventos e localize um registro informativo sem alterar configurações.", "Crie um procedimento para investigar um aplicativo que inicia junto com o Windows."], [
("Qual conta é mais indicada para uso cotidiano?", ["Administrador para tudo", "Conta padrão, elevando apenas quando necessário", "Uma conta compartilhada", "Conta sem senha"], 1, "O menor privilégio reduz o impacto de erros e comprometimentos."),
("Uso alto de CPU por si só prova que há vírus?", ["Sim", "Não; é preciso investigar processo e contexto", "Sim, se o PC for antigo", "Só se houver internet"], 1, "Uso alto pode ser legítimo, como renderização, atualização ou jogo."),
("Para que serve o Visualizador de Eventos?", ["Aumentar a memória", "Consultar registros e correlacionar falhas", "Substituir o antivírus", "Formatar automaticamente"], 1, "Logs fornecem evidências, mas precisam ser interpretados no contexto."),
]),
(12, "Linux para iniciantes: terminal, arquivos e permissões", "Linux", "90 min", "Aprenda os conceitos essenciais para navegar no terminal e compreender permissões sem executar comandos cegamente.", [
("Distribuições", "Linux é o núcleo; uma distribuição combina kernel, ferramentas, gerenciador de pacotes e aplicações. Ubuntu, Debian, Fedora e outras diferem em ciclo de atualização e ferramentas."),
("Estrutura de diretórios", " /home guarda diretórios de usuários em muitas distribuições; /etc contém configurações; /var guarda dados variáveis; /tmp é usado para arquivos temporários. A estrutura exata depende do sistema."),
("Comandos básicos", "pwd mostra o diretório atual; ls lista arquivos; cd navega; mkdir cria diretórios; cp copia; mv move/renomeia; cat exibe texto. Leia a ajuda antes de usar opções destrutivas."),
("Permissões", "Permissões tradicionais separam leitura, escrita e execução para proprietário, grupo e outros. sudo executa comandos com privilégios elevados; nunca copie comandos privilegiados sem compreender o efeito."),
], ["Em um ambiente Linux ou máquina virtual, use pwd, ls e mkdir em uma pasta de teste.", "Crie um arquivo de texto e copie-o com outro nome.", "Explique por escrito o que muda entre executar um comando comum e usar sudo."], [
("Qual comando mostra o diretório atual?", ["pwd", "mkdir", "sudo", "clearcache"], 0, "pwd imprime o caminho do diretório de trabalho atual."),
("O que o sudo permite em configurações comuns?", ["Executar tarefas com privilégios elevados", "Aumentar fisicamente o disco", "Traduzir todos os arquivos", "Desligar a internet permanentemente"], 0, "sudo pode executar comandos com permissões elevadas; use com cuidado."),
("Antes de usar rm em arquivos reais, é prudente:", ["Ignorar o caminho", "Conferir o alvo e testar em pasta descartável", "Adicionar sudo sempre", "Apagar a pasta raiz"], 1, "Comandos de remoção podem ser irreversíveis; confirme o caminho e o alvo."),
]),
(13, "Redes avançadas: DHCP, NAT, portas e Wi-Fi", "Redes", "95 min", "Amplie o diagnóstico de redes domésticas e compreenda como dispositivos recebem configuração e se comunicam.", [
("DHCP", "DHCP distribui configurações como endereço IP, máscara, gateway e DNS por concessões temporárias. Conflitos e falhas de concessão podem causar conectividade intermitente."),
("NAT e endereços privados", "Roteadores domésticos geralmente traduzem vários endereços privados para um endereço público. NAT não é sinônimo de firewall e não substitui regras de segurança."),
("Portas e protocolos", "TCP oferece fluxo confiável com conexão; UDP envia datagramas sem a mesma garantia de entrega. Portas identificam serviços em um dispositivo, como aplicações web, mas não são aplicações em si."),
("Wi-Fi e interferência", "Banda de 2,4 GHz tende a alcançar mais longe e sofrer mais interferência; 5 GHz costuma oferecer mais capacidade em distâncias menores. Obstáculos, canal, largura de banda e capacidade do roteador influenciam o resultado."),
], ["Execute ipconfig e identifique gateway e endereço IPv4.", "Desenhe o caminho entre notebook, roteador e um site.", "Compare velocidade perto do roteador e em outro cômodo, mantendo o mesmo dispositivo e servidor de teste."], [
("Qual serviço costuma distribuir IP automaticamente?", ["DHCP", "HTML", "GPU", "SMTP apenas"], 0, "DHCP distribui parâmetros de configuração de rede aos clientes."),
("NAT substitui todas as funções de um firewall?", ["Sim", "Não", "Só no Wi-Fi 5 GHz", "Somente no Linux"], 1, "NAT e filtragem de tráfego têm funções diferentes."),
("Por que o Wi-Fi pode ficar lento longe do roteador?", ["Distância, obstáculos e interferência", "A tela é pequena", "O teclado está sem fio", "O arquivo é PDF"], 0, "Sinal, interferência, congestionamento e capacidades dos dispositivos influenciam a rede."),
]),
(14, "HTML semântico e estrutura de páginas", "Desenvolvimento web", "90 min", "Construa documentos HTML organizados, acessíveis e compreensíveis por navegadores e tecnologias assistivas.", [
("Estrutura do documento", "Um HTML bem formado declara doctype, idioma, charset, viewport, título e corpo. Elementos devem ser aninhados corretamente e usados de acordo com seu significado."),
("Semântica", "header, nav, main, section, article e footer descrevem regiões da página. Títulos seguem hierarquia lógica; botões representam ações e links representam navegação."),
("Formulários", "Cada campo deve ter rótulo associado. Use tipos adequados, atributos required quando pertinentes e mensagens de erro claras. Validação no navegador melhora a experiência, mas o servidor também precisa validar."),
("Acessibilidade", "Texto alternativo descreve imagens informativas; imagens decorativas podem ter alt vazio. Contraste, foco visível, navegação por teclado e nomes acessíveis tornam a página mais utilizável."),
], ["Crie uma página com header, nav, main, duas sections e footer.", "Faça um formulário de contato com rótulos e tipos de entrada apropriados.", "Navegue pela página apenas com Tab e Enter e corrija elementos sem foco visível."], [
("Qual elemento representa o conteúdo principal da página?", ["main", "footer", "meta", "br"], 0, "main identifica a região principal do documento."),
("O que um link deve representar normalmente?", ["Uma ação destrutiva sem aviso", "Navegação para um destino", "Um campo de senha", "Um título visual"], 1, "Links navegam; botões executam ações."),
("Validação de formulário deve ocorrer:", ["Somente no navegador", "No navegador para UX e no servidor para segurança", "Nunca", "Apenas por cor"], 1, "O servidor não pode confiar apenas na validação feita pelo cliente."),
]),
(15, "CSS responsivo, layout e design system", "Desenvolvimento web", "100 min", "Aprenda a organizar estilos, adaptar telas e manter consistência visual em interfaces reais.", [
("Cascata e especificidade", "A cascata considera origem, importância, especificidade e ordem. Evite cadeias longas de seletores e uso indiscriminado de !important, pois tornam mudanças difíceis."),
("Flexbox e Grid", "Flexbox é útil para alinhar itens em uma dimensão; Grid organiza linhas e colunas. Escolha conforme a estrutura, e use gap para espaçamento consistente."),
("Responsividade", "Layouts responsivos usam unidades flexíveis, limites de largura e media queries. Teste em telas estreitas, zoom aumentado e orientação diferente, não apenas na resolução do computador."),
("Tokens visuais", "Variáveis CSS para cores, espaçamento, bordas e tipografia ajudam a manter consistência. Estados de foco, hover, erro e desabilitado precisam ser visíveis e distinguíveis."),
], ["Monte uma grade de três cartões com CSS Grid e adapte para uma coluna em telas pequenas.", "Defina variáveis CSS para cor principal, fundo, texto e espaçamento.", "Teste o layout em 360 px, 768 px e 1280 px de largura."], [
("Quando Flexbox costuma ser uma boa escolha?", ["Alinhamento em uma dimensão", "Armazenamento de dados", "Consultas SQL", "Criptografia de senha"], 0, "Flexbox organiza alinhamento e distribuição em uma dimensão principal."),
("Qual técnica ajuda a adaptar layout a telas pequenas?", ["Largura fixa enorme", "Media queries e unidades flexíveis", "Remover todo o texto", "Usar apenas imagens"], 1, "Media queries e medidas flexíveis permitem layouts responsivos."),
("Por que evitar muitos !important?", ["Eles apagam o HTML", "Dificultam entender e manter a cascata", "Impedem responsividade", "São obrigatórios em CSS"], 1, "Uso excessivo aumenta conflitos e reduz previsibilidade dos estilos."),
]),
(16, "JavaScript: lógica, DOM e eventos", "Programação", "120 min", "Crie interações no navegador com funções, eventos e manipulação cuidadosa da página.", [
("Valores e escopo", "const evita reatribuição de uma variável; let permite reatribuição. Tipos, conversões e escopo influenciam o comportamento. Prefira nomes claros e funções pequenas."),
("Condições e arrays", "if/else controla decisões; arrays armazenam listas. map transforma elementos, filter seleciona itens e find localiza um elemento, ajudando a evitar loops repetitivos."),
("DOM e eventos", "document.querySelector localiza elementos e addEventListener registra ações como click e submit. Atualize o conteúdo usando textContent quando possível e evite inserir HTML não confiável."),
("Depuração", "O console do navegador mostra erros e logs. Reproduza o problema, leia a primeira mensagem relevante, inspecione valores e corrija uma causa de cada vez."),
], ["Faça um contador com botões de aumentar, diminuir e zerar.", "Crie uma lista de tarefas com adicionar e remover usando textContent.", "Adicione validação para impedir tarefas vazias e teste com teclado."], [
("Qual método registra um ouvinte de evento?", ["addEventListener", "appendOnly", "makeClick", "runHTML"], 0, "addEventListener associa uma função a um evento."),
("Por que textContent é útil ao exibir texto do usuário?", ["Executa todo HTML automaticamente", "Insere texto sem interpretá-lo como marcação HTML", "Cria senhas seguras", "Substitui o servidor"], 1, "textContent evita interpretar o conteúdo como HTML executável."),
("O que fazer ao investigar um erro JavaScript?", ["Mudar tudo ao mesmo tempo", "Ler o erro, reproduzir e inspecionar valores", "Ignorar o console", "Apagar os arquivos CSS"], 1, "Depuração sistemática reduz hipóteses e ajuda a localizar a causa."),
]),
(17, "Python intermediário: módulos, funções e arquivos", "Programação", "130 min", "Organize programas em módulos, valide dados e manipule arquivos com tratamento de erros.", [
("Funções bem definidas", "Uma função deve ter uma responsabilidade clara, parâmetros explícitos e retorno previsível. Evite depender de variáveis globais quando os dados podem ser passados como argumentos."),
("Módulos e ambientes", "Módulos dividem o projeto em arquivos reutilizáveis. Ambientes virtuais isolam dependências por projeto e facilitam reproduzir instalações em outra máquina."),
("Arquivos e context managers", "with open(...) fecha arquivos mesmo se ocorrer uma exceção. Defina encoding='utf-8' para texto quando apropriado e escolha modos de leitura/escrita com atenção."),
("Tratamento de erros", "Capture exceções específicas e forneça mensagens úteis. Não use except genérico para ocultar bugs; registre o contexto necessário sem expor senhas ou dados pessoais."),
], ["Crie uma função que valide um e-mail de forma básica e documente suas limitações.", "Leia um arquivo de texto com encoding UTF-8 e conte linhas.", "Separe funções de entrada, processamento e saída em módulos diferentes."], [
("Qual é uma vantagem de usar with open(...) ?", ["Garante fechamento adequado do arquivo", "Apaga automaticamente o disco", "Dispensa validação", "Converte tudo em imagem"], 0, "O context manager gerencia o fechamento do recurso."),
("Para que serve um ambiente virtual?", ["Isolar dependências de um projeto", "Aumentar memória RAM", "Criar rede Wi-Fi", "Substituir Python"], 0, "Ambientes virtuais isolam bibliotecas e versões usadas pelo projeto."),
("Qual prática é melhor ao tratar erros?", ["Capturar qualquer erro e ignorar", "Capturar exceções esperadas e explicar a falha", "Mostrar senhas no log", "Reiniciar sempre o PC"], 1, "Tratamento específico preserva sinais úteis para depuração e segurança."),
]),
(18, "Git e GitHub: versionamento profissional", "Desenvolvimento", "100 min", "Registre mudanças, crie ramificações e colabore com segurança usando controle de versão.", [
("Repositório e commits", "Git registra snapshots do projeto. Commits pequenos e descritivos facilitam revisar mudanças, localizar regressões e entender a evolução do código."),
("Branch e merge", "Branches permitem trabalhar em funcionalidades separadas. Após testes e revisão, as alterações podem ser integradas; conflitos precisam ser resolvidos com compreensão do conteúdo, não escolhendo tudo às cegas."),
(".gitignore e segredos", "Arquivos gerados, ambientes virtuais e credenciais normalmente não devem ser versionados. Se um segredo foi enviado ao repositório, removê-lo do último commit pode não bastar: revogue/rotacione a credencial."),
("Colaboração", "Pull requests ajudam a discutir mudanças antes de integrá-las. Leia diffs, execute testes e documente instruções de instalação e execução no README."),
], ["Inicialize um repositório em um projeto de teste e faça o primeiro commit.", "Crie uma branch, altere um arquivo e integre a mudança.", "Adicione venv, arquivos .env e caches ao .gitignore."], [
("O que um commit representa?", ["Um registro de mudanças versionadas", "Uma senha", "Uma conexão Wi-Fi", "Uma cópia de segurança automática externa sempre"], 0, "Commits registram estados e mudanças do projeto no histórico Git."),
("Se uma chave secreta foi publicada, qual é a ação prioritária?", ["Só apagar a linha", "Revogar ou rotacionar a chave e revisar o histórico", "Deixar pública", "Trocar o nome do repositório"], 1, "Uma credencial exposta deve ser invalidada; apagar a linha não garante que deixou de vazar."),
("Por que usar branches?", ["Separar trabalho antes de integrar", "Impedir testes", "Substituir HTML", "Criptografar o monitor"], 0, "Branches permitem desenvolver mudanças de forma isolada."),
]),
(19, "Flask: rotas, templates e formulários", "Desenvolvimento web", "140 min", "Entenda a arquitetura de uma aplicação Flask e construa páginas dinâmicas sem misturar toda a lógica.", [
("Rotas HTTP", "Rotas conectam URLs e métodos HTTP a funções Python. GET normalmente consulta dados; POST envia dados para processamento. A aplicação deve validar entradas e responder com códigos apropriados."),
("Templates Jinja", "render_template entrega dados a arquivos HTML. Herança com extends e blocks evita repetir cabeçalhos e rodapés. O autoescape ajuda a proteger saída HTML, mas não substitui validação e boas práticas."),
("Formulários", "request.form recebe campos de formulários enviados como POST. Valide campos no servidor, normalize dados quando necessário e apresente mensagens claras sem revelar detalhes internos."),
("Sessões e configuração", "Sessões Flask são assinadas com SECRET_KEY; não coloque chaves fixas e públicas em produção. Use variáveis de ambiente, cookies seguros em HTTPS e proteção CSRF para formulários que alteram estado."),
], ["Crie uma rota GET que mostre uma página com um template Jinja.", "Faça um formulário POST que valide um campo obrigatório no servidor.", "Mova a chave secreta para variável de ambiente antes de publicar a aplicação."], [
("Qual é o uso habitual de GET?", ["Consultar um recurso", "Apagar sempre a conta", "Enviar senha por URL", "Alterar permissões sem confirmação"], 0, "GET é destinado à recuperação de recursos e não deve causar alterações de estado."),
("Onde é mais adequado guardar a SECRET_KEY em produção?", ["Em código público", "Em variável de ambiente ou gestão segura de segredos", "No HTML visível", "No nome do site"], 1, "Segredos devem ficar fora do código versionado e ser protegidos no ambiente de execução."),
("A validação feita apenas no navegador é suficiente?", ["Sim", "Não, o servidor também deve validar", "Somente em formulários pequenos", "Se usar CSS"], 1, "O cliente pode ser manipulado; o servidor é a fronteira de confiança."),
]),
(20, "SQL e SQLite: modelagem, consultas e integridade", "Banco de dados", "130 min", "Modele tabelas, relacione dados e escreva consultas seguras para aplicações.", [
("Tabelas e chaves", "Tabelas representam entidades; colunas descrevem atributos. Chaves primárias identificam registros, e chaves estrangeiras representam relações entre tabelas."),
("Consultas essenciais", "SELECT lê dados; WHERE filtra; ORDER BY ordena; GROUP BY agrupa; JOIN combina registros relacionados. Selecione apenas colunas necessárias para reduzir exposição e custo."),
("Parâmetros e injeção", "Nunca monte SQL concatenando diretamente texto fornecido pelo usuário. Use consultas parametrizadas, que separam o comando dos valores e reduzem o risco de injeção SQL."),
("Transações e índices", "Transações agrupam operações que devem ser tratadas em conjunto. Índices podem acelerar buscas, mas ocupam espaço e aumentam custo de escrita; escolha com base em consultas reais."),
], ["Crie tabelas alunos e aulas com chaves primárias.", "Faça uma consulta com WHERE, ORDER BY e JOIN em dados fictícios.", "Substitua uma consulta concatenada por parâmetros preparados."], [
("Qual recurso identifica de forma única cada linha?", ["Chave primária", "Cor de fundo", "Nome do arquivo", "Comentário SQL"], 0, "A chave primária identifica unicamente cada registro."),
("Como reduzir risco de SQL injection?", ["Concatenar toda entrada", "Usar consultas parametrizadas", "Ocultar o botão", "Remover índices"], 1, "Parâmetros mantêm valores separados da estrutura SQL."),
("Índices sempre tornam todas as operações mais rápidas?", ["Sim", "Não; podem ajudar leituras e aumentar custo de escrita", "Só em tabelas vazias", "Apenas no HTML"], 1, "Índices têm custos e devem ser escolhidos de acordo com consultas e dados."),
]),
(21, "APIs REST, JSON e integração entre sistemas", "Desenvolvimento web", "110 min", "Consuma e projete APIs com formatos claros, validação e respostas HTTP coerentes.", [
("O que é uma API", "Uma API define como sistemas trocam informações. Uma API web costuma expor recursos por URLs e métodos HTTP, com contratos de entrada, saída e erros."),
("JSON", "JSON representa objetos, arrays, strings, números, booleanos e null. Valide o formato, os tipos e os campos obrigatórios; um JSON sintaticamente válido ainda pode conter dados semanticamente inválidos."),
("Métodos e status", "GET consulta, POST costuma criar/processar, PUT substitui, PATCH altera parcialmente e DELETE remove. Códigos 2xx indicam sucesso, 4xx problemas da solicitação e 5xx falhas do servidor."),
("Segurança e limites", "Autenticação identifica o cliente; autorização define o que ele pode fazer. APIs precisam validar entradas, limitar requisições, proteger segredos e evitar retornar dados pessoais desnecessários."),
], ["Desenhe um endpoint /api/aulas que retorna uma lista JSON fictícia.", "Defina respostas para sucesso, recurso inexistente e entrada inválida.", "Escreva regras para impedir que um usuário consulte dados de outro usuário."], [
("O que JSON representa?", ["Dados estruturados", "Somente imagens", "Um sistema operacional", "Um protocolo físico de rede"], 0, "JSON é um formato textual para intercâmbio de dados estruturados."),
("O que significa autorização?", ["Verificar o que um usuário pode acessar", "Converter JSON em imagem", "Criar endereço IP", "Comprimir um arquivo"], 0, "Autorização determina permissões após identificar o usuário/cliente."),
("Uma API deve retornar dados pessoais que não são necessários?", ["Sim, sempre", "Não; deve aplicar minimização de dados", "Somente em JSON", "Apenas para ficar rápida"], 1, "Retorne somente os dados necessários para a finalidade solicitada."),
]),
(22, "Cibersegurança aplicada: ameaças e defesa em camadas", "Segurança", "120 min", "Aplique defesa em camadas em contas, computadores, aplicações e redes domésticas.", [
("Modelo de ameaças", "Identifique o que precisa proteger, quem poderia causar dano, caminhos de ataque e impacto. Priorize controles pelo risco, em vez de instalar ferramentas aleatórias."),
("Malware e phishing", "Malware pode roubar dados, espionar ou interromper operações. Phishing usa engano para obter credenciais ou induzir ações. Origem aparentemente conhecida não torna anexos ou links seguros."),
("Defesa em camadas", "Atualizações, MFA, privilégios mínimos, firewall, proteção de endpoint, backups testados e treinamento atuam em conjunto. Nenhuma medida isolada elimina todos os riscos."),
("Privacidade e incidentes", "Colete o mínimo de dados, limite permissões e defina como comunicar incidentes. Preserve evidências e não prometa recuperação antes de avaliar o caso."),
], ["Faça um modelo de ameaça para uma conta de e-mail fictícia.", "Crie um plano de recuperação de conta e teste como restaurar um arquivo de backup.", "Avalie uma mensagem simulada de phishing usando remetente, domínio, urgência e pedido feito."], [
("MFA ajuda principalmente a:", ["Adicionar uma camada de verificação à autenticação", "Garantir que nenhum ataque exista", "Substituir atualizações", "Aumentar armazenamento"], 0, "MFA dificulta o acesso indevido quando uma senha é comprometida."),
("Qual é uma estratégia realista de segurança?", ["Uma única ferramenta resolve tudo", "Combinar controles em camadas", "Desativar backups", "Compartilhar códigos"], 1, "Controles complementares reduzem riscos diferentes."),
("Um backup só é confiável se:", ["Nunca for testado", "A restauração for verificada periodicamente", "Estiver sempre conectado e gravável", "Contiver apenas atalhos"], 1, "Testes de restauração verificam se a cópia realmente pode ser usada."),
]),
(23, "Virtualização, máquinas virtuais e containers", "Infraestrutura", "100 min", "Compreenda como isolar ambientes de teste e empacotar aplicações de forma reproduzível.", [
("Máquina virtual", "Uma VM virtualiza hardware e executa um sistema operacional convidado. É útil para laboratórios isolados, testes de compatibilidade e snapshots, mas consome recursos do computador anfitrião."),
("Hipervisor", "Hipervisores tipo 1 rodam diretamente sobre hardware; tipo 2 funcionam sobre um sistema operacional anfitrião. A nomenclatura pode variar em materiais comerciais; observe o funcionamento real da solução."),
("Containers", "Containers compartilham o kernel do anfitrião e isolam processos e dependências, normalmente com inicialização rápida. Não equivalem a uma VM completa e não devem ser tratados como barreira absoluta de segurança."),
("Reprodutibilidade", "Imagens, arquivos de configuração e versões fixadas tornam ambientes mais previsíveis. Não inclua senhas ou tokens nas imagens; use configurações e segredos externos."),
], ["Desenhe um laboratório com máquina anfitriã, VM de teste e rede isolada.", "Compare VM e container em recursos, isolamento e uso pretendido.", "Documente versões e dependências necessárias para iniciar um projeto Flask."], [
("Uma máquina virtual normalmente inclui:", ["Um sistema operacional convidado", "Somente um arquivo de imagem", "Um cabo físico extra", "Uma conta de rede social"], 0, "Uma VM apresenta hardware virtual ao sistema operacional convidado."),
("Qual diferença importante existe entre container e VM?", ["Container costuma compartilhar o kernel do anfitrião", "Container sempre inclui hardware físico separado", "VM não pode rodar sistema operacional", "São sempre idênticos"], 0, "Containers isolam processos e compartilham o kernel, enquanto VMs virtualizam uma máquina."),
("Onde colocar segredos usados por um container?", ["Dentro da imagem pública", "Em mecanismo externo de configuração/segredos", "No título da janela", "Em comentário HTML"], 1, "Segredos devem ser injetados de forma protegida, não incorporados à imagem."),
]),
(24, "Dados e planilhas: limpeza, análise e visualização", "Dados", "105 min", "Organize dados, verifique qualidade e produza conclusões que possam ser conferidas.", [
("Qualidade de dados", "Dados podem conter valores ausentes, duplicados, formatos inconsistentes e erros de digitação. Antes de analisar, defina o significado de cada coluna e as regras de validação."),
("CSV e planilhas", "CSV armazena valores separados por delimitadores, mas não preserva toda a formatação de uma planilha. Configurações regionais alteram separadores decimais e de campo; importe e confira amostras."),
("Estatística descritiva", "Média é sensível a valores extremos; mediana descreve o centro de forma mais robusta em algumas distribuições. Percentuais precisam de denominador explícito e amostras pequenas pedem cautela."),
("Gráficos honestos", "Escolha gráficos conforme a pergunta: linhas para evolução temporal, barras para categorias e dispersão para relação entre variáveis. Rotule eixos, informe unidades e evite escalas que distorçam a interpretação."),
], ["Monte uma tabela fictícia com pelo menos 20 linhas e identifique duplicatas.", "Calcule média e mediana e explique por que podem divergir.", "Crie um gráfico com título, eixos e unidades adequados."], [
("Qual medida costuma ser menos sensível a um valor extremo?", ["Mediana", "Soma", "Máximo", "Amplitude"], 0, "A mediana depende da posição central e costuma ser mais robusta a extremos."),
("O que deve acompanhar um percentual?", ["Somente uma cor", "Denominador ou contexto da base de cálculo", "Uma senha", "Um arquivo executável"], 1, "Sem o denominador, o percentual pode ser interpretado de forma enganosa."),
("Qual gráfico é frequentemente útil para uma série temporal?", ["Linha", "Pizza com dezenas de fatias", "Texto sem eixos", "Ícone isolado"], 0, "Linhas ajudam a visualizar tendências ao longo do tempo."),
]),
(25, "Inteligência artificial: conceitos, limites e uso responsável", "Inteligência artificial", "100 min", "Entenda conceitos básicos de IA, avalie resultados e proteja dados ao usar ferramentas inteligentes.", [
("IA, aprendizado de máquina e modelos", "IA é um campo amplo; aprendizado de máquina ajusta modelos a partir de dados. Modelos generativos produzem conteúdo com base em padrões aprendidos, mas não garantem verdade ou compreensão humana."),
("Dados e vieses", "Qualidade, representatividade e origem dos dados afetam resultados. Um sistema pode reproduzir vieses ou falhar em grupos e situações pouco representados; avaliação precisa considerar contexto e impacto."),
("Alucinações e verificação", "Sistemas generativos podem apresentar respostas plausíveis e incorretas. Verifique fatos importantes em fontes independentes, teste código em ambiente seguro e não confie em referências que não foram confirmadas."),
("Privacidade e responsabilidade", "Não envie senhas, dados sensíveis ou informações confidenciais sem autorização e compreensão das políticas aplicáveis. Use supervisão humana em decisões importantes e documente limitações."),
], ["Peça a uma ferramenta de IA uma explicação de um conceito e confira três afirmações em fontes independentes.", "Compare uma resposta gerada com um teste real de código em ambiente de desenvolvimento.", "Escreva uma política de uso de IA para uma equipe de estudos."], [
("Uma resposta fluente de IA garante que esteja correta?", ["Sim", "Não; fatos importantes devem ser verificados", "Somente em português", "Apenas quando longa"], 1, "Fluência não é garantia de exatidão; verificação independente é necessária."),
("O que é um risco de dados pouco representativos?", ["Possíveis vieses e falhas em certos contextos", "Mais espaço no SSD", "Aumento físico de RAM", "Fim de toda incerteza"], 0, "Dados não representativos podem produzir resultados injustos ou pouco confiáveis."),
("Qual prática protege a privacidade?", ["Enviar senhas para qualquer ferramenta", "Minimizar dados e obter autorização", "Publicar dados de clientes", "Desativar autenticação"], 1, "Minimização e autorização reduzem exposição desnecessária de informações."),
]),
(26, "Cloud, publicação de sites e configuração de produção", "Infraestrutura", "120 min", "Prepare uma aplicação web para publicação com configurações, logs, HTTPS e cuidados operacionais.", [
("Desenvolvimento e produção", "Ambientes de desenvolvimento facilitam testes; produção atende usuários reais e exige configurações seguras, observabilidade, backups e atualizações. Não use o servidor de desenvolvimento Flask como servidor público de produção."),
("Variáveis de ambiente", "URLs, chaves e configurações variáveis devem ficar fora do código. Diferencie valores públicos de segredos e evite registrar tokens, cookies ou senhas em logs."),
("HTTPS e domínio", "HTTPS protege o tráfego entre cliente e servidor e ajuda a confirmar a identidade do serviço. Configure certificados válidos, redirecionamento adequado e cookies Secure quando houver HTTPS."),
("Operação e monitoramento", "Logs úteis, métricas, alertas, backups e um procedimento de rollback reduzem o tempo de recuperação. Teste atualização e restauração em ambiente controlado antes de mudanças grandes."),
], ["Faça uma checklist de publicação para uma aplicação Flask.", "Liste as variáveis de ambiente necessárias sem colocar valores secretos no arquivo versionado.", "Planeje backup, monitoramento e rollback para uma atualização."], [
("O servidor de desenvolvimento Flask é indicado para produção pública?", ["Sim, sempre", "Não; use uma configuração de servidor apropriada para produção", "Somente com senha curta", "Apenas em celular"], 1, "O servidor de desenvolvimento não é projetado para servir aplicações públicas em produção."),
("Qual é a função principal do HTTPS?", ["Proteger o tráfego e autenticar o servidor", "Garantir que o site nunca tenha bugs", "Aumentar a RAM", "Substituir backup"], 0, "HTTPS fornece proteção criptográfica ao tráfego e autenticação por certificados."),
("Por que planejar rollback?", ["Para desfazer uma publicação problemática", "Para apagar todos os logs", "Para evitar testes", "Para publicar segredos"], 0, "Rollback permite retornar a uma versão conhecida se a atualização falhar."),
]),
(27, "Diagnóstico integrado: computador lento ou sem internet", "Suporte técnico", "110 min", "Use uma árvore de decisão para separar problemas de hardware, sistema, aplicativos e conectividade.", [
("Defina o sintoma", "Pergunte o que falha, desde quando, com que frequência e o que mudou. Diferencie lentidão geral, falha em um aplicativo, perda de conexão e falha de resolução DNS."),
("Coleta de evidências", "Observe CPU, RAM, disco, temperaturas reportadas, mensagens de erro e estado da rede. Compare antes e depois de uma mudança controlada; registre data, condições e resultado."),
("Isolamento por camadas", "Para rede, verifique link físico, Wi-Fi, IP, gateway, DNS e destino. Para lentidão, examine inicialização, recursos, armazenamento, atualizações e integridade antes de considerar reinstalação."),
("Comunicação e prevenção", "Explique o diagnóstico em linguagem simples, informe incertezas e peça autorização antes de ações que alterem dados. Termine com ações realizadas, testes de confirmação e recomendações."),
], ["Crie uma árvore de decisão para o caso 'nenhum site abre'.", "Simule um diagnóstico de lentidão e preencha hipótese, teste, evidência e conclusão.", "Escreva um relatório de suporte sem incluir senhas ou dados desnecessários."], [
("Qual é uma boa primeira etapa de diagnóstico?", ["Formatar sem investigar", "Definir o sintoma e coletar evidências", "Desativar todas as proteções", "Trocar todas as peças"], 1, "Uma descrição precisa e evidências orientam testes proporcionais ao problema."),
("Se sites não abrem, mas o Wi-Fi aparece conectado, isso prova internet funcionando?", ["Sim", "Não; ainda é preciso testar IP, gateway, DNS e destino", "Sim, em qualquer situação", "Só se o monitor for novo"], 1, "Conexão ao ponto de acesso não garante acesso à internet ou DNS funcional."),
("Ao terminar o atendimento, o técnico deve:", ["Esconder o que fez", "Registrar ações, resultados e próximos passos", "Apagar os registros", "Compartilhar dados do cliente"], 1, "Documentação melhora transparência, continuidade e prevenção."),
]),
(28, "Projeto prático: construa um portal de estudos", "Projeto integrador", "180 min", "Planeje um pequeno portal com páginas, dados, formulários, testes e documentação.", [
("Requisitos e escopo", "Defina público, objetivos, páginas e critérios de aceite antes de programar. Separe requisitos essenciais de melhorias futuras para manter o projeto executável."),
("Arquitetura", "Separe rotas, templates, estilos, dados e lógica. Evite duplicar código e escolha uma estrutura que outra pessoa consiga compreender."),
("Testes e segurança", "Teste caminhos felizes, campos vazios, dados inválidos, acesso sem login e erros de rota. Use consultas parametrizadas, valide entradas no servidor e não exponha segredos."),
("Documentação e entrega", "Inclua instalação, dependências, variáveis necessárias, como executar, funcionalidades, limitações e passos para testes. Registre decisões e deixe claro o que ainda não está implementado."),
], ["Desenhe as páginas inicial, catálogo, aula e login antes de codificar.", "Implemente um formulário validado no servidor e uma lista de conteúdo fictício.", "Crie README com instalação, execução e checklist de testes; peça a alguém para seguir as instruções."], [
("Por que definir critérios de aceite?", ["Para saber como verificar que o requisito foi cumprido", "Para evitar qualquer teste", "Para substituir documentação", "Para ocultar bugs"], 0, "Critérios claros tornam o resultado verificável."),
("Onde devem ficar credenciais de produção?", ["No repositório público", "Em configuração segura fora do código", "No título do HTML", "Em comentário CSS"], 1, "Credenciais devem ser protegidas e não versionadas."),
("O que um README útil deve incluir?", ["Só o nome do autor", "Instalação, execução, dependências e testes", "Senhas de usuários", "Somente capturas de tela"], 1, "Um README reproduzível ajuda a instalar, executar e manter o projeto."),
]),
]

def build_lessons():
    lessons = []
    for lesson_id, title, category, duration, summary, theory, steps, quiz in RAW_LESSONS:
        lessons.append({
            "id": lesson_id,
            "level": "Curso completo gratuito",
            "title": title,
            "duration": duration,
            "category": category,
            "free": True,
            "summary": summary,
            "theory": theory,
            "steps": steps,
            "quiz": [
                {"q": q, "options": options, "answer": answer, "explain": explain}
                for q, options, answer, explain in quiz
            ],
        })
    return lessons

EXPANDED_LESSONS = build_lessons()
