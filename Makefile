install:
	poetry install

build:
	poetry build

lint:
	poetry run flake8 gendiff

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall
