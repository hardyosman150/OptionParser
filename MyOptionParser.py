from optparse import OptionParser
import subprocess

parser = OptionParser()
parser.add_option("-f",
                  "--file",
                  dest="filename",
                  help="write report to FILE",
                  metavar="FILE")
parser.add_option("-q",
                  "--quiet",
                  action="store_false",
                  dest="verbose",
                  default=True,
                  help="don't print status messages to stdout")

parser.add_option(
    "-d",
    subprocess.call("dir", shell=True),
    action="store_false",
    dest="verbose",
    default=True,
    help="Enter for show all file")  ##msg system what is say when call help

(options, args) = parser.parse_args()
