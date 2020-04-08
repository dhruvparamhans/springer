# Download books from Springer website 

Automate pulling Springer's free books.

Slight modificaton of code found on Reddit:

https://www.reddit.com/r/learnmachinelearning/comments/fvncjm/springer_is_giving_free_access_to_409_of_its/?sort=new

Added the option of downloading the epubs. 

To download all the books run:

```python
python3 main.py -filename=<name of csv file> -foldername=<name of folder to download files to> 
```

For instance if you want to download files from v4.csv into the folder springer books, do the following:

```python
python3 main.py -filename=v4.csv -foldername=springer_books 
```

If you want to download the epub versions as well, do the following

```python
python3 main.py -filename=v4.csv -foldername=springer_books -epub
```