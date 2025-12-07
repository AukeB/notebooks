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
	uv run marimo export ipynb notebooks/advent_of_code_2025.py -o notebooks/advent_of_code_2025.ipynb -f

all:
	make copy
	make clean
	make git
	@echo "⚡ Successfully executed all tasks."