# Scrapy 2.11.2 - no active project
#
# Usage:
#   scrapy <command> [options] [args]
#
# Available commands:
#   bench         Run quick benchmark test
#   fetch         Fetch a URL using the Scrapy downloader
#   genspider     Generate new spider using pre-defined templates
#   runspider     Run a self-contained spider (without creating a project)
#   settings      Get settings values
#   shell         Interactive scraping console
#   startproject  Create new project
#   version       Print Scrapy version
#   view          Open URL in browser, as seen by Scrapy
#
#   [ more ]      More commands available when run from project directory
#
# Use "scrapy <command> -h" to see more info about a command
import os

ALL_CMDS = ['bench', 'fetch', 'genspider', 'runspider', 'settings',
            'shell', 'startproject', 'version', 'view']


def do_gen():
    for cmd in ALL_CMDS:
        p = f'{cmd}.txt'
        if os.path.exists(p):
            continue
        os.system(f'scrapy {cmd} -h > {p}')


if __name__ == '__main__':
    do_gen()
    pass
