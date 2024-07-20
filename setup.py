import setuptools

with open('README.md', "r", encoding='utf-8') as f:
    long_decription = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to-End-Text-Summarization"
AUTHOR_USER_NAME = "susovanpatra00"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "susovanpatra00@gmail.com"


setuptools.setup(
    name= SRC_REPO,
    version= __version__,
    description= "Python Package for Text Summarization",
    long_description= long_decription,
    long_description_content="text/markdown",
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)