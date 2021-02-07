file = "WorldSeries.txt"

def main():

    input_file = open_file() 
    team_dict, win_count_dict = make_dict(input_file)
    get_prompt(team_dict, win_count_dict) 

def open_file():
    input_file = open(file, 'r')
    return input_file
    
def make_dict(input_file):
    team_dict = {}
    line = input_file.readline().rstrip('\n')
    for i in range(1903, 2009):
        if i != 1904 and i != 1994:
            team_dict[i] = line
            line = input_file.readline().rstrip('\n')
        
    print(team_dict, '\n')
    win_count_dict = {}
    for i in range(1903, 2009):
        if i != 1904 and i != 1994:
            team = team_dict[i]
            if not team in win_count_dict:
                win_count_dict[team] = 1
            else:
                win_count_dict[team] += 1
    print(win_count_dict, '\n')
    return team_dict, win_count_dict

def get_prompt(team_dict, win_count_dict):

    valid = True
    while valid:
        try:
            year = int(input('Enter a year in the range from 1903 to 2008 to '
                             'know which team won World Series in the year: '))
            if year > 1903 and year < 2008 and year != 1904 and year != 1994:
                print('The winning team in', year, 'was the', team_dict[year] + '.')
                print('The', team_dict[year], 'won', win_count_dict[team_dict[year]], 'times between 1903 and 2008.')
                valid = False
            elif year == 1904:
                print('World Series Not Played in 1904')
                valid = False
            elif year == 1994:
                print('World Series Not Played in 1994')
                valid = False
            elif year < 1903 or year > 2008:
                print('No records found')
                valid = False
        except:
           print('Enter a year in integer.')
    

main()