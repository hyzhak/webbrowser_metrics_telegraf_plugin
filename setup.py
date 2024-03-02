from setuptools import setup, find_packages

setup(
    name="webbrowser_metrics",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",  # Required for making HTTP requests to Chrome
    ],
    entry_points={
        "console_scripts": [
            "count-chrome-tabs=webbrowser_metrics:main",  # Enables command-line execution
        ],
    },
    # Metadata
    author="Your Name",
    author_email="your.email@example.com",
    description="A utility to count open Chrome tabs and report via Telegraf",
    keywords="chrome tabs telegraf influxdb grafana",
)
