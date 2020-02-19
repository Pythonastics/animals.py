<div align="center">
  <img src="https://img.shields.io/pypi/v/animals.py" alt="pkg-version">
  <img src="https://img.shields.io/pypi/wheel/animals.py" alt="wheel">
  
</div>

# animals.py
A Python module to get random image/facts of different animals

# Getting started

**Installation**
```sh
pip install animals.py
```
**Usage**
```py
from animals import Animals

animal = Animals('cat')

print(animal.image()) # Prints the url for the image
print(animal.fact()) # Prints the fact of the animal
```

# Thanks to

* [requests](https://github.com/psf/requests)
* [some-random-api](https://some-random-api.ml)
