API FastAPI para cálculo de cashback

Como executar (desenvolvimento):

1. Crie um ambiente virtual e instale dependências:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r backend/requirements.txt
```

2. Defina a variável de ambiente `DATABASE_URL` (opcional). Por padrão usa SQLite em `backend/db.sqlite`.

- Postgres example:
  `DATABASE_URL=postgresql+psycopg2://user:pass@host:5432/dbname`
- MySQL example:
  `DATABASE_URL=mysql+pymysql://user:pass@host:3306/dbname`

3. Rode a aplicação com uvicorn:

```bash
uvicorn backend.app.main:app --reload --port 8000
```

Endpoints:
- `POST /calculate`  -> recebe `{ "client_type": "normal|vip", "price": float, "discount_pct": float }` e retorna o detalhamento de cashback. A requisição registra o histórico associado ao IP do cliente.
- `GET /history` -> retorna o histórico apenas para o IP que fez a requisição.

Observações:
- O código usa SQLAlchemy e suporta Postgres/MySQL via `DATABASE_URL`.
- Para deploy, configure `DATABASE_URL` para apontar para um Postgres/MySQL real.
