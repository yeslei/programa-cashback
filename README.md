# Programa Cashback

Aplicacao simples para calcular cashback e manter historico de consultas por IP.

O projeto foi criado para o desafio Nology - Estagiario de Dev 2026.

## Funcionamento

O usuario informa:

- tipo de cliente: `normal` ou `vip`
- valor da compra
- percentual de desconto

A API calcula o cashback com as regras:

- o cashback base e 5% sobre o valor final da compra, apos desconto
- cliente `vip` recebe bonus de 10% sobre o cashback base
- compras com valor final acima de R$ 500 recebem cashback em dobro

Cada consulta e salva no banco com:

- IP do usuario
- tipo de cliente
- valor da compra
- desconto
- cashback calculado
- data da consulta

O historico exibido no frontend mostra apenas as consultas do IP que esta acessando a aplicacao.

## Tecnologias

- Backend: Python, FastAPI, SQLAlchemy
- Frontend: Angular
- Banco de dados: Postgres no Supabase
- Deploy da API: Railway
- Deploy do frontend: Render

## Servicos publicados

Preencha abaixo com as URLs do seu deploy:

- Frontend Render: `COLOQUE_AQUI_A_URL_DO_RENDER`
- API Railway: `COLOQUE_AQUI_A_URL_DA_API_NO_RAILWAY`
- Banco: Supabase Postgres

## Endpoints da API

### Status

```http
GET /
```

Resposta esperada:

```json
{
  "status": "ok",
  "service": "cashback-api"
}
```

### Calcular cashback

```http
POST /calculate
```

Body:

```json
{
  "client_type": "vip",
  "price": 600,
  "discount_pct": 20
}
```

Resposta:

```json
{
  "price": 600.0,
  "discount_pct": 20.0,
  "final_price": 480.0,
  "base_cashback": 24.0,
  "vip_bonus": 2.4,
  "total_cashback": 26.4
}
```

### Historico por IP

```http
GET /history
```

Retorna apenas as consultas associadas ao IP do usuario.

## Rodando localmente

### Backend

Crie o ambiente virtual e instale as dependencias:

```bash
py -3.11 -m venv backend/.venv
backend/.venv/Scripts/pip install -r backend/requirements.txt
```

Crie um arquivo `.env` na raiz baseado no `.env_example`:

```bash
cp .env_example .env
```

Configure ao menos:

```env
DATABASE_URL=postgresql+psycopg2://user:password@host:6543/postgres
FRONTEND_URL=http://localhost:4200
```

Suba a API:

```bash
backend/.venv/Scripts/python -m uvicorn backend.app.main:app --reload --port 8000
```

### Frontend

Instale as dependencias:

```bash
cd frontend
npm install
```

Suba o Angular:

```bash
npm start
```

Em desenvolvimento, o frontend usa `/api` com proxy para `http://localhost:8000`.

## Deploy

### Railway - API

Configuracoes principais:

- Root Directory: `backend`
- Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

Variaveis:

```env
DATABASE_URL=COLOQUE_AQUI_A_URL_DO_POSTGRES_SUPABASE
FRONTEND_URL=COLOQUE_AQUI_A_URL_DO_RENDER
```

### Render - Frontend

Configuracoes principais:

- Root Directory: `frontend`
- Build Command: `npm ci && npm run build`
- Publish Directory: `dist/frontend/browser`

Variavel:

```env
BACKEND_URL=COLOQUE_AQUI_A_URL_DA_API_NO_RAILWAY
```

Durante o build, o script `frontend/scripts/write-env.mjs` gera a configuracao do Angular usando `BACKEND_URL`.

## Variaveis e seguranca

O arquivo `.env` nao deve ser versionado.

Use `.env_example` apenas como referencia de configuracao. Nunca coloque senhas, chaves do Supabase ou URLs com credenciais diretamente no README.
