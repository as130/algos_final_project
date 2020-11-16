from setuptools import setup
setup(
	name = 'cli',
	version = '0.1',
	install_requires = ['Click', 'numpy', 'scikit-learn'],
	py_modules = ['cli'],
	entry_points = '''
	[console_scripts]
	cli=cli:cli
	''')