Welcome to my text files archive of Sandolphan's **excellent** Mastermind Numpad Binds! 👋 This archive contains text Numpad bind files based entirely on Sandolphan’s brilliant guide from the old forums (see “FAQ” below).

Each .zip archive in this folder (except for ‘All’) contains a single set of Mastermind Numpad keybinds text files relating to each respective Mastermind primary.  All, of course, contains all of them in a single archive.

In order to use these keybinds, you first need to unzip the file(s) you want wherever your game client stores keybinds, which can be different for different launcher types.
- Tequila/Sunrise Launcher: your City of Heroes\Data\ folder
- Homecoming Launcher: \Settings\Live under the CoH Installation folder
- Ouroboros.exe: your bind files will go in Client\Piggs\ - This one surprised me

**Please note**: you don’t *have* to put them in the default binds location, but you *will* have to edit the bind files to include your new path if you don't.

## How it Works
Numpad 0 = select all pets for command
Numpad 1 = Select minions for command
Numpad 2 = Select Lieutenants for command
Numpad 3 = Select Boss for command
Numpad 4 = Aggressive stance
Numpad 5 = Defensive stance
Numpad 6 = Passive stance
Numpad 7 = Attack target
Numpad 8 = Follow
Numpad 9 = Go To
Numpad / = Summon Minions
Numpad * = Summon Lieutenants
Numpad - = Summon Boss
Numpad + = First pet upgrade
Numpad Enter = Second upgrade
Left Ctrl + decimal = Dismiss pet(s)

### Examples
Let's say you're a **Thugs/Traps** Mastermind.  You want your bruiser to charge into melee, but you want to keep everything else in bodyguard mode beside you.

0 - select all your pets
5 - make sure they're all in Bodyguard mode
3 - seleft your Bruiser pet
7 - Send Bruiser in to attack.

It might sound a bit unwieldy, but once you've had a little practice, especially just using 0, 7 (select all pets, attack my target) it *quickly* becomes second nature.

## FAQ
**Q:** So how do I load these binds?  Is it hard?
**A:** Each bind set relies on five files.  A 'master' file ending in MM.txt (for example, NinjasMM.txt), three pet files - one for each tier of pets, and a file labeled "all.txt."

You want them all in the same directory.  After logging in to the game on your mastermind, type `/bind_load_file masterfileMM.txt` but with the name of your primary's master file.  I.e. `/bind_load_file NinjasMM.txt`

That's it!  Press Numpad 0 to get 'All.txt' loaded up, and start summoning and buffing away!

**Q:** Did you write all these?
**A: ** Nope!  I take zero credit for this amazing work.  A credit for these keybinds goes to Sandolphan from the original forums: archive.org link here: [Sandolphan's Revised MM Numpad Pet Controls](https://web.archive.org/web/20120904222729/http://boards.cityofheroes.com/showthread.php?t=117256 "Sandolphan's Revised MM Numpad Pet Controls")  

All I did was create a  Python script that let me automatically generate the pet files.  But they are 100% fully tested and working (that was the hard part!)

**Q:** Why go through all this trouble?
**A:** In every version of the guide that I've found, there's always just a sample code block and then you have to fill in the rest yourself.

I have severe altitis, so I make lots of themed characters, play them for awhile, maybe keep them, maybe delete them, but redoing those binds is a PITA.  I've never seen an archive of the binds completed before so I set out to make one.

I *very* quickly realized I could make a Python script that could do it for me, and Bob's your second cousin's wife's sister's neighbor.

**Q:** Can I add to these binds?
**A:** Of course!  Sandolphan’s guide has an entire subsection on giving your minions orders based on their pet name.  There’s also things like petcom_say for using emotes.  Nothing quite so creepy as a Necromancer surrounded by her (named) minions, all holding torches while one lone zombie cowers in the middle, hey? ;)   That’s beyond the purview of this simple project though.

## CreditsCredits
Sandolphan of course, for devising such an ingenious method of pet control.  These binds have made Masterminds my absolute favorite class bar none!

Shenanigunner’s awesome City of Heroes Technical Manual and Heroica
http://www.shenanigunner.com/ 
While just being an all around excellent resource, I wouldn’t have found the default locations for binds across the different launchers without having to manually log into each, create test characters, and trial and error my way through creating and saving dummy bind files.

## About the AuthorAbout the Author
I played City of Heroes from just after Issue 1 launched though at the time, I hadn’t realized the game had only been out for a few months.  A friend talked me into joining with him on the Virtue server where I ran with a handful of small-to-very-small supergroups over the years.  I was never a big face on the server, and I honestly liked it that way - despite some of my SG members’ best efforts to introduce me to the likes of Ascendant and others :P

Outside of the game, I'm legally blind, LGBTQ (transgender, lesbian), an extremely geeky author, I love music and play the piano, guitar, saxophone, and dabble in violin sometimes, I am an ADHD/neuro atypical advocate (and may be on the autism spectrum.

[@ScaerieTale](https://www.twitter.com/ScaerieTale "@ScaerieTale") on twitter for hot takes on politics, and ramblings about whatever I’m hyperfocused/fixated on at the moment, but usually programming, game design, music, or, and let’s be honest here, shit posting. <3
