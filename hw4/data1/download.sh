#!/bin/bash
FILE_NUMBER=$1

echo "##########################  Now downloading file # $FILE_NUMBER ##################";
wget http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-us-all-2gram-20090715-$FILE_NUMBER.csv.zip;
