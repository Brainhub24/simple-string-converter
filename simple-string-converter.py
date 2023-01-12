import argparse
import base64
import binascii

def print_welcome():
    print("""
                 Welcome to the simple python converter

                 Here below you can see the encrypted string.
                 You can find more information with the flag "-h". :)


                 ----------------------------------------------------
                 Jason Prime (Github: @Brainhub24)
		 github@brainhub24.com
    """)

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Define the command line arguments
parser.add_argument("-d", "--decode_string", help="Decode the string passed as argument")
parser.add_argument("-e", "--encode_string", help="Encode the string passed as argument")

# Parse the command line arguments
args = parser.parse_args()

# Original String
original_string = "This is a simple script that converts strings to base64 and or hex also with specific flags like \"-d or -decode | -h or -help\""

print_welcome()

if args.encode_string:
    original_string = args.encode_string

# Encode the string to base64
base64_encoded = base64.b64encode(original_string.encode())

# Convert the base64 encoded string to a hex string
hex_encoded = binascii.hexlify(base64_encoded)

# Check if the --decode_string flag is set
if args.decode_string:
    # Decode the hex encoded string passed as argument to bytes
    decoded_bytes = binascii.unhexlify(args.decode_string.encode())
    # Decode the base64 encoded bytes back to the original string
    decoded_string = base64.b64decode(decoded_bytes).decode()
    print(decoded_string)
else:
    print(hex_encoded)
