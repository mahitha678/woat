from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="watbot",
    version="0.1.0",
    author="Nithin Jambula",
    author_email="nithin@example.com",
    description="WhatsApp & Instagram Automation Bot Library with AI-powered responses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nithin434/woat",
    project_urls={
        "Bug Tracker": "https://github.com/nithin434/woat/issues",
        "Documentation": "https://github.com/nithin434/woat",
        "Source Code": "https://github.com/nithin434/woat",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=3.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950",
        ],
    },
    include_package_data=True,
    package_data={
        "watbot": ["*.js", "*.json"],
    },
    entry_points={
        "console_scripts": [
            "watbot=watbot.cli:main",
        ],
    },
    keywords="whatsapp instagram automation bot ai chatbot messaging",
    zip_safe=False,
)
