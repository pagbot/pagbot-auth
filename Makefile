make revision:
	@alembic revision --autogenerate -m "table"

make upgrade:
	@alembic upgrade head