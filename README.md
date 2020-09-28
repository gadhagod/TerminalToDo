<h1 align="center">TerminalToDo</h1>
<p align="center"><b>Stay organized in your command line!</b></p>
<h3><a href="https://terminaltodo.gadhagod.repl.co/quickstart.html">Docs</a>

<h3>Requirements</h3>
<ul>
  <li>At it's infancy, this this CLI only works on mac and linux. A windows verion is in developement. </li>
  <li>On mac, it works only on the bash shell. To enter the bash shell, run <code>bash</code>. Compatibility with other shells will arive in the future.</li>
  <li>Python3 must be installed.</li>
</ul>

<h3>Installation & Setup</h3>
<h5>Installation</h5>
In your home directory, clone this repo.

    cd ~
    git clone https://github.com/gadhagod/TerminalToDo/
Edit or create your .bashrc file.

    nano ~/.bashrc
Append the following to the file:
    
    alias ttd='python3 ~/TerminalToDo/ttd'
After you're done writing into that file, save it, and run this in the terminal:
```
source ~/.bashrc
```
Now run <code>ttd</code> in your terminal. You should see a help message.<br>
```
Usage: ttd [OPTIONS] COMMAND [ARGS]...

  A command line interface for you to stay organized in your terminal.

Options:
  --help  Show this message and exit.

Commands:
  add   Create a to-do
  cls   Finish all to-dos
  rm    Finish a to-do
  view  View your to-dos
```
<h5>DISCLAIMER</h5>
This is doesn't make the command permanent and, when you close your terminal, the command <code>ttd</code> will not work anymore.
To solve this problem, you can instead write into the bash_profile.
For example, instead of running this:
```
nano ~/.bashrc
```
in your command line, you can run this:
```
nano ~/.bash_profile
```
The file may already have text written in it, but ignore it as it isn't important.
At the end (or beginning of the file, write:
```
alias ttd='python3 ~/TerminalToDo/ttd'
```
Now, save and exit the file and run this in your terminal:
```
source ~/.bash_profile
```
If you did this correctly, the <code>ttd</code> command should work even after you close terminal.
<h3>Commands</h3>
<code>ttd add</code> creates a to-do with one parameter. The argument passed will be the name of your to-do.<br>
<code>ttd rm</code> completes a to-do with one parameter. The argument passed is the to-do to be removed.<br>
<code>ttd cls</code> completes all to-dos.<br>
<code>ttd view</code> displays all your to-dos.
<br><br><p align="center">
  <a href="http://gadhagod.repl.co/"><img src="images/logo.png" legnth=40% width=40%></a>
</p>
<h3>Uninstallation</h3>
If, in any case, you want to "uninstall" this command, you can go into <code>~/.bashrc</code> or <code>~/.bash_profile</code> (Depending on which one you wrote to) and delete the line where it makes the alias for the <code>ttd</code> command.
Go into the file in which you made the alias for the <code>ttd</code> command:
```
nano ~/.bashrc
```
**OR**
```
nano ~/.bash_profile
```
Now delete the line where it make the alias for the <code>ttd</code> command.
The line of code you should delete:
```
alias ttd='python3 ~/TerminalToDo/ttd'
```
Now, save and exit the file and source it.
How to source the file:
```
source ~/.bashrc
```
**OR**
```
source ~/bash_profile
```
