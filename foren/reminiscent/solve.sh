

# NOTE: i deleted the flounder-pc-memdump.elf because it was over 500Mb


mkdir -p dump
# list files and get address of the resume.pdf.lnk
addr=$(vol.py --profile=Win7SP1x64 filescan -f flounder-pc-memdump.elf | grep resume | tail -n1 | awk '{print$1}')
# dump file 
vol.py --profile=Win7SP1x64 dumpfiles -f flounder-pc-memdump.elf --dump-dir dump/ --physoffset=$addr

# it's a link to a powershell script and from here we can extract the contents
echo -e 'Extracting flag from obfuscated powershell script\n'
strings -n100 dump/file.None.*.dat | base64 -d | sed 's/\x00//g' | awk '{print$NF}' | base64 -d | sed 's/\x00//g' | grep 'HTB{[^}]\+}' -o

# cleanup
rm -r dump

