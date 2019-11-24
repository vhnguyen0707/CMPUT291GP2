import re
import sys

data = open(sys.argv[1],"r")
emails = open("emails.txt", "w")
recs = open("recs.txt", "w")

def main():
    global data, emails, recs
    for line in data:
        if re.match('<mail>.*</mail>',line):
            row = re.search('<row>(.*)</row>',line).group(1)
            #get from, to cc, bcc
            fro = re.search('<from>(.*)</from>',line).group(1).lower()
            to = re.search('<to>(.*)</to>',line).group(1).lower()
            cc = re.search('<cc>(.*)</cc>',line).group(1).lower()
            bcc = re.search('<bcc>(.*)</bcc>',line).group(1).lower()
            #outputs to emails.txt
            processEmails(row, fro, to, cc, bcc)
            #outputs to recs.txt
            processRecs(row,line)
    emails.close()
    recs.close()

def processEmails(row, fro, to, cc, bcc):
    if fro:
        emails.write("from-" +fro+ ":" +row+ "\n")
    if to:
        emails.write("to-"+to+ ":"+row+"\n")
    if cc:
        emails.write("cc-"+cc+":"+row+"\n")
    if bcc:
        emails.write("bcc-"+bcc+":"+row+"\n")
        
def processRecs(row,line):
    #writes the lines in xml to recs.txt in the desired format
    
    if line:
        recs.write(row + ':' + line)
    
    
if __name__ == "__main__":
    main()
