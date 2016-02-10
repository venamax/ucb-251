#!/bin/bash
for i in {0..33};
do
    wget http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-us-all-2gram-20090715-$i.csv.zip;
    echo file $i downloaded;
done
