Hello friends, this is my meme maker. How it works is that you run this on Google App Engine and it will give you a page where you enter your top text and bottom text using an html form. Then a random meme will be generated with your chosen top text and bottom text. The dropdown menu doesn't really do anything yet (as of July 25th) but it's intended to allow you to choose the meme too. I used templates.

main_wtemplate.py : where I have my code for getting the memes off of the imgflip api and for putting the templates in the right places and rendering them
home.html : code for where you start off on the main page with all the android bois and the place to enter your caption choices
meme_result.html : the page that gives the output meme
