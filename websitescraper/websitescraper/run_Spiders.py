import subprocess
import re

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
with open('articles_temp.json', 'r') as infile, open('articles.json', 'w', encoding="utf-8") as outfile:
    temp = re.sub("\n\]\[", ",", infile.read())
    outfile.write(temp)

# The function blocks until the shell command is completed.
#print(cnbc_proc.stdout, "\nEnd of CNBC spider.")
#print("Errors:\n")
#print(cnbc_proc.stderr)

#print(cnn_proc.stdout)
#print("Errors:\n")
#print(cnn_proc.stderr)
# No error for the shell command.