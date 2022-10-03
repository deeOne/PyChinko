init:
	pip install -m requirements.txt

test:
    py.test tests

.PHONY: init test