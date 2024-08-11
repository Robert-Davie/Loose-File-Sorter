<h1>Loose File Sorter</h1>
by Robert Davie

<h2>What is it?</h2>
The loose file sorter copies files from a given directory
into a SortedFile directory, grouping files into 
sub-directories by file extension.

<br>
<b>N.B. this program has not been fully tested so should be
used with some caution, however the program does not
delete files, it only copies them.</b>

<h2>How to use it?</h2>
1. Download the repo
2. Ensure the virtual environment is activated
3. Call the program in the terminal<br>
`python main.py <location of folder to be sorted>`
<br> the location of the directory is an argument to be 
given to the program
4. The program will ask you to confirm your choice with
`[y/n]`, to proceed enter `y`
5. The SortedFiles directory will be created in the same
directory that the given directory exists in


<h2> What version of python is required?</h2>
This project was created using python 3.12<br>
No external libraries were used.