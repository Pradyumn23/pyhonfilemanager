# COMPSCI 383 Homework 0 
#  
# Fill in the bodies of the missing functions as specified by the comments and docstrings.


import sys
import csv
import datetime 


# Exercise 0. (8 points)
#  
def read_data(file_name):
    """Read in the csv file and return a list of tuples representing the data.

    Transform each field as follows:
      date: datetime.date
      mileage: integer
      location: string
      gallons: float
      price per gallon: float (you'll need to get rid of the '$')

    Do not return a tuple for the header row.  And for the love of all that's holy, do not use
    primitive string functions for parsing (use the csv modules instead).

    Hint: to parse the date field, use the strptime function in the datetime module, and then
    use datetime.date() to create a date object.

    See: 
      https://docs.python.org/3/library/csv.html
      https://docs.python.org/3/library/datetime.html

    """
    rows = []  # this list should contain one tuple per row
    with open(file_name, 'r') as csvfile:
     
      csv_reader = csv.reader(csvfile, dialect='excel')
      next(csv_reader)
      for row in csv_reader:
        marker = len(row[4])
        date = datetime.datetime.strptime(row[0],"%m/%d/%Y").date()
        mileage = int(row[1])
        location = str(row[2])
        gallons = float(row[3])
        pricePerGallon = float(row[4][1:marker])
        thistuple = (date, mileage, location,gallons,pricePerGallon)
        rows.append(thistuple)

    return rows  # a list of (date, mileage, location, gallons, price) tuples


# Exercise 1. (5 points)
#
def total_cost(rows):
    """Return the total amount of money spent on gas as a float.
    
    Hint: calculate by multiplying the price per gallon with the  number of gallons for each row.
    """
    sum = 0.0
    for row in rows:
      sum += row[4]*row[3]

    return sum # fix this line to return a float 


# Exercise 2. (5 points)
#
def num_single_locs(rows):
    """Return the number of refueling locations that were visited exactly once.
    
    Hint: store the locations and counts (as keys and values, respectively) in a dictionary, 
    then count up the number of entries with a value equal to one.  
    """
    #
    # fill in function body here
    #
    thisdict = {}
    count = 0
    for row in rows:
      if row[2] in thisdict:
        thisdict[row[2]]+=1
      else:
        thisdict[row[2]] = 1

    for x in thisdict:
       if thisdict[x]==1:
         count+=1


    return count  # fix this line to return an int


# Exercise 3. (8 points)
#
def most_common_locs(rows):
    """Return a list of the 10 most common refueling locations, along with the number of times
    they appear in the data, in descending order.  
    
    Each list item should be a two-element tuple of the form (name, count).  For example, your
    function might return a list of the form: 
      [ ("Honolulu, HI", 42), ("Shermer, IL", 19), ("Box Elder, MO"), ... ]

    Hint: store the locations and counts in a dictionary as above, then convert the dictionary 
    into a list of tuples using the items() method.  Sort the list of tuples using sort() or 
    sorted().

    See:
      https://docs.python.org/3/tutorial/datastructures.html#dictionaries
      https://docs.python.org/3/howto/sorting.html#key-functions
    """
    #
    # fill in function body here
    #
    thisdict = {}
    count = 0
    for row in rows:
      if row[2] in thisdict:
        thisdict[row[2]]+=1
      else:
        thisdict[row[2]] = 1

    x = thisdict.items()
    a = sorted(x, key = lambda kv: kv[1])
    number = len(a)-1
    i = 0
    top = []
    while number>=0:
      if(i>=10):
        break
      top.append(a[number])
      number-=1
      i+=1



    return top  # fix this line to return a list of strings


# Exercise 4. (8 points)
#
def state_totals(rows):
    """Return a dictionary containing the total number of visits (value) for each state as 
    designated by the two-letter abbreviation at the end of the location string (keys).  

    The return value should be a Python dictionary of the form:
      { "CA": 42, "HI": 19, "MA": 8675309, ... }

    Hint: to do this, you'll need to pull apart the location string and extract the state 
    abbreviation.  Note that some of the entries are malformed, and containing a state code but no
    city name.  You still want to count these cases (of course, if the location is blank, ignore
    the entry.
    """
    #
    # fill in function body here
    #
    thisdict = {}
    count = 0
    for row in rows:
      thearray = row[2].split(", ")
      place = ''
      if len(thearray) == 0:
        continue
      elif len(thearray) == 1:
        place = thearray[0]
      else:
        place = thearray[1]
      if place in thisdict:
        thisdict[place]+=1
      else:
        thisdict[place] = 1

    return thisdict  # fix this line to return a dictionary mapping strings to ints


# Exercise 5. (8 points)
#
def num_unique_dates(rows):
    """Return the total number unique dates in the calendar that refueling took place.

    That is, if you ignore the year, how many different days had entries? (This number should be 
    less than or equal to 366!)
 
    Hint: the easiest way to do this is create a token representing the calendar day.  These could
    be strings (using strftime()) or integers (using date.toordinal()).  Store them in a Python set
    as you go, and then return the size of the set.

    See:
      https://docs.python.org/3/library/datetime.html#date-objects
    """
    #
    # fill in function body here
    #
    thisset = set()
    for row in rows:
      date = row[0].strftime("%m/%d")
      if date in thisset:
        continue
      else:
        thisset.add(date)


    return len(thisset)  # fix this line to return an int


# Exercise 6. (8 points)
#
def month_avg_price(rows):
    """Return a dictionary containing the average price per gallon as a float (values) for each 
    month of the year (keys).

    The dictionary you return should have 12 entries, with full month names as keys, and floats as
    values.  For example:
        { "January": 3.12, "February": 2.89, ... }

    See:
      https://docs.python.org/3/library/datetime.html
    """
    #
    # fill in function body here
    #
    thisdict = {}
    count = 0
    for row in rows:
      month_name = row[0].strftime("%B")
      if month_name in thisdict:
        thisdict[month_name]=[thisdict[month_name][0]+row[4],thisdict[month_name][1]+1]
      else:
         thisdict[month_name]=[row[4],1]
      

    
    
    for x in thisdict:
     thisdict[x] = thisdict[x][0]/float(thisdict[x][1])
     
   

      

    return thisdict  # fix this line to return a dictionary 


# EXTRA CREDIT (+0 points, do this for fun and glory)
#
def highest_thirty(rows):
    """Return the start and end dates for top three thirty-day periods with the most miles driven.

    The periods should not overlap.  You should find them in a greedy manner; that is, find the
    highest mileage thirty-day period first, and then select the next highest that is outside that
    window).
    
    Return a list with the start and end dates (as a Python datetime object) for each period, 
    followed by the total mileage, stored in a tuple:  
        [ (1995-02-14, 1995-03-16, 502),
          (1991-12-21, 1992-01-16, 456),
          (1997-06-01, 1997-06-28, 384) ]
    """
    #
    # fill in function body here
    #
    return []  # fix this line to return a list of tuples


# The main() function below will be executed when your program is run to allow you to check the 
# output of each function.  Do not modify this code!
def main(file_name):
    rows = read_data(file_name)
    print("Exercise 0: {} rows\n".format(len(rows)))

    cost = total_cost(rows)
    print("Exercise 1: ${:.2f}\n".format(cost))

    singles = num_single_locs(rows)
    print("Exercise 2: {}\n".format(singles))

    print("Exercise 3:")
    for loc, count in most_common_locs(rows):
        print("\t{}\t{}".format(loc, count))
    print("")

    print("Exercise 4:")
    for state, count in sorted(state_totals(rows).items()):
        print("\t{}\t{}".format(state, count))
    print("")

    unique_count = num_unique_dates(rows)
    print("Exercise 5: {}\n".format(unique_count))

    print("Exercise 6:")
    for month, price in sorted(month_avg_price(rows).items(),
                               key=lambda t: datetime.datetime.strptime(t[0], '%B').month):
        print("\t{}\t${:.2f}".format(month, price))
    print("")

    print("Extra Credit:")
    for start, end, miles in sorted(highest_thirty(rows)):
        print("\t{}\t{}\t{} miles".format(start.strftime("%Y-%m-%d"),
                                          end.strftime("%Y-%m-%d"), miles))
    print("")


#########################

if __name__ == '__main__':
    
    data_file_name = "mustard_data.csv" 
    main(data_file_name)




