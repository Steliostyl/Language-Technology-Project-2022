import subprocess

cnbc_proc = subprocess.run(
    ["scrapy", "crawl", "cnbc_spider", "-o", "cnbc_spider.json"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# bbc_proc = subprocess.run(
#    ["scrapy", "crawl", "bbc_spider", "-o", "/crawler_files/bbc_spider.json"],
#    stdout=subprocess.PIPE,
#    stderr=subprocess.PIPE,
#    text=True
#)

# The function blocks until the shell command is completed.
print(cnbc_proc.stdout)
print("Errors:\n")
print(cnbc_proc.stderr)
# No error for the shell command.