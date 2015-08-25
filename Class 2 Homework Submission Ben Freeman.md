1. The header is the various data categories from Chipotle.
	Head chipotle.tsv
Each row represents the items that were purchased along with the price. Each order number is on the side too and some
include more items than other orders.
	Tail chipotle.tsv

2.There are 1834 orders. you can see it when you examine the tail of the file. 

3. 4623 lines
wc -l chipotle.tsv 

4. Chicken was more popular
Code:

grep -i -c "chicken" chipotle.tsv
1565

grep -i -c "steak" chipotle.tsv
706

5.Couldn't figure this one out.

6. Three 
Code:
find DAT8 -name *.*sv 

7. 
Code from within the DAT8 repo: 

grep -r "dictionary" .