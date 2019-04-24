Sorting your Windows Development environment
---

To start with, my Windows skills are **rusty** - my time at ThoughtWorks means I've  been working almost exclusively with macOS for the last few years.

The other thing I've realised is, even when I did support Windows systems - it was in a support role solving user issues and fixing broken hardware. I've never actually done any _development_ work on Windows. There are _so many_ tools on macOS/Linux that I just take for granted that aren't immediately available on Windows.

In this instance we want to build a simple python application. So we'll need the following:

* Python 3
* Git for Windows
* A suitable IDE.

The IDE is interesting. On Mac/Linux - I'm happy firing up a terminal (or three) and getting stuck in. On Windows I find the Powershell environment confusing and unhelpful - so using a IDE to hide that complexity is actually very helpful. And is something I should _really_ take back with me to the Mac. I've heard nothing but good things about Microsoft's [VSCode](https://code.visualstudio.com/) albeit on Mac - so as I'm working on Windows, why not take it for a spin.

We also want our application to be self-contained. As a result it's important to get our python environment setup properly. Unlike a Mac, Windows doesn't come with a system version of python. This can be a good thing, as we can work with Python 3 - and not end up on Python 2.7 which is _still_ the default on new Macs, but is due for retirement [very soon](https://pythonclock.org/)...