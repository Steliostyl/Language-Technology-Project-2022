import subprocess

#cnbc_proc = subprocess.run(
#    ["scrapy", "crawl", "cnbc_spider", "-o", "cnbc_spider.json"],
#    stdout=subprocess.PIPE,
#    stderr=subprocess.PIPE,
#    text=True
#)

cnn_proc = subprocess.run(
    ["scrapy", "crawl", "cnn_spider", "-o", "cnn_spider.json"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# The function blocks until the shell command is completed.
#print(cnbc_proc.stdout, "\nEnd of CNBC spider.")
print(cnn_proc.stdout)
print("Errors:\n")
print(cnn_proc.stderr)
# No error for the shell command.