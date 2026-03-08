# This tells make to always link cs50.c with whatever file you are making
%: %.c cs50.c
	gcc -g $@.c cs50.c -o $@