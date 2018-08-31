#!/usr/bin/python
# -*- coding: utf-8 -*-
#Developed by Tiago Neves
#Github: https://github.com/TiagoANeves
#Version: 1.0
#All rights reserved

#Import necessary modules
import socket
import sys
import os
from argparse import ArgumentParser

os.system("clear")

#Color scheme
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Create Banner
def banner():
    print("""%s
     _______ _____ _______        _         _                       _       ______ _   _ _____  
    |__   __|  __ \__   __|      | |       | |                     (_)     |  ____| \ | |  __ \ 
       | |  | |  | | | |___ _   _| |__   __| | ___  _ __ ___   __ _ _ _ __ | |__  |  \| | |  | |
       | |  | |  | | | / __| | | | '_ \ / _` |/ _ \| '_ ` _ \ / _` | | '_ \|  __| | . ` | |  | |
       | |  | |__| | | \__ \ |_| | |_) | (_| | (_) | | | | | | (_| | | | | | |    | |\  | |__| |
       |_|  |_____/  |_|___/\__,_|_.__/ \__,_|\___/|_| |_| |_|\__,_|_|_| |_|_|    |_| \_|_____/%s%s

    # Coded By Tiago Neves
    # Github https://github.com/TiagoANeves
    """ % (bcolors.OKBLUE, bcolors.ENDC, bcolors.FAIL))

# Arguments Parser
parser = ArgumentParser()
parser.add_argument("-d", "--domain", help="domain name")
parser.add_argument("-w", "--wordlist", default="subdomains.txt", help="wordist file %s" %bcolors.ENDC)

# Count wordlist subdomains
def countlines(textfile):
	num_lines = len(open(textfile).readlines(  ))
	return num_lines


# Main function
if __name__ == "__main__":
    try:
        banner()
        print "This program will check for subdomains based on a wordlist."
        print "If wordlist not especified, it will use the subdomains.txt by default."
        print bcolors.ENDC
        args = parser.parse_args()
    except:
        sys.exit(0)
    if len(sys.argv) < 3:
        print bcolors.WARNING + "Usage: python "+sys.argv[0]+" -d domain.com -w subdomains.txt\n" + bcolors.ENDC
        print bcolors.WARNING + "Use "+sys.argv[0]+" -h or --help to print the help option\n" + bcolors.ENDC
        sys.exit()
    else:
        print bcolors.HEADER + "Starting the program...\n" + bcolors.ENDC
	numlines = countlines(args.wordlist)
	print bcolors.HEADER + "The file %s%s%s has %s%s%s words" %(bcolors.OKGREEN,args.wordlist,bcolors.HEADER,bcolors.OKGREEN,numlines,bcolors.HEADER) + bcolors.ENDC	
        domain = args.domain
        try:
	    IP = socket.gethostbyname(domain)
	    print bcolors.HEADER + "The domain %s%s%s has the IP address %s%s%s\n" %(bcolors.OKGREEN,domain,bcolors.HEADER,bcolors.OKGREEN,IP,bcolors.HEADER) + bcolors.ENDC	
        except:
            print "Error to get the IP address from the given domain"
            sys.exit()
        try:
            filewordlist = open(args.wordlist,'r')
        except:
            print "Error trying to open wordlist file"
            sys.exit()
        subdomains = filewordlist.read().split('\n')
	subdomaincount = 0
	subdomainfound = 0
	try:
	    for subdomain in subdomains:
	    	print bcolors.WARNING + "Trying %s%s%s of %s%s%s subdomains" %(bcolors.OKGREEN,subdomaincount,bcolors.WARNING,bcolors.OKGREEN,numlines,bcolors.WARNING) + bcolors.ENDC
	    	try:
		    IP = socket.gethostbyname(subdomain+'.'+domain)
		    sys.stdout.write("\033[F") #Back to previous line
                    sys.stdout.write("\033[k") #Clear line
                    print "%s%s%sSubdomain found:%s %s%s.%s (%s)%s" %(bcolors.OKBLUE,bcolors.BOLD,bcolors.UNDERLINE,bcolors.ENDC,bcolors.OKGREEN,subdomain,domain,IP,bcolors.ENDC)
                    subdomainfound += 1
	    	except:
		    sys.stdout.write("\033[F") #Back to previous line
                    sys.stdout.write("\033[k") #Clear line
	    	subdomaincount += 1
	except KeyboardInterrupt:
	    print bcolors.FAIL + "Bruteforcing interrupted by the user..." + bcolors.ENDC
	
	if (subdomainfound == 0):
            print bcolors.FAIL + "\nCould not find any subdomain from "+ domain + bcolors.ENDC
	else:
	    print bcolors.FAIL + "\n\nWas found %s%s%s subdomains from %s%s%s\n" %(bcolors.OKGREEN,subdomainfound,bcolors.FAIL,bcolors.OKGREEN,domain,bcolors.ENDC)
