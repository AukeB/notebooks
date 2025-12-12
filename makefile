# Default project folder
PROJECT_NAME = notebooks

# Format and lint code with Ruff
ruff:
	uv run ruff check $(PROJECT_NAME) --fix
	uv run ruff format $(PROJECT_NAME)
	@echo "🔧 Successfully executed ruff."

# Type-check code with Mypy
# --disallow-untyped-calls: Error when calling functions without type hints
# --disallow-untyped-defs: Error on functions without type hints
# --ignore-missing-imports: Suppresses errors about external packages lacking type hints
# --follow-imports=skip: Skips checking imported modules to speed up analysis
mypy:
	uv run mypy $(PROJECT_NAME) \
		--disallow-untyped-calls \
		--disallow-untyped-defs \
		--ignore-missing-imports \
		--follow-imports=skip
	@echo "🔍 Successfully executed mypy."

clean:
	@find . -type d \( \
		-name '__pycache__' \
	\) -exec rm -rf {} +
	@rm -f  .python-version
	@echo "🧹 Successfully cleaned project."

git:
	git add -A
	git commit -m "Updated"
	git push
	@echo "📤 Successfully executed git."

copy:
	uv run marimo export ipynb notebooks/advent_of_code/advent_of_code_2015.py -o notebooks/advent_of_code/advent_of_code_2015.ipynb -f
	uv run marimo export ipynb notebooks/advent_of_code/advent_of_code_2025.py -o notebooks/advent_of_code/advent_of_code_2025.ipynb -f

all:
	make copy
	make clean
	make git
	@echo "⚡ Successfully executed all tasks."