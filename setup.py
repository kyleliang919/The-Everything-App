from setuptools import find_packages
from setuptools import setup

setup(
    name="theEverythingApp",
    version="0.0.0",
    license="GNU General Public License v2.0",
    author="Kaizhao Liang",
    author_email="kyleliang919@gmail.com",
    description="One App to rule them all",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=["revChatGPT"],
    url="https://github.com/kyleliang919/The-Everything-App",
    install_requires=[
        "httpx",
        "nest-asyncio",
        "OpenAIAuth>=0.0.6",
        "playwright",
        "cf_clearance2>=0.28.3",
    ],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "theEverythingApp = theEverythingApp.__main__:main",
        ]
    },
)