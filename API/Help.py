def Help(body):
    X = 1
    for words in body:
        if X == 1:
            if words == "Help" or words == "help":
                X = "What do you need help with? Right now all I do is ask if you need help! \n Hopefully soon I will be able to do more than this."
            if words == "Progress" or words == "progress":
                X = "Right now all this does is respond to Help and Progress, however I have figured out how to call functions outside of the file. \n Now to figure out what to do next? Budget Bot here I come"
    if X == 1:
        return "Try using the term Progress or Help"
    else:
        return X
