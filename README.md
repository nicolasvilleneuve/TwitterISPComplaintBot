## TwitterISPComplaintBot
If your internet coming up way slower than you expected/was promised to you by your internet service provider, use this bot to chceck your internet speed, log into twitter and submit a complain to, in this case Bell_Support, since they are the largest internet service provider in Canada. 

## Description
In order to use this bot (and watch it control your computer), all you need to do is replace lines 5 and 6 to match the expected download and upload speed you were promised by your internet service provider, respectively. Additonally, lines 7 and 8 (of the main.py file) need to be re-populated with your twitter username and password, respectively. The code to change out may be denoted by Figure 1, below. 

<img src="https://github.com/nicolasvilleneuve/TwitterISPComplaintBot/blob/main/figures/Figure1.png" alt="Figure 1"> 
Figure 1. The code to change out for your own download/upload speed, followed by your Twitter credentials in the main.py file. 

Additonally, if you are a user of google chrome you will need to provide the path to your chromedriver in line 11 of main.py (exemplified by Figure 2, below). Should you not know how to install this, simply google it and you will find all that you need. If, instead, you use any other internet browser, you may sub this out for the driver required. 

<img src="https://github.com/nicolasvilleneuve/TwitterISPComplaintBot/blob/main/figures/Figure2.png" alt="Figure 2"> 
Figure 2. The code to change out for your own filepath to your desired internet browser driver.  

## Usage
You can freely access and utilize this program so long as you have a version of python 3 (this was made in python 3.9.1), the proper credentials to access Twtiter (with your login credentials), the selenium, and the time module. 


## Contributing/Support 
If you would like to create a PULL request, please feel free. Whether the intent be to pilfer from the code as you like some elements of the app, or to suggest improvements, you are most welcome to. If the changes are to be major, however, please open an issue first so we can discuss if/what you would like to change. Should you have a problem in doing so, please feel free to let me know (my email is on my website so please find it there in case it has changed since writing this).

## License

MIT License

Copyright (c) 2021 Nicolas Villeneuve

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
