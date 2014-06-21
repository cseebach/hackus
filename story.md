You're the new guy on the block at PragmaSec, a computer security firm. You've been assigned a crummy duty: get anything
important off of some ancient computers that have just been found in a warehouse that belongs to the company.

Thing about these machines - they're running an operating system that the firm developed on it's own, and the previous
programmers can't be found. So it's up to you to read the documentation and sift through the data.

This basically presents itself as a bunch of hacking and computer use challenges.

Challenge 1) Login to the machine.

You have to guess the right username and password. This is simple: it's 'admin' and 'password'.

Reward: 
    You get the first few commands that you can use.
        chdr - change current directory
        list - list all the files and directories in a directory
        move - move a file from one place to another
        copy - copy a file from one place to another
        edit - read and edit text files
        help - list all the commands, plus help on a specific topic
        logout - logs you out so you can switch users
        
Challenge 2) Gain super-user privileges

Hook: You find the home directory, and find a few different accounts within it. One of them is labeled djabir, the
previous user of this pc. But, you can't change into his directory to check it out because you don't have super-user
privileges.

You have to read a help topic called "users" to figure out where the list of super-users is kept. You have to modify
that list so it includes "admin", and then log out and log back in.