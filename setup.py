from setuptools import setup, find_packages

setup(
    name='dtreeviz',
    version='0.2.1',
    url='https://github.com/parrt/dtreeviz',
    license='MIT',
    packages=find_packages(),
    install_requires=['graphviz>=0.9','pandas','numpy','scikit-learn','matplotlib'],
    python_requires='>=3.6',
    author='Terence Parr and Prince Grover',
    author_email='parrt@cs.usfca.edu',
    description='A python library for sci-kit learn decision tree visualization',
    keywords='machine-learning data structures trees visualization',
    classifiers=['License :: OSI Approved :: MIT License',
                 'Intended Audience :: Developers']
)
