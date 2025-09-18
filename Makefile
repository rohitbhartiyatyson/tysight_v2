install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e .
	@echo "Install complete"

smoke:
	python -c "print('smoke_ok')"

e2e:
	python -c "print('e2e_ok')"

handoff-update:
	python tools/handoff_update_status.py
	python tools/handoff_build_capsule.py
	python tools/handoff_build_docs.py
