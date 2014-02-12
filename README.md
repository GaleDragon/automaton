Automaton  
=========

[Setting up the DB](#dbsettings)

[Adding Tests](#testadd)

[Adding to the Form](#formadd)

[Common Errors (local)](#localerror)

<a name="dbsettings"/>  
Setting up the DB  
=================
```  
brew install postgresql  
createuser -Pdr automaton  
```  
Enter the password "boomtown" at both prompts  
```
createdb -U automaton boomtown
```  
And the DB should be ready to rock.  

<a name="testadd"/>
Adding Tests
============

Where does the test go and what do I need?
------------------------------------------

Adding tests to automaton is easy. All you need to do is navigate to the automaton/tests/ directory and drop a .py test case in. Automaton only runs tests with the prefix wd, so be sure that your test matches this naming schema. Also make sure you also add a .txt file with the name and description you want displayed for the test on the results page. 

Ex. If the test case is named wdRegister.py, the .txt file should be named wdRegister.txt

The .txt should be formatted in 2 lines, with the first being the name and the second being the description.

1. Test Case Name
2. Test Case Description

What kind of modifications will my test case need?
--------------------------------------------------

In order to properly display the output in the results page, you will need to make a few modifications to the test case.

1. Make sure that all references to form field (url, email, etc.) are correctly referenced in the test case as defined in the config file, as this is how they will be referenced once the inject function runs.

2. If your test requires a name field, automaton will not handle this. We suggest using generated names. We have been using [treyhunner's name module](https://github.com/treyhunner/names) for our name field needs so far.

3. In the ```main``` method of your test case, you will need to define the test, and call the config inject function. Here is an example for the wdRegister test case.

```
if __name__ == "__main__":
    test = RegWD('test_reg_w_d') #this is the method that runs the test
    test.inject()
```

<a name="formadd"/>
Adding more information to the form
===================================

Adding more information to be pulled in will be a little bit more involved than adding a simple test case.

<a name="localerror"/>
Common local errors
===================

If you are running the project locally, in django's debug mode, you may run into a one of these. This section is meant for quick fixes to errors we encountered a lot. They may not represent the errors you actually encounter, or the cause of them, but it might be useful to start here if you encounter one that sounds similar.

No such file or directory
-------------------------

Most of these are caused by running manage.py from the wrong directory. To solve this, always run manage.py from the directory it is located in, even though you may be able to run it from sub directories, or parent directories.

Database conflicts
------------------

While testing we ran into this one a few times. The problem seems to be in django's syncdb method, which is called from manage.py. While it is supposed to be able to alter tables, it seems to only add new ones at the time of writing. You can solve this by manually dropping the tables you are having issues with, then running syncdb again. It will add the new updated tables back.

I/O Errors
----------

We found a few of these as well, which were caused generally caused by running manage.py from the wrong location. As before, make sure that you always run manage.py from the directory you have it stored locally in.

