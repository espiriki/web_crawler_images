#!/usr/bin/env python
from dataset_builder import DatasetBuilder
from web_crawler import WebCrawler
import os
from os import listdir
import sys
import shutil

api_keys = {}

number_to_name = {1: "black", 2: "blue", 3: "green",
                  4: "take_to_recycle", 5: "blue/refundable"}

string_to_search = sys.argv[1]

# num_images = int(input("How many images to search for? 0 to skip\n"))
num_images = 199

if num_images == 0:
    print("Skipping!")
    sys.exit(0)

bin_colour = input("Which class is the object?\
    \n1 - black\
    \n2 - blue\
    \n3 - green\
    \n4 - take_to_recycle\
    \n5 - refundable\n")

keywords = [string_to_search]
images_nbr = num_images  # number of images to fetch
download_folder = "./data"  # folder in which the images will be stored

### Crawl and download images ###
crawler = WebCrawler(api_keys)

# 1. Crawl the web and collect URLs:
crawler.collect_links_from_web(
    keywords, images_nbr, remove_duplicated_links=True)

# 2. (alernative to the previous line) Load URLs from a file instead of the web:
#crawler.load_urls(download_folder + "/links.txt")
#crawler.load_urls_from_json(download_folder + "/links.json")

# 3. Save URLs to download them later (optional):
crawler.save_urls(download_folder + "/links.txt")
#crawler.save_urls_to_json(download_folder + "/links.json")

# 4. Download the images:
crawler.download_images(target_folder=download_folder)

### Build the dataset ###
dataset_builder = DatasetBuilder()

# 1. rename the downloaded images:
source_folder = download_folder
target_folder = download_folder + "_renamed"
dataset_builder.rename_files(source_folder, target_folder)


folder = "data"+os.sep+string_to_search+os.sep
for file_name in listdir(folder):

    if file_name.endswith('.jpeg') or \
       file_name.endswith('.jpg') or \
       file_name.endswith('.png'):
        continue
    else:
        os.remove(folder + file_name)


wait = input("Enter when done filtering images")


for file_name in listdir(folder):
    name = number_to_name[int(bin_colour)]
    dest_folder = "dataset"+os.sep+name+os.sep+string_to_search
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    shutil.copy(folder + file_name, dest_folder)
