from setuptools import find_packages, setup



setup(
    
    name = "MCQ_GENERATOR_PROJECT_LLM",
    version = "0.0.1",
    author = "Rohit Bharti",
    author_email = "rohit.bharti8211@gmail.com",
    install_requires = ["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages = find_packages()
    
)