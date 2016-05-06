#!/usr/bin/env python

import web_crawler

keyword = "cats"
my_key = "111111111111"
my_search_engine_id = "11111111111"
images_nbr = 5 # number of images to get

# create the instance and fetch for images URLs in the web:
api_keys = [('google', my_key, my_search_engine_id)]
crawler = web_crawler.WebCrawler(api_keys)
crawler.fetch_links(keyword, images_nbr, remove_duplicated_links=True)

# Replace the previous line by the following one if you want to load URLs from a file instead of crawling the web:
# urls_file_path = "./" + keyword + "/links.txt"
# crawler.load_urls(urls_file_path)

# save URLs in a file to download them later (optional):
urls_file_path = "./" + keyword + "/links.txt"
crawler.save_urls(urls_file_path)

# Download the images
images_folder_path = "./" + keyword
crawler.download_images(target_folder=images_folder_path)

# Rename downloaded files
import dataset_builder
dataset_builder = dataset_builder.DatasetBuilder()
dataset_builder.rename_files(images_folder_path, target_folder=images_folder_path + "_renamed")
# dataset_builder.rename_files(images_folder_path, target_folder=images_folder_path + "_renamed", extensions=('.jpg', '.png', '.gif'))
