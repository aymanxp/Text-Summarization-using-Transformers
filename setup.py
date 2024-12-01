#The setup.py script is a crucial element in creating reusable Python packages. 
#It serves two primary purposes:


import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-summarizer-model"
AUTHOR_USER_NAME = "aymanxp"
SRC_REPO = "Text-Summarization-using-Transformers"
AUTHOR_EMAIL = "jhhhh@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Fine-tuning a pre-trained model to perform Text Summarization tasks",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)