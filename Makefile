install:
	poetry install

build:
	poetry build

check: lint test

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run coverage run -m pytest && poetry run coverage report -m

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall
