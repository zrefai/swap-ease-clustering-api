# Introduction

The swap-ease-clustering-api contains the methods to cluster NFTRank data. There are also methods to get and add to mongoDB databases

# Getting Started

## Install Dependencies

Make sure your python version is < 3.10. Preferably 3.8.

At the project root, we run this command below. It will create our python virtual environment

```
python3 -m venv venv
```

Next we need to activate the virtual env using

```
. venv/bin/activate
```

Using the requirements.txt file, we can install all necessary dependencies on the virtual env using

```
pip install -r requirements.txt

// If top fails, upgrade pip and re-run
pip install --upgrade pip
```

All dependencies should now be in the virtual environment. If we want to update the dependencies list in requirements.txt we can use the line below. We need to have the necessary updates installed before freezing though.

```
pip freeze > requirements.txt
```

## Starting API

To start, run (from root)

```
python3 src/app.py
```

## Testing

To run the testing suite, run from root

```
pytest

# For coverage report in html
pytest --cov --cov-config=.coveragerc --cov-report=html
```

## Trouble shooting

If a problem occurs with pip, say "No module name pip found", run this command

```
python3 -m ensurepip --default-pip
```

If you need to deactivate the virtual environment

```
deactivate
```

If you absolutely can't figure out whats going on with the packages (for some reason it's just not working), you can delete venv and run through installing the dependencies from scratch

# Build and Test

TODO: Describe and show how to build your code and run the tests.

# Contribute

TODO: Explain how other users and developers can contribute to make your code better.

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:

- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)
