#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hoh
#
# Created:     05/05/2011
# Copyright:   (c) hoh 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
input_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
output_string = []
notranslateset=[" ",".","'","(",")"]
def main():
    for idx,c in enumerate(input_string):
        if c not in notranslateset:
             if int(ord(c)) + 2>int(ord('z')):
                output_string.append(chr(int(ord(c)) - int(ord('z')) + int(ord('a')) + 1))
             else:
                output_string.append(chr((int(ord(c))+2)))
        else:
             output_string.append(c)


    print "".join(output_string)


if __name__ == '__main__':
    main()
