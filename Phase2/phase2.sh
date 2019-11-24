#sorts the .txt file, uses break.pl to break, and build .idx
sort -u emails.txt | perl break.pl |db_load  -c duplicates=1 -T -t btree ./outputs/em.idx