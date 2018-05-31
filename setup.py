from setuptools import setup

def readme():
    with open('README.md') as f:
	return f.read()

setup(name='chistes_gallegos',
      version='0.3',
      description='los mejores chistes gallegos',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/victor-fdez/chistes-gallegos',
      author='victor-fdez',
      author_email='victor.j.fdez@gmail.com',
      license='MIT',
      python_requires='~=3.6',
      packages=['chistes_gallegos'],
      zip_safe=False)

