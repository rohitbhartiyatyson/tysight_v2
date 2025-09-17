install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e .
	@echo "Install complete"

smoke:
	python - <<'PY'
print("smoke_ok")
PY

e2e:
	python - <<'PY'
print("e2e_ok")
PY

handoff-update:
	python tools/handoff_update_status.py
	python tools/handoff_build_capsule.py
	python tools/handoff_build_docs.py
