<h1 align="center">TerminalToDo</h1>
<p align="center"><b>Stay organized in your command line!</b></p>

<h3>Requirements</h3>
<ul>
  <li>At it's infancy, this this CLI only works on mac and linux. A windows verion is in developement. </li>
  <li>On mac, it works only on the bash shell. To enter the bash shell, run <code>bash</code>. Compatibility with other shells will arive in the future.</li>
  <li>Python3 must be installed.</li>
</ul>

<h3>Installation & Setup</h3>
In your home directory, clone this repo.

    cd ~
    git clone https://github.com/gadhagod/TerminalToDo/
Edit or create your .bashrc file.

    nano ~/.bashrc
Append the following to the file:
    
    alias ttd='python3 ~/TerminalToDo/ttd'
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
<h3>Commands</h3>
<code>ttd add</code> creates a to-do with one parameter. The argument passed will be the name of your to-do.<br>
<code>ttd rm</code> completes a to-do with one parameter. The argument passed is the to-do to be removed.<br>
<code>ttd cls</code> completes all to-dos.<br>
<code>ttd view</code> displays all your to-dos.
<br><br><p align="center">
  <a href="http://gadhagod.repl.co/"><img src="images/logo.png" legnth=40% width=40%></a>
</p>
