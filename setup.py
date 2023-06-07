import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "Text_summarizer_1"
AUTHOR_NAME = "nitanshuj"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "nitanshuj138@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package to summarize text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/" + AUTHOR_NAME + "/" + SRC_REPO,
    project_urls={
        "Bug Tracker": "https://github.com/" + AUTHOR_NAME + "/" + SRC_REPO + "/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)