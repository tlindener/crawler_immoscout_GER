# crawler_immoscout_GER
This crawler will crawl all the listings for flats (rent) on the German real estate website www.immobilienscout24.de.

It is running on Python3 and uses BeautifulSoup4.

If you run this tool, it will create two csv files in your home directory.  
  wohnung_data_raw.csv contains the data as it was extracted from the website.
  wohnung_data_clean.csv is already formatted and ready to use for further analysis.
  
The final (and clean) csv contains five variables:
  1.location (location of the real estate object)
  2.price (rent in €)
  3.size(square meters)
  4.location_first(the first piece inside the location variable which should be equal to the street)
  5.location_last(the last piece inside the location variable which should be equal to the city)
  
Note that "," is used for decimal notation.
