try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = [
	"description": "Email client written in Python",
	"author": "Andrew Darnton",
	"url": "github.com/IrrelevantPenguin",
	"download_url": "github.com/IrrelevantPenguin",
	"author_email": "andrew.darnton12@gmail.com",
	"version": "0.1",
	"install_requires": ["nose"],
	"packages": ["snorkel"],
	"scripts": [],
	"name": "Snorkel"
	]

setup(**config)
