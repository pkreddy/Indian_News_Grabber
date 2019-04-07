call activate base
F:
cd F:\GitHub\Indian_News_Grabber\inshorts
python "Update InShorts Links.py"
python Download_News.py
call conda deactivate