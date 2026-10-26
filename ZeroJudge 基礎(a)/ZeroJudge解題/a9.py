pw=(list(map(lambda c: chr(ord(c)-7),input())))
#因為map是涵式所以若要讓map, filter這種解果print出來得話，外面加一層list即可，
#再搭配.join or *
print("".join(pw))