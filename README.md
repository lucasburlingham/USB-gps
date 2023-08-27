# USB-GPS

## Description

This is a simple python script to read data from a USB GPS device and plot that data on a map.

## Requirements

* Python 3
* gpsd-py3
* gpsd
* websockets
* make

## Installation

```bash
git clone https://github.com/lucasburlingham/USB-gps
cd USB-gps
make install
```

## Usage

```bash
make run
```

or

```bash
python3 main.py
```

Tested on Arch and Ubuntu 22.04 with a [VK-162 G-Mouse USB GPS Dongle](https://www.amazon.com/gp/product/B078Y52FGQ/).

## License

MIT License - see the [LICENSE](LICENSE.md) file for details