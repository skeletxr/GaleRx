from setuptools import setup, find_packages

setup(
    name='GaleRx',
    version='0.1',
    author='saket',
    install_requires=[
        'sentence-transformers==2.2.2',
        'langchain',
        'flask',
        'pypdf',
        'python-dotenv',
        'pinecone[grpc]',
        'langchain-pinecone',
        'langchain_openai',
        'langchain_community',
        'langchain_experimental',
    ],
)