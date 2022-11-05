# Copyright 2022 Zlac-org

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


try:
    # Importing all modules
    import advance
    import webbrowser
    import math
    import os
    from halo import Halo                                      
    from operator import pow, truediv, mul, add, sub
    import rich
    from rich.table import Table
    from rich import box
    from rich.prompt import Prompt
    from datetime import datetime
    from rich.console import Console, Group
    from rich.markdown import Markdown
    import sys
    from rich.align import Align
    from rich.panel import Panel
    from rich.live import Live
    from rich.layout import Layout
    import time
    from art import *

except ImportError:
    print('\n[ERROR] Failed importing modules. Make sure the venv is activated or try running ''pip install -r recquirements.txt''')    
    # If any dependency is missing or venv not activated

__app_name__ = 'Zlac'
__version__ = '2022.11.05'

console = Console() 
cws = os.name # Getting current working operating sys
doc_dir = os.path.normpath(os.getcwd() + os.sep + os.pardir)+"\docs"  # Getting the docs dir

def readmex():    
    # Usage part 1 
    markdownx ="""
# Zlac - Terminal claculator 

> Usage

**[replace `<a>`,`<b>`,`<h>`,`<l>`,`<w>` and `<r>` with numbers]**

Enter `?` for more info

## Simple mode
Enter any mathematical expression or exit(e) / clear(cl) / help(h) / oh(open_history)

Other operations :

■ Greater than : >

■ Less than : < 

■ Greater than or equal to : >= 

■ Less than or equal to : <=


## Advanced mode

### Area 

■ Area of rectangle : `<a>ar.rect<b>`

■ Area of square : `<a>ar.sq`
    """
    mdx = Markdown(markdownx)
    return Panel(mdx, style='yellow',expand=True,title='usage')

def readmey():  
    # Usage part 2
    markdowny = """
■ Area of Triangle [when height and base are given] : `<h>ar.tri<b>`

■ Area of circle : `<r>ar.cir`

### Perimeter

■ Perimeter of a rectangle : `<l>per.rect<w>`

■ Perimeter of square : `<a>per.sq`  

■ Circumference of circle : `<r>cic.cir`

### Log

■ Logarithm [value of log <a> to the base <b>]: `<a>log<b>`

■ Natural Logarithm : `ln<a>`

### Percentage 

■ <part>%<whole>

### Factorial 

■ <x>!

### Operations using pi (π)

■ pi (or π) add (or +) <a>         ■ pi (or π) div (or /) <a>

■ pi (or π) mul ( or *) <a>        ■ pi (or π) sub (or -) <a>

    
    """
    mdy = Markdown(markdowny)
    return Panel(mdy, style='cyan',expand=True,title='usage')      

def license():   
    """ Display the license in short """
    li = "Copyright 2022 Zlac-org\nSPDX-License-Identifier: Apache-2.0"
    return Panel(li,title='License')   # Displayed on footer


def help():        
    """ Help guide for all operations available for Zlac"""
     
    opt = Table.grid(expand=True)
    opt.add_column('Operation',style='cyan',justify='right')
    opt.add_column('Symbol',justify='left')
    opt.add_row('Simple mode','')
    opt.add_row('','')
    opt.add_row('Addition',' + ')
    opt.add_row('Subtraction',' - ')
    opt.add_row('Multiplication',' * ')
    opt.add_row('Division',' /')
    opt.add_row('Modulo',' % ')
    opt.add_row('Greater than',' > ')
    opt.add_row('Less than',' < ')
    opt.add_row('Greater than or equal to',' >= ')
    opt.add_row('Less than or equal to',' <= ')
    opt.add_row('Greatest integer function (Floor division) ',' // ')
    opt.add_row('','')
    opt.add_row('Advanced mode','')
    opt.add_row('','')
    opt.add_row('Area of rectangle',' ar.rect ')
    opt.add_row('Area of square',' ar.sq ')
    opt.add_row('Area of Triangle',' ar.tri ')
    opt.add_row('Area of circle',' ar.cir ')
    opt.add_row('Perimeter of a rectangle',' per.rect ')
    opt.add_row('Perimeter of square',' per.sq ')
    opt.add_row('Circumference of circle',' cic.cir ')
    opt.add_row('Operations using pi / π',' pi / π (add/sub/mul/div) ')
    opt.add_row('Logarithm',' log ')
    opt.add_row('Natural Logarithm',' ln ')
    opt.add_row('Square root',' √ ')
    opt.add_row('Factorial',' ! ')
    opt.add_row('Percentage',' % ')
    
    opt_panel = Panel(
        Align.center(
            Group("\n", Align.center(opt)),
            vertical="middle",
        ),
        box=box.ROUNDED,
        title="Zlac operations",
        border_style="green",
    )
    return opt_panel # Displayed on left side


def cmds():
    """ Special commands """
    keys = 'Enter exit(e) to quit\nEnter clean(cl) to clear all input'
    return Panel(keys,title='Commands') # Displayed on footer

def head():
    """ Header of the layout """
    head_view = Table.grid(expand=True)   
    head_view.add_column(justify='center')
    head_view.add_column(justify='right') 
    head_view.add_row('\t\t[bright_yellow][b]Zlac[/b] - Terminal Calculator')
    return Panel(head_view, style="white")

def lazy(str,delay): # types any str slowly. Speed can be changed using the delay ->float 
    """ Prints text slowly """
    for letter in str + '\n':
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)    

def app_info():
    """ App name with art module along with version """
    apin = text2art('                            '+__app_name__,font='fancy42') +' '+str(__version__)
    return Panel(apin, style="white") # Displayed on the header 

def exit_out():
    """ Quit the application along with a spinner """
    text = 'Exiting...'
    spinner = Halo(text=text, spinner='dots')
    spinner.start()
    time.sleep(1)
    spinner.stop()      # When exiting [1 second delay]


    
# Defining layout
def make_layout():
    """ Making the layout """
    layout = Layout(name="root")

    layout.split(
        Layout(name="header",size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer",size=4),
    )
    layout["main"].split_row(
        Layout(name="side"),
        Layout(name="body", ratio=2, minimum_size=60),
    )
    layout["header"].split_row(Layout(name="title"),Layout(name="art"))
    layout["body"].split_row(Layout(name="doc1"),Layout(name="doc2"))
    layout["footer"].split_row(Layout(name="cds"),Layout(name="li"))

    return layout 

# Updating all layouts
def update_layout():
    """ Updating all layouts """
    layout = make_layout()
    layout["title"].update(head())
    layout["art"].update(app_info())
    layout["cds"].update(cmds())
    layout["side"].update(help())
    layout["doc1"].update(readmex())
    layout["doc2"].update(readmey())
    layout["li"].update(license())
    console.print(layout)

def clear():
    """ Clearing all things and displaying the layout """
    if(cws == 'posix'):
        os.system('clear') # If unix or linux
    else:
        os.system('cls') # If windows

    update_layout()    

def exit_handler():
    """ Handle ctrl+c """
    print('\n')
    user_text = "# Exit Zlac ?? ( y / n ) [ n ]"
    user_text_md = Markdown(user_text)
    console.print(user_text_md,style="bright_yellow")
    user_resp = input(" > ") or "n"
    
    if user_resp.lower() == "y":
        time.sleep(1)
        exit_out()
        sys.exit()
    elif user_resp.lower() == "n":
        print('User choice > '+user_resp+' . ....')
        if(cws == 'posix'):
            os.system('clear') # If unix or linux
        else:
            os.system('cls') # If windows

        try:

            zlac()
        except KeyboardInterrupt:
            exit_handler()

    else:
        if(cws == 'posix'):
            os.system('clear') # If unix or linux
        else:
            os.system('cls') # If windows

        try:

            zlac()
        except KeyboardInterrupt:
            exit_handler()
    
def zlac():
    """ Main function of Zlac """
    update_layout() # Displaying the layout
    adv = "Zlac advanced mode - For advanced calculations"
    sim = "Zlac simple mode - For simple mathematical calculations"
    doc = """

## Enter `>` to enter advanced mode . To come back enter `<`

### Examples:

```

> 2*5
10

> 5*34/(3*6)   
9.444444444444445

> 5*(5/6)
4.166666666666667

> 5**5
3125

> 4*-4/3
-5.333333333333333

> -4.3/3
-1.4333333333333333

> 4%345//9/3+12-3
9.0

> 45<4
False

> 3<4>3
True

> 6<=4 
False
```
    """

    xdoc = """

## Enter `<` to return to simple mode   
 
### Examples:

```
>> 24ar.rect3
72.0

>> 4ar.sq
16.0

>> 3ar.tri4
6.0

>> ln3
1.0986122886681098

>> 2log10
0.30102999566398114

>> pi add 3 (or π + 3)
6.141592653589793

>> pi add (or π add)
3.141592653589793

>> 5%
0.05

>> 5%6
83.33333333333333

>> 7!
5040
```
    """

    zl = ''
    while zl != 'e':
        zl = input(' > ')
        if zl.lower() == 'exit' or zl.lower() == 'e':
            exit_out()
            break
        elif zl.lower() == 'cl' or zl.lower() == 'clear':
            clear()
        elif zl.lower() == '?' or zl.lower() == 'help' or zl.lower() == 'h' :
            ud = Markdown(doc)
            console.print(Panel(ud, style='cyan',expand=True,title='?'))   
        elif zl.lower() == 'h...' or zl.lower() == 'history...':
            try:

                with open("history.txt", encoding="utf-8") as f:
                    print(f.read()) # Display the history.txt file in terminal 
            except FileNotFoundError:
                print("'history.txt' file is missing or has not been created yet.This error may be raised if you have not done any calculations yet. Read documentation for details about the file. ")
        elif zl.lower() == 'advanced' or zl.lower() == 'a' or zl.lower() == '>':
            console.print(Panel(adv, expand=True,title='Mode'))
            za = ''
            while za != 'b':
                za = input(' >> ')
                if za.lower() == '<' or za.lower() == 'back' or za.lower() == 'b':
                    console.print(Panel(sim,expand=True,title='Mode'))
                    break
                elif za.lower() == 'exit' or za.lower() == 'e':
                    exit_out()
                    sys.exit()
                elif za.lower() == '?' or za.lower() == 'help' or za.lower() == 'h' :
                    xud = Markdown(xdoc)
                    console.print(Panel(xud, style='green4',expand=True,title='?'))
                elif za.lower() == 'h...' or za.lower() == 'history...':
                    try:

                        with open("history.txt", encoding="utf-8") as f:
                            print(f.read()) # Display the history.txt file in terminal 
                    except FileNotFoundError:
                        print("'history.txt' file is missing or has not been created yet.This error may be raised if you have not done any calculations yet. Read documentation for details about the file. ")
                elif za.lower() == 'cl' or za.lower() == 'clear':
                    clear()
                else:
                    # All operations in a single dictionary
                    ops = {
                    'log' : advance.log,
                    'ln' : advance.ln,    
                    '√' : advance.sqr,
                    '%' : advance.perc,
                    '!' : advance.facto,
                    'pi mul ': advance.pim,
                    'pi add ': advance.pia,
                    'pi sub ': advance.pis,
                    'pi div ': advance.pid,
                    'π * ': advance.pim,
                    'π + ': advance.pia,
                    'π - ': advance.pis,
                    'π / ': advance.pid,
                    'ar.rect' : advance.area_rectangle,
                    'ar.sq' : advance.area_sq,
                    'ar.tri': advance.area_tri,
                    'per.rect': advance.per_rectangle,
                    'per.sq': advance.per_sq,
                    'ar.cir': advance.area_circle,
                    'cic.cir': advance.per_circle,
                    }
                    def calculate(s): # Calculating input
                        if s.isdigit():
                            return float(s)  
                        for c in ops.keys():
                                left, op, right = s.partition(c) # splitting into 3 parts
                                if op in ops:
                                    return ops[op](calculate(left), calculate(right)) # Calculating seperately

                    try:
                        print(str(calculate(za))) # Printing the result as string
                        # Get current time
                        now = datetime.now().strftime("%H:%M:%S")
                        # Appending info to file > history.txt
                        with open("history.txt", "a" ,encoding="utf-8") as f:
                            f.write('\n[ZLAC] ['+now+'] [ADVANCED MODE] [>>] '+str(za))
                            f.write('\n[ZLAC] ['+now+'] [ADVANCED MODE] [ANSWER] '+str(calculate(za)))
                    except TypeError as e:
                        print('\n[ERROR] ',e)
                        console.print_exception(show_locals=True) 
                    except ZeroDivisionError as e:                          # Rich traceback handling
                        print('[ERROR]',e)       
                        console.print_exception(show_locals=True)
                    except ValueError as e:
                        print('[ERROR]',e) 
                        console.print_exception(show_locals=True) 
                    except NameError as e:
                        print('[ERROR]',e)
                        console.print_exception(show_locals=True)
                    except SyntaxError as e:
                        print('[ERROR]',e)
                        console.print_exception(show_locals=True)    
                    except OSError as e:
                        print('[ERROR]',e)
                        console.print_exception(show_locals=True)
                    

        else:

            def scal(n): # Evaluating the string input with eval() function

                if advance.checkifint(zl) == True:
                    return zl
                else:
                    op = compile(n, "<string>", "eval")   
                    if op.co_names:
                        raise NameError("[ERROR] Invalid usage") # Disallowing the use of names
                    return eval(op, {"__builtins__": {}},{})                 
            try:
                print(str(scal(zl))) # Printing the result after evaluating as string
                # Get current time
                now = datetime.now().strftime("%H:%M:%S")
                # Appending info to file > history.txt
                with open("history.txt", "a" ,encoding="utf-8") as f:
                    f.write('\n[ZLAC] ['+now+'] [SIMPLE MODE] [>]'+str(zl))
                    f.write('\n[ZLAC] ['+now+'] [ANSWER] '+str(scal(zl)))
        
            except TypeError as e:
                print('\n[ERROR] ',e)
                console.print_exception(show_locals=True) 
            except ZeroDivisionError as e:                          # Rich traceback handling
                print('[ERROR]',e)       
                console.print_exception(show_locals=True)
            except ValueError as e:
                print('[ERROR]',e) 
                console.print_exception(show_locals=True) 
            except NameError as e:
                print('[ERROR]',e)
                console.print_exception(show_locals=True)
            except SyntaxError as e:
                print('[ERROR]',e)
                console.print_exception(show_locals=True)    
            except OSError as e:
                print('[ERROR]',e)
                console.print_exception(show_locals=True)  

# Parsing argument  
# Start args doc / li / Start (s)

try:
    start_mode = sys.argv[1]  # Getting second argument in command line
    if start_mode.lower() == 'open' or start_mode.lower() == 'o':
        webbrowser.open('https://zlac-org.github.io/Zlac/')
    elif start_mode.lower() == 'li' or start_mode.lower() == 'license': 
        with open(doc_dir+"\LICENSE.txt") as f:
            print(f.read()) # Displays the full license file in terminal 
    elif start_mode.lower() == 'v' or start_mode.lower() == 'version':
        print('\nZlac version '+__version__)
    elif start_mode.lower() == 's' or start_mode.lower() == 'start':
        try:
            import window

        except ImportError:
            print('\n[ERROR] Failed importing window module.. ! window.py missing from > '+os.getcwd())
        try:

            zlac()
        except KeyboardInterrupt:
            exit_handler()

    elif start_mode.lower() == 'h.s' or start_mode.lower() == 'hide.start':
        try:
            zlac()
        except KeyboardInterrupt:
            exit_handler()

    elif start_mode.lower() == 'h' or start_mode.lower() == 'help':
        args = """
# python zlac.py <ARG> [version (v) | open (o) | license (li) | start (s) | hide.start (h.s) | help (h)]

`open (o)` : Open official website of Zlac-org

`license (li)` : Displays the full license file in terminal

`start (s)` : Runs the app with intro video

`hide.start (h.s)` : Runs the app without intro video

`help (h)` : Show this message and exit

        """
        md = Markdown(args)
        console.print(Panel(md, expand=True,title='Usage',style='dark_orange3'))
    else:
        # If user inputs wrong argument
        er = "Invalid argument '"+ start_mode+ "'" +"\nAvailable arguments (v | o | li | s | h.s | h)"
        console.print(Panel(er ,expand=True,title='Error',style="red1"))



except IndexError:
    # If user input has no argument
    args = "python zlac.py <ARG> [version (v) | open (o) | license (li) | start (s) | hide.start (h.s) | help (h)]"
    md = Markdown(args)
    console.print(Panel(md, expand=True,title='Usage'))






    
