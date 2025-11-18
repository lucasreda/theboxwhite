# DarkBox España - Landing Page

Landing page simples em HTML puro para DarkBox España.

## 🚀 Como Executar

### Opção 1: Python (Recomendado)

Se você tem Python instalado:

```bash
python3 server.py
```

O servidor iniciará em `http://localhost:8000` e abrirá automaticamente no navegador.

### Opção 2: Node.js

Se você tem Node.js instalado:

```bash
npm install
npm start
```

Ou diretamente:

```bash
npx http-server . -p 8000 -o
```

### Opção 3: PHP

Se você tem PHP instalado:

```bash
php -S localhost:8000
```

### Opção 4: Qualquer servidor HTTP

Você pode usar qualquer servidor HTTP estático apontando para a raiz do projeto. O arquivo `index.html` será servido automaticamente.

## 📁 Estrutura

```
landingespana/
├── index.html      # Landing page principal
├── server.py       # Servidor Python simples
├── package.json    # Configuração Node.js (opcional)
└── README.md       # Este arquivo
```

## 🌐 Acessar

Após iniciar o servidor, acesse:

- **Local**: http://localhost:8000
- **Rede local**: http://[seu-ip]:8000

## 📝 Notas

- O arquivo `index.html` contém todo o HTML, CSS e conteúdo
- Não há dependências externas
- Design responsivo para desktop e mobile
- Pronto para produção (basta servir o arquivo `index.html`)

