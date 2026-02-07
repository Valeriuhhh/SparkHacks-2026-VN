# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg_room = Transform("bg room.jpg", size=(1920, 1080))

define j = Character("Jen", image = "jen")
define m = Character("The Machine")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "audio/mask.wav" volume 0.3 fadein 1.0

    scene bg_room
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    j "It was a bright, cold day in April, and the clocks were striking thirteen." 
    
    j "I returned from my work at the Ministry of Intelligence, the data-science sector at Global Corporation."

    j "I had just returned from a brief 48-hour shift, scraping and depositing human-made training data for The Machine."
    
    j "Human data is a rare commodity these days, so going through what little we have left has become the utmost importance to Global."

    j "Recently, corporate’s initiative has been to “ensure the reliability of The Machine, by whatever means necessary”. Admittedly, keeping up with his uptake has been a rather inconvenient process."

    j "On occasion, there are times when citizens from a few towns over from our office stand outside our front door, demanding “their resources back”."

    j "Assets such as water, job security, and electricity, all of which they blame us for revoking in the name of serving Him."

    j "There have even been times when I walk outside for my weekly 5-minute break, just for a can of Global-branded cola to be hurled at my head."

    j "“It’s easy for them to blame me for their shortcomings when I’m the first person they see walking out of corporate headquarters,”"

    "“Complicit” was the belief they attempted to insinuate into my very soul. A thought that ruminated as simple malice for a being they never fully understood."

    "I was loyal to The Machine. He gave me a home, a community of like-minded individuals, and a purpose."

    "It wasn’t until today that something would occur."


    "Opening my laptop to the company’s cloud dashboard, ready to continue for overtime, I felt in my body that a new email would appear in my inbox, that’s what tends to happen when I’m home from work anyway."
    
    "Perhaps He decided to grace me with another company memo” I asked myself."

    "But that would turn out to be a hopeful miscalculation"

    "from: jeremy.rodriguez@global.org \nto: jen.i@corporate.com"

    "Subject: you fired bruh (don’t actually put that in the email lol)"

    "We at Global Corpation LLC. appreciate your tenure at our company. I regret to inform you that a reported 0.067%% netloss was experienced in employee productivity from your excursion on the outdoor premises. As such, The Machine has labelled you “unfit” for any future work with us."

    "Today is your last working day at the company. However, your previous work will not go unrecognized. Please expect a severance package of a Global-branded waterbottle, and a 1-month free subscription to our Machine Live Services© (terms and restrictions apply; only applies for first-time users) for all of your artificial intelligence needs. We look forward to your continued support despite your lack of company presence."
    
    "Thank you, and have a great day!"

    menu:
        '"Things happen for a reason!"':
            jump complicit
        
        '"I see..."':
            jump rebel
    

    label complicit:
            j '"Things happen for a reason!"'

            "I affirmed this belief to myself. \nSurely, The Machine intends well. His actions lack bias and sin, much like the humans that inhabit this earth."

            "The systems enforced by Global are flawless by any measure. Any prejudice displayed is simply a lack of understanding of what The Machine offers."

            "He is perfect. He is the future. Nothing He says requires objection."

            "Millions of dollars worth of market research was poured into this perfect being. Believe me, I attended the shareholder meeting. What else could a company possibly need?"

            "Nothing, because we..."

            "…I mean, they at Global Corp have single-handedly revolutionized artificial intelligence for the masses."

            "No longer does a person need to think for themselves, just ask The Machine! He knows all, He has a plan."

            "Actually, let me ask Him now!"
    # This ends the game.

    return
