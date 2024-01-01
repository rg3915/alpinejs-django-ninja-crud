lint:
	ruff check --fix --show-fixes .
	ruff format --exclude migrations .

