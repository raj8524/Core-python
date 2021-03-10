# import platform
# def show_it():
#     message()
# def message():
#     print("this is python version {}".format(platform.python_version()))
# if __name__=='__main__':
#     show_it()

# def Madhuri_raj():
#     a,b=2,3
#     add=a+b
#     print(add)
# Madhuri_raj

# def isprime(n):
#     if n <= 1:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     else:
#         return True
# n=20
# if isprime(n):
#     print(f"{n} is prime")
# else:
#     print(f"{n} is not prime")

# x="seven '{1:<09}' '{0:>08}' ".format(8,9)
#
# print(" x is {}".format(x))
#
# ## none type,empty string, 0 remians false in boolean.###

# secret="swordfish"
# count=0
# auth=False
# max_count=5
# pw=''
# while pw!=secret:
#     count+=1
#     pw=input(f"{count} enter secret:")
#     if count >max_count:
#         break
#     print("come soon")
#
# else:
#     auth=True
#
# print("authorised" if auth else "calling FBI...")

#
# z=[67,89,45,33,56]
# for k in z:
#     if k==45:
#         continue
#     if k==56:
#         break
#     else:
#         print("dance")
#     print(k)
# else:
#
#     print("hghj")
#


import csv
import requests
import xml.etree.ElementTree as ET


def loadRSS():
    # url of rss feed
    url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'

    # creating HTTP response object from given url
    resp = requests.get(url)

    # saving the xml file
    with open('topnewsfeed.xml', 'wb') as f:
        f.write(resp.content)


def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # create empty list for news items
    newsitems = []

    # iterate news items
    for item in root.findall('./channel/item'):

        # empty news dictionary
        news = {}

        # iterate child elements of item
        for child in item:

            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')

                # append news dictionary to news items list
        newsitems.append(news)

        # return news items list
    return newsitems


def savetoCSV(newsitems, filename):
    # specifying the fields for csv file
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(newsitems)


def main():
    # load rss from web to update existing xml file
    loadRSS()

    # parse xml file
    newsitems = parseXML('topnewsfeed.xml')
    print(newsitems)

    # store news items in a csv file
    # savetoCSV(newsitems, 'topnews.csv')


if __name__ == "__main__":
    # calling main function
    main()




    
    



        



   























