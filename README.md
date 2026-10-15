# NEXA Academia Digital — Flask

Protótipo de plataforma de curso de informática em português, com:
- Página inicial responsiva e visual profissional
- Cadastro, login e logout
- Senhas armazenadas com hash via Werkzeug
- SQLite para usuários e progresso
- Básico gratuito e trilha avançada protegida
- Aulas com teoria, resumo digital, atividades e quizzes corrigidos
- Plano avançado anunciado por R$ 10
- Botão de acesso de demonstração local (não é pagamento real)

## 1. Instalar Python e dependências

Abra o terminal nesta pasta e execute:

```bash
python -m pip install flask werkzeug
```

## 2. Iniciar o site

```bash
python app.py
```

Abra `http://127.0.0.1:5000`.

A base SQLite `curso.db` é criada automaticamente na primeira execução.

## 3. Testar cadastro e login

1. Clique em “Começar grátis”.
2. Crie uma conta com e-mail e senha de pelo menos 8 caracteres.
3. Abra Cursos e comece as aulas básicas.
4. Para testar aulas avançadas sem cobrança, use “Ativar acesso de demonstração”. Esse recurso existe somente para desenvolvimento.

## 4. Antes de colocar na internet

Este projeto é uma base inicial, não um serviço de pagamentos pronto para produção:
- Troque `SECRET_KEY` por uma variável de ambiente longa e aleatória.
- Desative `debug=True` e use um servidor WSGI apropriado.
- Configure HTTPS, cookies `Secure`, limitação de tentativas de login, proteção CSRF e política de privacidade.
- Remova a rota `/ativar-acesso-demo`.
- Integre um gateway de pagamento (por exemplo, checkout hospedado) e confirme o pagamento por webhook validado no servidor antes de ativar o acesso avançado.
- Faça backup do banco e teste em ambiente de homologação.
- Atualize e revise os conteúdos pedagógicos antes de comercializar. O curso incluído é uma trilha inicial com módulos demonstrativos, não uma formação técnica certificada.

## Estrutura

```text
curso_informatica_pro/
├── app.py
├── curso.db           # criado ao iniciar
├── requirements.txt
├── README.md
├── static/
│   └── style.css
└── templates/
    ├── base.html
    ├── index.html
    ├── course.html
    ├── lesson.html
    ├── auth.html
    ├── locked.html
    └── plan.html
```


## Conteúdo ampliado

O curso agora inclui a trilha ampliada no arquivo `expanded_lessons.py`, mantendo os templates e estilos existentes. Todas as aulas são gratuitas. A trilha aborda montagem e compatibilidade de PCs, BIOS/UEFI, armazenamento e backup, administração do Windows, Linux, redes, HTML, CSS, JavaScript, Python, Git, Flask, SQL, APIs, cibersegurança, virtualização, análise de dados, IA, publicação de sites, diagnóstico e projeto integrador.

A página `/curso` oferece busca por título/resumo e filtro por categoria. Cada aula inclui teoria por tópicos, laboratório prático e questionário com explicações.
