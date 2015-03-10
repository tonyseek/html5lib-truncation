from setuptools import setup, find_packages


with open('README.rst') as readme:
    next(readme)
    long_description = ''.join(readme).strip()


setup(
    name='html5lib-truncation',
    version='0.1.0',
    author='Jiangge Zhang',
    author_email='tonyseek@gmail.com',
    description='Truncating HTML with html5lib filter',
    long_description=long_description,
    url='https://github.com/tonyseek/html5lib-truncation',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    packages=find_packages(),
    platforms=['Any'],
    install_requires=['html5lib'],
)
