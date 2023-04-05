from setuptools import setup, find_packages

setup(
    name='ChatterAgent',
    version='0.1',
    author='Sevan Brodjian',
    author_email='sevanbro7@gmail.com',
    description='A Python package for spawning agents that interface with the OpenAI ChatGPT API.',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    project_urls={
        'Source': 'https://github.com/SevanBrodjian/ChatAgent',
    },
)