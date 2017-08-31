.PHONY: build upload


build:
	python setup.py sdist

upload: build
	twine upload dist/*
