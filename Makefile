venv:
	python3 -m venv venv

install: venv
	venv/bin/pip3 install -r requirements.txt
