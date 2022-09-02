import subprocess
import re

def run(verbose=0):
    cnbc_proc = subprocess.run(
        ["scrapy", "crawl", "cnbc_spider", "-o", "articles_temp.json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
        
    cnn_proc = subprocess.run(
        ["scrapy", "crawl", "cnn_spider", "-o", "articles_temp.json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Cleanup file so that it contains 1 instead of 2 lists
    with open('articles_temp.json', 'r', encoding="utf-8") as infile, open('articles.json', 'w', encoding="utf-8") as outfile:
        temp = re.sub("\n\]\[", ",", infile.read())
        outfile.write(temp)

    if verbose != 0:
        print(cnbc_proc.stdout, "\nEnd of CNBC spider.")
        if verbose == 2:
            print("Errors:\n")
            print(cnbc_proc.stderr)
        print(cnn_proc.stdout, "\nEnd of CNN spider.")
        if verbose == 2:
            print("Errors:\n")
            print(cnn_proc.stderr)