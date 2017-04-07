# opsgenie-to-graphite-python v0.1.0

This is a simple python script to querry infos form Opsgenie and send them to graphite.

## Requirements

* [graphitesend](https://github.com/daniellawrence/graphitesend)
* [opsgenie-sdk](https://github.com/opsgenie/opsgenie-python-sdk)

## Usage

The minimal command to use is :
```
./opsgenie-to-graphite.py -c "customer_name"
```
The only required parameter is the "-c" which is the name of the customer

You have some parameters that you can specify if needed but they all have default values :
* the '-b' which is the backend that you want to send your data to, the default backend is set to [graphite](http://graphite.readthedocs.io)
* the '-s' which is the schema under which you want to set your data in graphite for example
* the '-H' which is the host of your backend, the default value is localhost
* the '-P' which is the port of your backend, the default value is 2003

## Contributing

Feel free to make a pull request.

## Licence

```
MIT License

Copyright (c) 2017 QuentinDeSoete

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


