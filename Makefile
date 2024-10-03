.PHONY: install
install: ## 🚀 Install the poetry environment and install the pre-commit hooks
	@echo "🎉 Creating virtual environment using pyenv and poetry"
	@poetry install
	@poetry shell
