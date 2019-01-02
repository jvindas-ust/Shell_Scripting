# Shell Scripting

-   [What is it?](#what-is-it)
-   [Bash scripting language pros and cons](bash-scripting-language-pros-and-cons)
-   [So what are the alternatives?](#so-what-are-the-alternatives)
-   [Our first python shell script](#our-first-python-shell-script)
-   [export and env command](#export-and-env-command)
-   [Python's OS Module](#pythons-os-module)
-   [A more complex example](#a-more-complex-example)

## What is it?

According to Wikipedia:

> A shell script is a computer program designed to be run by the [Unix shell](https://en.wikipedia.org/wiki/Unix_shell), a [command-line interpreter](https://en.wikipedia.org/wiki/Command-line_interpreter). The various dialects of shell scripts are considered to be [scripting languages](https://en.wikipedia.org/wiki/Scripting_language). Typical operations performed by shell scripts include file manipulation, program execution, and printing text.

So there are two main components of shell scripting, the Unix shell and a scripting language. We already know a Unix shell, to interact with Ubuntu we have been using the [Bash shell](<https://en.wikipedia.org/wiki/Bash_(Unix_shell)>) profusely with commands like ls, cd, cp, grep, more, awk, etc.

Now we need a scripting language, but what is that? According to Wikipedia:

> A scripting or script language is a programming language that supports scripts — programs written for a special [run-time environment](https://en.wikipedia.org/wiki/Run-time_environment) that automate the execution of tasks that could alternatively be executed one-by-one by a human operator.

> The term "scripting language" is also used loosely to refer to [dynamic](https://en.wikipedia.org/wiki/Dynamic_programming_language) [high-level](https://en.wikipedia.org/wiki/High-level_language) [general-purpose languages](https://en.wikipedia.org/wiki/General-purpose_programming_language), such as [Perl](https://en.wikipedia.org/wiki/Perl), [PowerShell](https://en.wikipedia.org/wiki/PowerShell), [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>), and [Tcl](https://en.wikipedia.org/wiki/Tcl) with the term "script" often used for small programs (up to a few thousand lines of code) in such languages, or in domain-specific languages such as the text-processing languages [sed](https://en.wikipedia.org/wiki/Sed) and [AWK](https://en.wikipedia.org/wiki/AWK).

We have had experience this need to encapsulate a series of commands in order to have a convenient way of repeatedly and consistently executing instructions. For that we wrote small bash scripts using a .sh file with #!/bin/bash on top and execute permissions.

```bash
#!/bin/bash
for jpg; do                                  # use $jpg in place of each filename given, in turn
    png="${jpg%.jpg}.png"                    # construct the PNG version of the filename by replacing .jpg with .png
    echo converting "$jpg" ...               # output status info to the user running the script
    if convert "$jpg" jpg.to.png ; then      # use the convert program (common in Linux) to create the PNG in a temp file
        mv jpg.to.png "$png"                 # if it worked, rename the temporary PNG image to the correct name
    else                                     # ...otherwise complain and exit from the script
        echo 'jpg2png: error: failed output saved in "jpg.to.png".' >&2
        exit 1
    fi                                       # the end of the "if" test construct
done                                         # the end of the "for" loop
echo all conversions successful              # tell the user the good news
exit 0
```

This is the [bash scripting language](https://en.wikibooks.org/wiki/Bash_Shell_Scripting). You might be thinking what is the difference between the bash language and the others mention in the definition, why don’t we just keep using the bash language?

## Bash scripting language pros and cons

Shell scripting is really good for simple “light” scripting, quicker to write, easy to handle input/output and pipes. But as your script grows in complexity and size, there are many problems that could appear:

-   Slow execution speed.
-   Design flaws within the language syntax or implementation to support old legacy systems, make the language verbose, error prone and hard to maintain.
-   Code reuse among scripts tends to be difficult, and scripts tend to be very specific to a certain problem.
-   It does not provide minimal data structures until Bash 4.
-   Libraries for advanced features, such as HTML parsing or HTTP requests, are not as easily available as they are with modern programming and scripting languages.
-   It is hard to debug and test.
-   It uses eval, you don't want to treat your data as executable code because is a major security issue.

It is possible and not so difficult to write safe Bash once you know the tricks, but it takes extra consideration and it is easy to forget or be lazy about it. Writing three or four lines of safe Bash is easy; two-hundred is quite a bit more challenging.

## So what are the alternatives?

There are many alternatives, one of the most traditional ones is a programing language called [Perl](https://en.wikipedia.org/wiki/Perl). Perl for beginners has some similar issues to Bash: it was a much smaller language when it was created, and a lot of the syntax for the newer features has a bolted-on feeling. There are two main versions [Perl 5](https://www.perl.org/) and [Perl 6](https://perl6.org/). Perl 6 solves much of the issues in Perl 5 but the community is divided between the two versions and Perl 6 adoption is slow at best and not without [shortcomings](https://www.evanmiller.org/a-review-of-perl-6.html).

However, if one knows Perl well and is comfortable with it, it's well suited to the task and is still a much saner choice for non-trivial automation scripts, and that is one of its strongest domains.

Another great alternative is python, we are already familiar with it and from all the scripting languages is the one that has had the most growth, being one of the most [strong](http://pypl.github.io/PYPL.html) and [popular](https://www.tiobe.com/tiobe-index/) programming languages. Other advantages of python as a scripting language are:

-   Is installed by default on all the major Linux distributions.
-   Easy to read and understand syntax. Its style emphasizes minimalism and clean code while allowing the developer to write in a bare-bones style that suits shell scripting.
-   Is an interpreted language, meaning there is no compile stage. Also comes with a Read Eval Print Loop [RELP](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop), this lets the developer tinker with ideas without having to write the full program out into a file.
-   Is a fully featured programming language. Code reuse is simple, because Python modules easily can be imported and used in any Python script. Scripts easily can be extended or built upon.
-   Has access to an excellent standard library and thousands of third-party libraries for all sorts of advanced utilities, such as parsers and request libraries. For instance, Python's standard library includes datetime libraries that allow you to parse dates into any format that you specify and compare it to other dates easily.
-   Can be a simple link in the chain. Python should not replace all the bash commands. It is as powerful to write Python programs that behave in a UNIX fashion (that is, read in standard input and write to standard output) as it is to write Python replacements for existing shell commands, such as cat and sort.

## Our first python shell script

The first thing we got to do is to find out the python we got installed in the Linux distribution, and where is the binary in the system.

```bash
python --version
python3 -V
which python3
```

Now we can create a executable file in a similar way we used to do with bash, using the [shebang](<https://en.wikipedia.org/wiki/Shebang_(Unix)>) and changing the permission.

```python
#!/usr/bin/env python3

print('hello, world!')
```

If you want you can name your script with a `.py` extension, some people don’t do this in order to make it less obvious the script is written in Python and to make it look as a regular shell command, your choice.

Also notice the use of `/usr/bin/env`, if you have several versions of Python installed, `/usr/bin/env` will ensure the interpreter used is the first one on your environment's [`$PATH`](<https://en.wikipedia.org/wiki/PATH_(variable)>). The alternative would be to hardcode something like `#!/usr/bin/python3`; that's ok, but less flexible. This takes us to our first bash review topic: [environment variables](https://en.wikipedia.org/wiki/Environment_variable).

## export and env command

An environment variable is a dynamic-named value that can affect the way running processes will behave on a computer. The `export` command is used to export a variable or function to the environment of all the child processes running in the current shell.

```bash
export BASH_VAR=example
echo $BASH_VAR

export -f functionname # exports a function in the current shell.
```

The `env` command lists all the environment variables. If you run `env` after the last `export`, you can see displayed the exported variable varname.

```bash
env
```

There are some variables that are automatically export in the [Bash Shell Startup Files](https://www.tldp.org/LDP/lfs/LFS-BOOK-6.1.1-HTML/chapter07/profile.html) that help create the environment for the current session. In linux there are [many of this files](https://medium.com/coding-blocks/getting-to-understand-linux-shell-s-start-up-scripts-and-the-environments-path-variable-fc672107b2d7), but in ubuntu the most common file is the `.bashrc`

```bash
nano ~/.bashrc
```

Inside you could also notice another command called `alias`. A [shell alias](https://shapeshed.com/unix-alias/) is a shortcut to reference a command. It can be used to avoid typing long commands or as a means to correct incorrect input. The use the`unalias` command to remove.

```bash
alias lh='ls -lhat'
```

If you want this changes to remain in your system, you need to add this line to your startup file, to reload a startup file in the current session the `source` command can be use; or its `.` alias. For example add this alias and reload the file:

```bash
alias update='sudo apt update && sudo apt upgrade'
```

The `set` and `unset` commands can also be used to declare and un-declare variables, the difference with the export command is that they declare variables in the current shell. The export command is used to define the variable as one that subshells (shells spawned from the original) should inherit, [read more](http://hackjutsu.com/2016/08/04/Difference%20between%20set,%20export%20and%20env%20in%20bash/). But how do we manipulate environment variables inside a Python script?

## Python's OS Module

One of the great features of python is that it comes with a very extensive set of functionality built-in, this is call the [Standar Library](https://docs.python.org/3/library/), and provides access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers; as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming.

Inside the Standard Library there is a module call Operating System Interface or [os](https://docs.python.org/3/library/os.html#module-os) that provides dozens of functions for interacting with the operating system.

To use this module in our script we need a new keyword `import` that instructs the Python interpreter to _bring in_ the code we need to the current file or session. The specific fuctionality that we are looking for inside the module is access with a `.` notation, for our example is [`os.environ`](https://docs.python.org/3/library/os.html#os.environ)

```python
import os

print(os.environ['HOME'])
```

## A more complex example

For our more complex example we will try to count the unique names inside a system log file. In order to do that we need to [open a file and read it line by line](https://stackabuse.com/read-a-file-line-by-line-in-python/), in python that is pretty easy:

```python
with open('days.txt') as file:
    for line in file:
        # Do something with the line
```

Notice that we are hard coding the file path, it would be great to pipe the file to our script like we did with other shell commands, for example `| more`. For this we will use another python module from the standar library called [`sys`](https://docs.python.org/3/library/sys.html) which has a function call [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin) to read the [standard input stream](https://en.wikipedia.org/wiki/Standard_streams)

```python
import sys

for line in sys.stdin.readlines():
	for line in file:
		# Do something with the line
```

Now we can pipe a file into our script like this:

```bash
cat days.txt | ./04_read_stdin.py
```

In Ubuntu there is an [Authorization Log](https://help.ubuntu.com/community/LinuxLogFiles#Authorization_Log) that tracks the usage of authorization systems, the mechanisms for authorizing users which prompt for user passwords, like when you execute a sudo command. This file is located here `/var/log/auth.log`.

In order to analyze this file, let's say we want to view the _usernames that fail an authentication_, first inspect the file:

```bash
cat /var/log/auth.log | more
grep -a "failure" /var/log/auth.log
```

Now you could use one of the tools we learned like `awk`:

```bash
awk '/authentication failure/ {print $4}' /var/log/auth.log | uniq
```

But what if you want to count the amount of failed logins per user, you could do something like:

```bash
awk '/authentication failure/ {print $4}' /var/log/auth.log | wc -l
```

Now pretend that your server has hundreds of users and your boss asks you for a python dictionary in the form:

```python
{
	username: count
}
```

Modify the script `05_count_users.py` to do this functionality. If you feel confident and want to go the extra mile save the results as a .json file that could be later consume by a web service API.
