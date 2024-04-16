
# Create the main parser
parser = argparse.ArgumentParser(prog='mycli', description='My CLI Tool')

# Create subparsers for each program
subparsers = parser.add_subparsers(title='Available Programs', dest='program')

# Create a parser for the 'ls' program
ls_parser = subparsers.add_parser('ls', help='List files')
ls_parser.add_argument('-s', '--size', action='store_true', help='Display file sizes')
ls_parser.add_argument('-a', '--all', action='store_true', help='Display hidden files')

# Create a parser for the 'del' program
del_parser = subparsers.add_parser('del', help='Delete files')
del_parser.add_argument('filename', type=str, help='Name of the file to delete')

# Parse the command-line arguments
args = parser.parse_args()

# Perform actions based on the selected program and arguments
if args.program == 'ls':
    # Logic for 'ls' program
    if args.size:
        # Perform action for '-s' flag
        print("Displaying file sizes...")
    if args.all:
        # Perform action for '-a' flag
        print("Displaying hidden files...")
    # Perform other 'ls' actions

elif args.program == 'del':
    # Logic for 'del' program
    filename = args.filename
    # Perform 'del' action with the specified filename
    print("Deleting file:", filename)
    # Perform other 'del' actions

# Add logic for other programs and flags
# if __name__ == "__main__":
#     main()


