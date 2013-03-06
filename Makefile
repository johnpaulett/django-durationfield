.PHONY: build upload


build:
	python setup.py sdist

upload: build
	python setup.py sdist register upload
