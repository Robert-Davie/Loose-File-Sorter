<h1>Loose File Sorter</h1>
by Robert Davie
<br><br>
<h2>What is it?</h2>
The loose file sorter copies files from a given directory
into a SortedFile directory, grouping files into 
sub-directories by file extension.
<br>
<br>
<b>N.B. this program has not been fully tested so should be
used with some caution, however the program does not
delete files, it only copies them.</b>
<br>
<br>
<h2>How to use it?</h2>
<ol>
    <li>Download the repo</li>
    <li>Ensure the virtual environment is activated</li>
    <li>Call the program in the terminal<br>
        <code>python main.py directory</code>
        <br>where <code>directory</code> is the directory to be sorted e.g. <code>C:\\Users\\user\\MyFolder</code>
    </li>
    <li>The program will ask you to confirm your choice with <code>[y/n]</code>, to proceed enter <code>y</code></li>
    <li>The SortedFiles directory will be created in the same directory that the user given directory exists in</li>
</ol>
<br>
<br>
<h2> What version of python is required?</h2>
This project was created using python 3.12.<br>
No external libraries were used.
