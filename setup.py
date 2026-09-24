from setuptools import setup, find_packages

setup(
    name="mahe-v2",
    version="2.0.0",
    description="MAHE V2: Multi-Agent Hallucination Evaluator",
    author="Ansh Tiwari",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi>=0.104.0",
        "uvicorn[standard]>=0.23.2",
        "pydantic>=2.4.2",
        "pydantic-settings>=2.0.3",
        "httpx>=0.25.0",
        "websockets>=12.0",
        "prometheus-client>=0.17.1",
        "redis>=5.0.1",
        "motor>=3.3.1",
        "tenacity>=8.2.3",
        "structlog>=23.2.0"
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "pytest-asyncio>=0.21.1",
            "pytest-cov>=4.1.0",
            "ruff>=0.1.5",
            "mypy>=1.7.0",
            "black>=23.11.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "mahe=mahe.cli:main",
        ],
    },
    python_requires=">=3.10",
)
