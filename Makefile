test:
	nosetests

upload:
	python setup.py sdist --format=zip upload
