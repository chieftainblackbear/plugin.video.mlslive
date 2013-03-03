#!/usr/bin/python

import mlslive, sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-u', '--user', type='string', dest='user',
                  help="Username for authentication")
parser.add_option('-p', '--password', type='string', dest='password',
                  help="Password for authentication")
parser.add_option("-g", "--game", type='string', dest='game',
                  help="Game to display")

(options, args) = parser.parse_args()

if options.user == None:
    print "ERROR: please specify a username (call with -h for help)"
    sys.exit(1)
elif options.password == None:
    print "ERROR: please specify a password (call with -h for help)"
    sys.exit(1)

my_mls = mlslive.MLSLive()


if not my_mls.login(options.user, options.password):
    print "Unable to authenticte with MLS live. please set username and password."
    sys.exit(1)

if options.game != None:
    
    # get the streams
    stream = my_mls.getGameStream(options.game)
    
    # print the stream
    print stream
     
    sys.exit(0)

#games = my_mls.getGames()
games = my_mls.getGames(0)
teams = my_mls.getTeams()

for game in games:

    print game['gameID'] + ": " + my_mls.getGameString(game, "at") 
    home = my_mls.getTeamAbbr(teams, game['homeTeamID'])
    vist = my_mls.getTeamAbbr(teams, game['visitorTeamID'])
    if home != None:
        print '\t' + home
    if vist != None:
        print '\t' + vist 

