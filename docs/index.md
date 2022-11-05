# ZLAC - ORG
```

╭───────────────────────────────────────────────────── zlac ──────────────────────────────────────────────────────╮
│ ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════╗ │
│ ║                             Zlac-org - Hosting the advanced terminal calculator                             ║ │
│ ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════╝ │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```
[![Install-zlac](https://img.shields.io/badge/Download📥-00FF00?style=for-the-badge)]()
[![Git](https://img.shields.io/badge/Github-000000?style=for-the-badge)](https://github.com/zlac-org)
[![Rel](https://img.shields.io/badge/Releases-800080?style=for-the-badge)](https://github.com/Zlac-org/Zlac/releases)

```
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Zlac-org hosts the Zlac calculator - an advanced console based calculator made in Python 🐍 .                   │
│                                                                                                                 │
│  • Feature                                                                                                      │
│                                                                                                                 │
│ You can do basic math operations like + , - , * , / , // [Greatest integer function], % [Modulo] or compare two │
│ numbers with < , > , <= , >= directly from your terminal in simple mode. Just enter '>' to jump to advanced     │
│ mode where you can find the area and perimeter of a triangle , square , rectangle , circle ; do operations      │
│ using 'π' ; find the log and natural logarithm (ln) ; find square root ('√') of a number ;  find factorial      │
│ ('!') of a number ; find percentage ('%')                                                                       │
│                                                                                                                 │
│  • How to use ??                                                                                                │
│                                                                                                                 │
│ Zlac accepts six command line arguments 'version (v) | open (o) | license (li) | start (s) | hide.start (h.s) | │
│ help (h)' . To start the application with intro video, type 'zlac s' ; to start without intro video, type 'zlac │
│ h.s' You can view the license or open this webpage by entering 'zlac li' or `zlac o'  . You can enter Advanced  │
│ mode with '>' and return by '<'                                                                                 │
│                                                                                                                 │
│  • History file                                                                                                 │
│                                                                                                                 │
│ History file appends all progress made by the user . To clear history simply delete the file. You can access    │
│ the file through Zlac when working by entering 'h...' or 'history...'                                           │
│ An example history file :                                                                                       │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
```
╭────────────────────────────────────────────────── history.txt ──────────────────────────────────────────────────╮
│ [ZLAC] [15:44:39] [SIMPLE MODE] [>]5//3                                                                         │
│ [ZLAC] [15:44:39] [ANSWER] 1                                                                                    │
│ [ZLAC] [15:44:43] [SIMPLE MODE] [>]8*0                                                                          │
│ [ZLAC] [15:44:43] [ANSWER] 0                                                                                    │
│ [ZLAC] [15:45:20] [SIMPLE MODE] [>]34+45-8/(9+2)*2-(333+1)/3/1/(44-345)                                         │
│ [ZLAC] [15:45:20] [ANSWER] 77.91533272928622                                                                    │
│ [ZLAC] [15:45:35] [ADVANCED MODE] [>>] π / 2                                                                    │
│ [ZLAC] [15:45:35] [ADVANCED MODE] [ANSWER] 1.5707963267948966                                                   │
│ [ZLAC] [15:45:41] [ADVANCED MODE] [>>] π + 12                                                                   │
│ [ZLAC] [15:45:41] [ADVANCED MODE] [ANSWER] 15.141592653589793                                                   │
│ [ZLAC] [15:45:47] [ADVANCED MODE] [>>] π // 2                                                                   │
│ [ZLAC] [15:45:47] [ADVANCED MODE] [ANSWER] None                                                                 │
│ [ZLAC] [15:45:57] [ADVANCED MODE] [>>] 3!                                                                       │
│ [ZLAC] [15:45:57] [ADVANCED MODE] [ANSWER] 6                                                                    │
│ [ZLAC] [15:46:04] [ADVANCED MODE] [>>] 8!                                                                       │
│ [ZLAC] [15:46:04] [ADVANCED MODE] [ANSWER] 40320                                                                │
│ [ZLAC] [15:46:11] [ADVANCED MODE] [>>] 45!                                                                      │
│ [ZLAC] [15:46:11] [ADVANCED MODE] [ANSWER] 119622220865480194561963161495657715064383733760000000000            │
│ [ZLAC] [15:46:17] [ADVANCED MODE] [>>] 5%5                                                                      │
│ [ZLAC] [15:46:17] [ADVANCED MODE] [ANSWER] 100.0                                                                │
│ [ZLAC] [15:46:20] [ADVANCED MODE] [>>] 5%                                                                       │
│ [ZLAC] [15:46:20] [ADVANCED MODE] [ANSWER] 0.05                                                                 │
│ [ZLAC] [15:46:29] [ADVANCED MODE] [>>] 4ar.rect5                                                                │
│ [ZLAC] [15:46:29] [ADVANCED MODE] [ANSWER] 20.0                                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
```
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                 │
│  • Download                                                                                                     │
│                                                                                                                 │
│ You can download binary releases from above or from Github releases For source download the 'tar-gz' file from  │
│ releases and unzip or alternatively clone this repository using Git .                                           │
│                                                                                                                 │
│  • Dependencies                                                                                                 │
│                                                                                                                 │
│ When building from source make sure to install all dependencies using 'pip install -r requirements.txt' .       │
│ Layout made with rich and intro video played using python-vlc .                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
```
╭─────────────────────────────────────────────────── Releases ────────────────────────────────────────────────────╮
│  Versions 🏷️                                                                                                    |
│ └── 2022.11.05                                                                                                  │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
```
╭─────────────────────────────────────────────────── Examples ────────────────────────────────────────────────────╮
│                                                                                                                 │
│  • Usage examples                                                                                               │
│                                                                                                                 │
│ To view examples in Zlac calculator enter '?' or 'help' or 'h' . To clear screen or refresh enter 'cl' or       │
│ 'clear' and to exit enter 'exit' or 'e' or alternatively you can press 'ctrl+c'. To view history just enter     │
│ 'history...' or 'h...'                                                                                          │
│                                                                                                                 │
│  • In simple mode                                                                                               │
│                                                                                                                 │
│ > 2*5                                                                                                           │
│ 10                                                                                                              │
│                                                                                                                 │
│ > 5*34/(3*6)                                                                                                    │
│ 9.444444444444445                                                                                               │
│                                                                                                                 │
│ > 5*(5/6)                                                                                                       │
│ 4.166666666666667                                                                                               │
│                                                                                                                 │
│ > 5**5                                                                                                          │
│ 3125                                                                                                            │
│                                                                                                                 │
│ > 4*-4/3                                                                                                        │
│ -5.333333333333333                                                                                              │
│                                                                                                                 │
│ > -4.3/3                                                                                                        │
│ -1.4333333333333333                                                                                             │
│                                                                                                                 │
│ > 4%345//9/3+12-3                                                                                               │
│ 9.0                                                                                                             │
│                                                                                                                 │
│ > 45<4                                                                                                          │
│ False                                                                                                           │
│                                                                                                                 │
│ > 3<4>3                                                                                                         │
│ True                                                                                                            │
│                                                                                                                 │
│ > 6<=4                                                                                                          │
│ False                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯ 
```
