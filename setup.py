from setuptools import find_packages, setup

setup(
    name="E_commerce_ChatBot",
    version="0.0.1",
    author="Jatin",
    author_email="sareenjatin002@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain-google-genai','datasets','pypdf','python-dotenv','flask']
)