#! /bin/bash

ENDINGS=(
	"Today is the greatest day -Nate"
	"<insert_lame_joke_here> -Michael"
	"Apple sucks!! Use ENUMS!!!! -Ryan"
	"blah blah blah...Shenanigans -Makayden"
	"I wonder what this does? .. ***BOOM***"
	"Copy ~ Pasta"
	"I looked out the window and what did I see...snow..."
	"It takes a lot of balls to golf the way I do"
	"A clean desk is a sign of a cluttered drawer"
	"Hello IT. Have you tried turning it off and on again?"
	"Statistically, 6 out of 7 Dwarves are not Happy"
	"If the speed of light is 186,000 mi/sec, what is the speed of darkness?"
)

# Modified from https://gist.github.com/amberj/5166112?permalink_comment_id=3788836#gistcomment-3788836
green_echo() {
    echo -e "\x1b[1;32m $1"
}

IDX=$(( $RANDOM % ${#ENDINGS[@]} ))
green_echo """
${ENDINGS[${IDX}]}
"""