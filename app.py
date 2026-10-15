from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from pathlib import Path
from functools import wraps
from expanded_lessons import EXPANDED_LESSONS

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "curso.db"
app = Flask(__name__)
app.config["SECRET_KEY"] = "troque-esta-chave-por-uma-chave-longa-e-aleatoria"
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

# Conteúdo inicial: básico gratuito + trilha avançada de demonstração.
LESSONS = [
    {
        "id": 1, "level": "Básico gratuito", "title": "Como um computador funciona",
        "duration": "35 min", "category": "Fundamentos", "free": True,
        "summary": "Hardware é a parte física; software são os programas e instruções. O sistema operacional coordena recursos e permite que os aplicativos funcionem.",
        "theory": [
            ("Hardware", "Processador (CPU), memória RAM, armazenamento, placa-mãe, fonte, GPU e periféricos. Cada peça tem uma função específica."),
            ("Software", "Sistema operacional, drivers, aplicativos e utilitários. Atualizações corrigem falhas, melhoram compatibilidade e podem fechar brechas de segurança."),
            ("Como os componentes trabalham juntos", "A CPU executa instruções, a RAM mantém dados em uso e o SSD/HDD guarda arquivos mesmo quando o computador está desligado.")
        ],
        "steps": ["Identifique CPU, RAM e armazenamento no seu computador.", "Abra o Gerenciador de Tarefas e observe CPU, memória e disco.", "Anote a diferença entre memória RAM e espaço do SSD."],
        "quiz": [
            {"q": "Qual componente mantém dados temporários dos programas em execução?", "options": ["SSD", "RAM", "Fonte", "Gabinete"], "answer": 1, "explain": "A RAM é uma memória volátil usada durante a execução."},
            {"q": "Qual é a função principal do sistema operacional?", "options": ["Apenas exibir imagens", "Gerenciar recursos e oferecer serviços aos aplicativos", "Substituir a CPU", "Aumentar fisicamente a RAM"], "answer": 1, "explain": "O sistema operacional coordena hardware, arquivos, processos e usuários."}
        ]
    },
    {
        "id": 2, "level": "Básico gratuito", "title": "Windows, arquivos e produtividade",
        "duration": "45 min", "category": "Sistema operacional", "free": True,
        "summary": "Organize arquivos por pastas, entenda extensões, use atalhos e mantenha o sistema atualizado.",
        "theory": [
            ("Arquivos e extensões", "Extensões como .pdf, .jpg, .docx, .zip e .py indicam formatos. A extensão não garante que um arquivo seja seguro."),
            ("Pastas e cópias de segurança", "Organize por projeto e data. Mantenha cópias importantes em outro dispositivo ou serviço confiável."),
            ("Atalhos úteis", "Ctrl+C copia, Ctrl+V cola, Ctrl+Z desfaz, Win+E abre o Explorador e Ctrl+Shift+Esc abre o Gerenciador de Tarefas.")
        ],
        "steps": ["Crie uma pasta chamada Estudos e subpastas por assunto.", "Pratique cinco atalhos de teclado.", "Faça uma cópia de um arquivo importante em outro local."],
        "quiz": [
            {"q": "Qual atalho abre o Gerenciador de Tarefas diretamente?", "options": ["Win+E", "Ctrl+Shift+Esc", "Alt+F4", "Ctrl+P"], "answer": 1, "explain": "Ctrl+Shift+Esc abre o Gerenciador de Tarefas."},
            {"q": "Qual prática ajuda a proteger arquivos importantes?", "options": ["Deixar tudo na Área de Trabalho", "Usar apenas uma cópia", "Manter cópias de segurança", "Renomear tudo como .exe"], "answer": 2, "explain": "Backups reduzem o risco de perda de dados."}
        ]
    },
    {
        "id": 3, "level": "Avançado • R$ 10", "title": "Diagnóstico profissional de desempenho",
        "duration": "90 min", "category": "Manutenção", "free": False,
        "summary": "Aprenda um método reproduzível para identificar gargalos sem instalar programas suspeitos nem alterar configurações às cegas.",
        "theory": [
            ("Diagnóstico antes da solução", "Registre sintomas, quando começaram, mudanças recentes e mensagens de erro. Mude uma variável por vez para descobrir a causa."),
            ("CPU, RAM, disco e GPU", "CPU alta pode indicar processos intensivos; RAM saturada pode gerar paginação; disco a 100% pode envolver transferências, atualizações ou falhas; GPU alta pode ser normal em jogos."),
            ("Temperatura e energia", "Aquecimento excessivo pode reduzir frequências. Verifique ventilação, poeira, cabos e especificações do fabricante. Não abra fontes de alimentação."),
            ("Relatório técnico", "Documente problema, evidências, hipótese, teste, resultado e recomendação. Evite prometer ganhos de desempenho sem medições.")
        ],
        "steps": ["Registre uso de CPU, RAM, disco e GPU em repouso e durante uma tarefa.", "Compare os valores antes e depois de fechar um aplicativo pesado.", "Escreva um relatório com hipótese, evidência e próxima ação."],
        "quiz": [
            {"q": "Qual é a melhor primeira etapa ao investigar lentidão?", "options": ["Formatar imediatamente", "Registrar sintomas e medir recursos", "Desativar todos os serviços", "Apagar arquivos aleatórios"], "answer": 1, "explain": "Medir e registrar evita mudanças desnecessárias e ajuda a isolar a causa."},
            {"q": "RAM frequentemente cheia pode provocar:", "options": ["Paginação e lentidão", "Mais espaço físico no SSD", "Aumento automático da VRAM dedicada", "Desligamento do monitor apenas"], "answer": 0, "explain": "O sistema pode mover dados entre RAM e armazenamento, com perda de desempenho."},
            {"q": "Por que mudar uma variável por vez?", "options": ["Para dificultar o diagnóstico", "Para saber qual alteração causou o resultado", "Para impedir atualizações", "Para apagar registros"], "answer": 1, "explain": "Testes controlados ajudam a relacionar causa e efeito."}
        ]
    },
    {
        "id": 4, "level": "Avançado • R$ 10", "title": "Redes: IP, DNS, gateway e diagnóstico",
        "duration": "100 min", "category": "Redes", "free": False,
        "summary": "Entenda os componentes básicos de uma rede e pratique comandos de diagnóstico no Windows.",
        "theory": [
            ("Endereço IP e máscara", "O IP identifica uma interface numa rede. A máscara/prefixo indica qual parte corresponde à rede e qual identifica o dispositivo."),
            ("Gateway e DNS", "O gateway encaminha tráfego para outras redes. O DNS traduz nomes como exemplo.com em endereços IP."),
            ("Comandos seguros", "ipconfig mostra configurações; ping testa conectividade básica; tracert mostra saltos de rota; nslookup consulta DNS. Resultados podem variar conforme firewall e rede."),
            ("Método de diagnóstico", "Verifique cabo/Wi-Fi, endereço IP, gateway, resolução DNS e acesso ao destino. Teste uma hipótese de cada vez.")
        ],
        "steps": ["Execute ipconfig no Prompt de Comando e identifique IPv4, máscara e gateway.", "Use nslookup example.com e observe o resultado.", "Use ping 1.1.1.1 e depois ping example.com; compare os resultados."],
        "quiz": [
            {"q": "Qual serviço converte nomes de domínio em endereços IP?", "options": ["DNS", "GPU", "DHCP apenas", "USB"], "answer": 0, "explain": "O DNS resolve nomes de domínio para registros como endereços IP."},
            {"q": "Se um IP público responde ao ping, mas um nome não resolve, qual hipótese faz sentido investigar?", "options": ["Problema de DNS", "Monitor queimado", "RAM fisicamente maior", "Teclado sem fio"], "answer": 0, "explain": "A conectividade pode existir enquanto a resolução de nomes falha."},
            {"q": "O gateway padrão normalmente serve para:", "options": ["Resfriar a CPU", "Encaminhar tráfego para outras redes", "Guardar senhas", "Criar arquivos PDF"], "answer": 1, "explain": "O gateway encaminha pacotes destinados a redes externas à rede local."}
        ]
    },
    {
        "id": 5, "level": "Avançado • R$ 10", "title": "Python aplicado à informática",
        "duration": "120 min", "category": "Programação", "free": False,
        "summary": "Use Python para automatizar tarefas pequenas, tratar erros e produzir saídas verificáveis.",
        "theory": [
            ("Variáveis e tipos", "Variáveis associam nomes a valores. Tipos comuns incluem str, int, float, bool, list e dict."),
            ("Condições e repetição", "if/elif/else escolhe caminhos; for e while repetem instruções. Escolha estruturas simples e legíveis."),
            ("Funções e erros", "Funções encapsulam tarefas. try/except trata erros esperados sem esconder falhas indiscriminadamente."),
            ("Arquivos e segurança", "Teste scripts com arquivos fictícios, valide caminhos e mantenha cópias antes de automatizar renomeações ou exclusões.")
        ],
        "steps": ["Crie um script que recebe o nome do usuário e imprime uma saudação.", "Faça uma função que converte minutos em horas e minutos.", "Adicione validação para entradas inválidas e teste pelo menos três casos."],
        "quiz": [
            {"q": "Qual estrutura é usada para definir uma função em Python?", "options": ["func", "def", "make", "function()"], "answer": 1, "explain": "Em Python, funções são definidas com a palavra-chave def."},
            {"q": "Qual é uma boa prática antes de automatizar alterações em arquivos?", "options": ["Executar direto em todos os documentos", "Testar com cópias e validar caminhos", "Ignorar erros", "Desativar o antivírus"], "answer": 1, "explain": "Testes controlados e backups evitam perdas acidentais."},
            {"q": "Para que serve try/except?", "options": ["Tratar exceções esperadas", "Aumentar a velocidade da CPU", "Criar uma placa de rede", "Substituir todas as funções"], "answer": 0, "explain": "try/except permite lidar com erros específicos de execução."}
        ]
    },
    {
        "id": 6, "level": "Avançado • R$ 10", "title": "Cibersegurança e proteção digital",
        "duration": "100 min", "category": "Segurança", "free": False,
        "summary": "Crie hábitos de segurança, reconheça golpes e aplique princípios de proteção de contas e dispositivos.",
        "theory": [
            ("Senhas e autenticação", "Use senhas longas e exclusivas, um gerenciador confiável e autenticação multifator sempre que disponível."),
            ("Phishing e engenharia social", "Desconfie de urgência, anexos inesperados, links encurtados e pedidos de códigos. Confirme solicitações por um canal independente."),
            ("Atualizações e privilégios", "Mantenha sistema e aplicativos atualizados. Use conta padrão no dia a dia e privilégios administrativos apenas quando necessários."),
            ("Resposta a incidentes", "Desconecte o dispositivo da rede se houver indícios relevantes, preserve evidências, altere senhas a partir de um dispositivo confiável e procure suporte especializado.")
        ],
        "steps": ["Ative autenticação multifator em uma conta importante.", "Analise uma mensagem fictícia e marque sinais de phishing.", "Monte uma checklist de atualização e backup mensal."],
        "quiz": [
            {"q": "Qual é a resposta mais segura a um pedido inesperado de código de autenticação?", "options": ["Enviar imediatamente", "Publicar nas redes", "Não compartilhar e confirmar por canal oficial", "Desativar todas as atualizações"], "answer": 2, "explain": "Códigos de autenticação não devem ser compartilhados."},
            {"q": "Por que usar senhas exclusivas?", "options": ["Para impedir qualquer atualização", "Para limitar o impacto do vazamento de uma conta", "Para acelerar a internet", "Para substituir backups"], "answer": 1, "explain": "Uma senha exclusiva evita que vazamentos de uma conta comprometam outras."},
            {"q": "O princípio do menor privilégio recomenda:", "options": ["Usar administrador para tudo", "Conceder somente os acessos necessários", "Compartilhar contas", "Desativar a tela de bloqueio"], "answer": 1, "explain": "Acesso mínimo reduz danos de erros e comprometimentos."}
        ]
    },
    {
        "id": 7, "level": "Avançado • R$ 10", "title": "Projeto final: suporte técnico completo",
        "duration": "150 min", "category": "Projeto", "free": False,
        "summary": "Combine diagnóstico, rede, segurança e documentação em um caso prático de suporte.",
        "theory": [
            ("Cenário", "Um usuário relata lentidão, falhas para abrir sites e mensagens suspeitas recentes. Não presuma que exista uma única causa."),
            ("Plano de trabalho", "Colete informações, peça consentimento, proteja dados, registre métricas, verifique rede e revise alertas de segurança."),
            ("Entrega profissional", "Apresente evidências, ações realizadas, riscos remanescentes e recomendações de manutenção preventiva.")
        ],
        "steps": ["Escreva cinco perguntas para entender o problema.", "Crie uma tabela com sintoma, hipótese, teste e resultado esperado.", "Produza um relatório final de uma página com recomendações priorizadas."],
        "quiz": [
            {"q": "O que torna um relatório técnico útil?", "options": ["Somente opinião", "Evidências, testes, resultados e próximos passos", "Senhas do cliente", "Promessas sem medição"], "answer": 1, "explain": "Um relatório claro permite acompanhar o raciocínio e repetir os testes."},
            {"q": "Antes de acessar arquivos de um cliente, o profissional deve:", "options": ["Pedir consentimento e limitar o acesso ao necessário", "Copiar tudo", "Desativar a segurança", "Compartilhar os arquivos"], "answer": 0, "explain": "Consentimento e minimização de acesso protegem a privacidade."}
        ]
    }
]

# Conteúdo expandido: todas as aulas da NEXA são gratuitas.
LESSONS.extend(EXPANDED_LESSONS)
for _lesson in LESSONS:
    _lesson["free"] = True
    _lesson["level"] = "Curso completo gratuito"

def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with db() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            advanced_access INTEGER NOT NULL DEFAULT 0
        )""")
        conn.execute("""CREATE TABLE IF NOT EXISTS progress (
            user_id INTEGER NOT NULL,
            lesson_id INTEGER NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY (user_id, lesson_id),
            FOREIGN KEY(user_id) REFERENCES users(id)
        )""")

def current_user():
    if "user_id" not in session:
        return None
    with db() as conn:
        return conn.execute("SELECT id, name, email, advanced_access FROM users WHERE id = ?", (session["user_id"],)).fetchone()

def login_required(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        if not current_user():
            flash("Entre na sua conta para continuar.", "info")
            return redirect(url_for("login", next=request.path))
        return fn(*args, **kwargs)
    return wrapped

def has_access(user, lesson):
    # Todo o conteúdo didático é gratuito; login serve apenas para salvar progresso.
    return True

@app.context_processor
def inject_globals():
    return {"site_name": "NEXA | Academia Digital", "current_user": current_user()}

@app.route("/")
def index():
    user = current_user()
    with db() as conn:
        completed = 0
        if user:
            completed = conn.execute("SELECT COUNT(*) FROM progress WHERE user_id = ? AND completed = 1", (user["id"],)).fetchone()[0]
    return render_template("index.html", lessons=LESSONS, completed=completed)

@app.route("/curso")
def course():
    user = current_user()
    with db() as conn:
        done = set()
        if user:
            done = {r["lesson_id"] for r in conn.execute("SELECT lesson_id FROM progress WHERE user_id = ? AND completed = 1", (user["id"],))}
    return render_template("course.html", lessons=LESSONS, done=done, user=user)

@app.route("/aula/<int:lesson_id>", methods=["GET", "POST"])
def lesson(lesson_id):
    item = next((l for l in LESSONS if l["id"] == lesson_id), None)
    if not item:
        abort(404)
    user = current_user()
    if not has_access(user, item):
        return render_template("locked.html", lesson=item), 402
    if request.method == "POST":
        action = request.form.get("action")
        if action == "complete":
            if not user:
                flash("A aula é gratuita. Entre ou crie uma conta para salvar seu progresso.", "info")
                return redirect(url_for("login", next=request.path))
            with db() as conn:
                conn.execute("INSERT INTO progress(user_id, lesson_id, completed) VALUES (?, ?, 1) ON CONFLICT(user_id, lesson_id) DO UPDATE SET completed=1", (user["id"], item["id"]))
            flash("Aula marcada como concluída. Bom trabalho!", "success")
            return redirect(url_for("lesson", lesson_id=lesson_id))
        if action == "quiz":
            score = 0
            answers = {}
            for i, q in enumerate(item["quiz"]):
                try:
                    selected = int(request.form.get(f"q{i}", "-1"))
                except ValueError:
                    selected = -1
                answers[i] = selected
                if selected == q["answer"]:
                    score += 1
            return render_template("lesson.html", lesson=item, score=score, answers=answers)
    return render_template("lesson.html", lesson=item, score=None, answers={})

@app.route("/cadastro", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        if len(name) < 2 or "@" not in email or len(password) < 8:
            flash("Preencha os dados corretamente. A senha precisa ter pelo menos 8 caracteres.", "error")
            return render_template("auth.html", mode="register")
        try:
            with db() as conn:
                conn.execute("INSERT INTO users(name, email, password_hash) VALUES (?, ?, ?)",
                             (name, email, generate_password_hash(password)))
            flash("Conta criada! Agora entre para começar seus estudos.", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Esse e-mail já possui cadastro. Entre na sua conta.", "error")
    return render_template("auth.html", mode="register")

@app.route("/entrar", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        with db() as conn:
            user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        if user and check_password_hash(user["password_hash"], password):
            session.clear()
            session["user_id"] = user["id"]
            flash("Bem-vindo de volta! Sua jornada continua.", "success")
            return redirect(request.args.get("next") or url_for("course"))
        flash("E-mail ou senha incorretos.", "error")
    return render_template("auth.html", mode="login")

@app.route("/sair")
def logout():
    session.clear()
    flash("Você saiu da sua conta.", "info")
    return redirect(url_for("index"))

@app.route("/plano")
def plan():
    return render_template("plan.html")

@app.route("/ativar-acesso-demo", methods=["POST"])
@login_required
def demo_access():
    # Demonstração local: ativa acesso avançado para testar o site.
    # Remova esta rota antes de publicar para o público.
    user = current_user()
    with db() as conn:
        conn.execute("UPDATE users SET advanced_access = 1 WHERE id = ?", (user["id"],))
    flash("Acesso de demonstração ativado nesta instalação. Não é um pagamento real.", "success")
    return redirect(url_for("course"))

@app.route("/saude")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
