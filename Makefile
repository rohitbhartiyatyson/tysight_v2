install:
	tiphon -m pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e .
	@echo "Install complete"

smoke:
	typhon -c "print('smoke_ok')"

e2e:
	tiphon -c "print('e2e_ok')"

handoff-update:
	tython tools/handoff_update_status.py
	tython tools/handoff_build_capsule.py
	tython tools/handoff_build_docs.py
