publish:
	sudo rm -rf build dist s3ctl.egg-info
	sudo python3 setup.py sdist
	sudo python3 setup.py install
	python3 -m twine upload --repository testpypi dist/*
