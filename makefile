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

all:
	make clean
	make git
	@echo "⚡ Successfully executed all tasks."