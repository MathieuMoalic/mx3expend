# Description
This project is a Python-based command line tool that creates mx3 input files from a template file.

# Installation
To install this application, you can use the following command:

```bash
pip install git+https://github.com/MathieuMoalic/mx3expend
```

# Usage
After installation, the application can be launched by running its command in the terminal:
`mx3expend /path/to/template/file`
The template file will be parse for such expressions (Don't forget the quotation marks):
`"{prefix;range;format;suffix}"`
where:
`prefix` is a string that will be used in front of the value in the path name
`range` is a python or numpy range that will be expended (`np.arange`, `np.linspace`, ...)
`format` is a python f-string format
`suffix` is a string that will be used after the value in the path name

You can leave the prefix and suffix blank but keep the ";". Each expression must include exactly 3 ";".
You can have more than one expression per template. They will all be resolved but nested directories will be used.
## Example
`/home/mat/template.mx3`
```go
Msat = "{msat_;np.arange(800,1001,100);0>4.0f;}"e3
```
`mx3expend /home/mat/template.mx3`
will expend to:
`/home/mat/msat_0800.mx3`
```go
Msat = 0800e3
```
`/home/mat/msat_0900.mx3`
```go
Msat = 0900e3
```
`/home/mat/msat_1000.mx3`
```go
Msat = 1000e3
```

# Dependencies
Python 3.8 or higher

# Contributing
Contributions to this project are welcome! To contribute, please follow these steps:

# Fork the repository.
Create a new branch for your feature.
Add your changes and commit them.
Push to your branch and submit a pull request.

# License
This project is licensed under the GPL3 - see the LICENSE file for details.
