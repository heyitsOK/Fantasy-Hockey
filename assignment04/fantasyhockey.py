#Omar Khan Student ID: 101168124

#Reads all the stats from the csv file and returns a 2D List
def readStats(fileName):
    try:
        file = open(fileName)
        lines = file.readlines()
        stats = []
        
        for i in range(1, len(lines)):
            stats.append(lines[i].split(","))
            
        for i in range(len(stats)):
            for j in range(len(stats[i])):
                if stats[i][j].endswith("\n"):
                    text = stats[i][j]
                    text = text[:-1]
                    stats[i][j] = text
        
        for i in range(len(stats)):
            for j in range(len(stats[i])):
                if stats[i][j].isdigit():
                    stats[i][j] = int(stats[i][j])
        
        return stats
        
    except:
        print("The file does not exist!")
        return []

#Gets the stats for a specific player from the all the stats 2D list
def statsForPlayer(stats2D, name):
    player = []
    for i in range(len(stats2D)):
        if stats2D[i][0] == name:
            player = stats2D[i]
    return player

#Returns a a 2D list of stats of only players that play the position passed in
def filterByPos(stats2D, pos):
    filtered = []
    for i in range(len(stats2D)):
        if stats2D[i][2] == pos:
            filtered.append(stats2D[i])
    return filtered

#Returns a 2D list of stats sorted by descending order of points
def sortByPoints(stats2D):
    sorted = []
    sorted = stats2D
    for i in range(len(sorted)-1,0,-1):
        for j in range(i):
            if sorted[j][6] < sorted[j+1][6]:
                temporary = sorted[j]
                sorted[j] = sorted[j+1]
                sorted[j+1] = temporary 
    
    return sorted

#Builds a team of 5 best players
def buildBestTeam(stats2D, fileName):
    sorted = sortByPoints(stats2D)
    bestTeam = []
    positions = ['C','LW','RW','D','D']
    f = open(fileName, 'w+')
    
    for j in range(0, len(positions)):
        for i in range(0, len(sorted)):
            if sorted[i][2] == positions[j]:
                bestTeam.append(sorted[i][0])
                sorted.remove(sorted[i])
                break
    
    for i in range(len(bestTeam)):
        f.write(bestTeam[i] + "\n")

#Displays the stats of the team passed in
def displayTeamStats(stats2D, fileName):
    f = open(fileName)
    bestTeam = f.readlines()
    for i in range(len(bestTeam)):
        if bestTeam[i].endswith("\n"):
            temp = bestTeam[i]
            temp = temp[:-1]
            bestTeam[i] = temp
    
    teamStats = []
    for i in range(len(bestTeam)):
        for j in range(len(stats2D)):
            if bestTeam[i] == stats2D[j][0]:
                teamStats.append(stats2D[j])
    print(teamStats)
    #print(bestTeam)
    print("Name\t\tTeam\tPos\tGames\tG\tA\tPts\tPIM\tSOG\tHits\tBS")
    print("===========================================================================================")
    for i in range(len(teamStats)):
        row = ""
        for j in range(len(teamStats[i])):
            row += str(teamStats[i][j]) + "\t"
        print(row)

#Returns the total number of points of the team that's passed in
def pointsPerTeam(stats2D, fileName):
    try:
        total = 0 
        f = open(fileName)
        bestTeam = f.readlines()
        for i in range(len(bestTeam)):
            if bestTeam[i].endswith("\n"):
                temp = bestTeam[i]
                temp = temp[:-1]
                bestTeam[i] = temp
    
        teamStats = []
        for i in range(len(bestTeam)):
            for j in range(len(stats2D)):
                if bestTeam[i] == stats2D[j][0]:
                    teamStats.append(stats2D[j])
        
        for i in range(len(teamStats)):
            total += teamStats[i][6]
        
        return total
        
    except:
        return 0

stats = readStats("nhl_2018.csv")
displayTeamStats(stats, "my_team.txt")
print(pointsPerTeam(stats, "my_team.txt"))