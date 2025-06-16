.PHONY: black-check flake8 test check

black-check:
	poetry run black --check src tests

flake8:
	poetry run flake8 src tests

test:
	poetry run pytest

ci-check: black-check flake8 test
