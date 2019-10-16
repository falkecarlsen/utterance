# General purpose utterance script
This script allows you to log and keep track of which specific words and phrases you have used, should you have a need to do so!

## Installation
Clone the repository
```
git clone https://github.com/Badgie/utterance.git
```
Navigate to the cloned directory
```
cd /path/to/utterance
```
Run the install script
```
bash install.sh
```
Restart your terminal and you should now be able to use the `utter` CLI

## Usage
To print help text, pass the argument `-h`.
```
[usr@host ~]$ utter -h
usage: utterance.py [-h] [-a [STRING]] [-r [STRING]] [--avail] [--used]

optional arguments:
  -h, --help   show this help message and exit
  -a [STRING]  add word or phrase to available list
  -r [STRING]  move word or phrase to used list
  --avail      list all available words or phrases
  --used       list all used words or phrases
```
To add a word or phrase to the available list, pass argument `-a` followed by a word or phrase. Phrase should be encased in quotes.
```
utter -a yeet
utter -a "more yeet"
```
To remove a word or phrase from the available list, pass argument `-r` followed by a word or phrase. Phrases should be encased in quotes.
```
utter -r yeet
utter -r "more yeet"
```
To list all available words or phrases, pass argument `--avail`.
```
utter --avail
```
To list all used words or phrases, pass argument `--used`.