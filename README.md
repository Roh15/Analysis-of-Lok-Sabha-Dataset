# Analysis of Lok Sabha Dataset
A dataset and some analysis of all the Lok Sabha debates up till 25th March 2021.

## Link to the report
https://drive.google.com/file/d/14jdKCWyNvMK1_zHh7Umq7fMoeTg4xiAu/view?usp=sharing

## Link to the slides describing the process
https://docs.google.com/presentation/d/1iJh1Oz8q1Nbub8ikniGeBbv1oHnvrm0qxQ9noowQcN4/edit?usp=sharing

## Link to all the data files
* **PDFs**: https://drive.google.com/drive/folders/13f2_rkDOzMOY6UYozx2gcPMrIii-475k?usp=sharing
* **Text Files**: https://drive.google.com/drive/folders/14IBwHoa32ANWQhVATjbFoU6MkwZkOk2g?usp=sharing

## Interface
An interface to visualize the locations mentioned in the 16th Lok Sabha. It can be visited [here](https://ls-analysis.herokuapp.com/).

## Notebook descriptions

### Dataset Creation

* **Lok Sabha Data Scraper**: Contains scripts to download the lok sabha debate pdfs available at Lok Sabha Digital Library.
* **Aryan2 to Unicode Map**: Contains script for knowing the font(s) used in a pdf along with their encoding and a Aryan2 font encoding to Unicode encoding map.
* **OCR**: Contains script for performing on pdfs.
* **Lok Sabha Data Harshil**: Contains script for cleaning the text and storing them in desired format as a csv file.

### Analysis

* **NER and POS Tagging**: Contains scripts to perform NER on English data and POS Tagging on Hindi data. Also includes a failed attempt at NER using Deep Pavlov for Hindi data.
* **Calculate Stats**: Contains scripts to calculate various stats such as number of files in each Lok Sabha, number of entites, frequency of entites, etc.
* **Hindi NER**: Contains trials run for NER for Hindi text using Flair and IndicBart. 

### Interface

* **Geocoding (GoogleMapsAPI)**: Contains script for getting the geo-coordinates (latitude and longitude) of a location using Google Maps API.
* **Geocoding (NominatimAPI)**: Contains script for getting the geo-coordinates (latitude and longitude) of a location using Nominatim API. Also, contains script for getting names of all countries, states and cities/towns in the world and translating them into hindi using google translate.
