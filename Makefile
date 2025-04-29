.PHONY: dev-up api
dev-up:
	poetry install

api:
	poetry run uvicorn src.api.main:app --reload

.PHONY: snowflake-shell
snowflake-shell:
	@poetry run python - <<'PY'
from src.db import get_conn
cur = get_conn().cursor()
print("Snowflake version →", cur.execute("select current_version()").fetchone()[0])
cur.close()
PY
