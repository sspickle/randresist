from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='randresist',
      version='0.01',
      description='A simple random resistor generator',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/sspickle/randresist',
      author='Steve Spicklemire',
      author_email='steve@spvi.com',
      license='MIT',
      packages=['randresist'],
      install_requires=[
          'numpy',
      ],
      zip_safe=False,
)
