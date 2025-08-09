from setuptools import setup, find_packages

setup(
    name="agentic-ai-project",
    version="0.1.0",
    description="A template for building Agentic AI systems.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/your-username/agentic-ai-project",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "openai",
        "anthropic",
        "google-generativeai",
        "pandas",
        "numpy",
        "python-dotenv",
        "loguru",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
