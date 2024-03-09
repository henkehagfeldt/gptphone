import setuptools

setuptools.setup(
    name="GptPhone",
    version="0.1.0",
    author="Henrik Hagfeldt",
    author_email="henke9606@hotmail.com",
    description="Let's you dial up an AI assistant through the power of python!",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/henkehagfeldt/gptphone",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pyaudio>=0.2.14',
        'requests>=2.31.0',
        'SpeechRecognition>=3.10.1',
        'pyttsx3>=2.90',
        'openai>=1.13.3'
    ],
)