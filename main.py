from springer import *

import argparse

parser = argparse.ArgumentParser(description = "Download pdfs from the Springer archive")

parser.add_argument('-filename', type = str, default = 'v4.csv', help = "CSV file with the names of the books")
parser.add_argument('-foldername', type = str, default = 'download', help = "Folder into which to download the books")
parser.add_argument('-epub', action = 'store_true', default = False, help = "Download epub as well")




dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

args = parser.parse_args()

if __name__ == "__main__":

	print(args)
	folder_to_download = os.getcwd() + f"/{args.foldername}/"
	if not os.path.exists(folder_to_download):
		os.mkdir(folder_to_download)
	download(args.filename, folder_to_download, args.epub)

