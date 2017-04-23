# Crawler for flats and houses on immobilienscout24.de
This crawler will crawl all the listings for flats and houses (rent and sale) on the German real estate website www.immobilienscout24.de.

Dependencies

This crawler was programmed with Python3 and BeautifulSoup4. Naturally, you would need to install Python3 as well as the BeautifulSoup4 package. Pandas was used for data wrangling and generating the output. I recommend using Anaconda which already includes Pandas.

Usage

1. Make sure that all dependencies are installed.
2. Download the .py file in this repository.
3. Run the file inside Python
4. Go to your root directory (Home in unix; Documents in Windows)
5. Use either wohnung_data_clean.csv or wohnung_data_raw.csv for further analysis

Output

In your home directory you'll find two similar files: wohnung_data_clean.csv and wohnung_data_raw.csv. Both files contain the same data. However, wohnung_data_clean.csv has already been cleaned and is ready for analysis. If you prefer to work with the data that comes directly from Immobilienscout24.de, then you should use wohnung_data_raw.csv.
There are six variables inside the clean version. Price indicates the price for a given real estate (either rent or total price). size is the size of a listing in square meters. location_first is the most precise location indication (should be equal to the street in most cases). location_last should be equal to the city. real_estate tells you whether it is a flat ("Wohnung") or a house ("Haus"). "ownership" indicates whether the given real estate is for rent ("Miete") or for sale ("Kauf").

Formatting

German formatting conventions are used. This means that ";" is the delimeter inside the .csv file. Also note that the decimal seperator is equal to "," and not "."! Keep these formatting conventions in mind when you read in the data.

Usage

Feel free to use this data and crawler for your personal/academic/commerical projects. If you write an academic paper, I would appreciate to be mentioned by my full name (see bio). Please be polite when crawling. This crawler was not developed to do any harm.
