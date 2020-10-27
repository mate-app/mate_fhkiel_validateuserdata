<h1 align="center">
  FH Kiel User Validation Cloud Function for the Official <a href="https://mate-app.de">mate App</a>.
</h1>

<p align="center">
  <a href="https://codecov.io/gh/TobiasPrt/mate_validateuserdata">
    <img src="https://codecov.io/gh/TobiasPrt/mate_validateuserdata/branch/master/graph/badge.svg" />
  </a>
  <a href="https://github.com/TobiasPrt/mate_validateuserdata_/issues/">
    <img src="https://img.shields.io/github/issues/TobiasPrt/mate_validateuserdata"
         alt="Issues">
  </a>
  <a href="https://github.com/TobiasPrt/mate_validateuserdata_/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/TobiasPrt/mate_validateuserdata"
         alt="Contributors">
  </a>
  <a href="https://github.com/TobiasPrt/mate_validateuserdata_/LICENSE.md">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg"
         alt="License">
  </a>
  
  
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>


## Key Features

* sends Post-Request to Website of FH Kiel, grabs cookies and then verifies the legitimacy via parsing

## How To Use
To clone and run this application, you'll need [Git](https://git-scm.com) and [PYTHON 3.8.5+](https://www.python.org) installed on your computer. Then from your command line run:

```bash
# Clone this repository
$ git clone https://github.com/TobiasPrt/mate_fhkiel_validateuserdata

# Go into the repository
$ cd mate_fhkiel_validateuserdata

# Create virtual environment
$ python3 -m venv env

# Install dependencies from requirements
$ pip install -r requirements.txt

# Use functions-framework for python to test and debug locally
$ functions-framework --target=validate_user_date
```

The function is now available on [http://localhost:8080](http://localhost:8080).

## Credits

This function specifically uses the following open source packages:

- [Functions Framwork Python](https://github.com/GoogleCloudPlatform/functions-framework-python)
- [Requests](https://github.com/psf/requests)
- [lxml](https://github.com/lxml/lxml)
- [pytest-cov](https://github.com/pytest-dev/pytest-cov)

## License

MIT

---

> [mate-app.de](https://mate-app.de) &nbsp;&middot;&nbsp;
> Instagram [@officialmateapp](https://www.instagram.com/officialmateapp/) &nbsp;&middot;&nbsp;
> Twitter [@officialmateapp](https://twitter.com/officialmateapp)
