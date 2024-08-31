ffuf  -X POST -u http://chal.pctf.competitivecyber.club:9096/check.php -H 'Content-Type: application/x-www-form-urlencoded' -d 'password=FUZZ' -w possibilities.txt -fr 'incorrect password'
