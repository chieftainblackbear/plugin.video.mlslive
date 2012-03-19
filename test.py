#!/usr/bin/python

import mlslive, sys

my_mls = mlslive.MLSLive()

if len(sys.argv) == 2:
    
    # get the streams
    streams = my_mls.getGameStreams(sys.argv[1])
    
    # print each stream bitrate and 
    for k in streams.keys():
        print k + ": " + streams[k]
    sys.exit(0)

if not my_mls.login('', ''):
    print "Unable to authenticte with MLS live. please set username and password."
    sys.exit(1)
    
games = my_mls.getGames()

for game in games:
    
    # Print the game info
    print game.game_id + ": " + game.time.strftime("%H:%M") + " "+ game.away + \
          " at " + game.home
