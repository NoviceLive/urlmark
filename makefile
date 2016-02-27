default:
	(cd gh-pages && ../urlmark.py)


install:
	mkdir -p ~/bin/lnk
	ln -srf ./urlmark.py ~/bin/lnk/urlmark
	printf '\n\n%s\n' "Add ~/bin/lnk to your path."
