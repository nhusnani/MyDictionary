file = "WorldSeries.txt"

def open_file():
    return open(file, 'r')
def make_dict(file_object):
    champ_dict = {}
    line = file_object.readline().rstrip('\n')
    for i in range(1903, 2009):
        champ_dict[i] = line
        line = file_object.readline().rstrip('\n')
    #print(champ_dict, '\n')
    numb_dict = {}
    for i in range(1903, 2009):
        team = champ_dict[i]
        if not team in numb_dict:
            numb_dict[team] = 1
        else:
            numb_dict[team] += 1
    #print(numb_dict, '\n')
    return champ_dict, numb_dict

def get_prompt(champ_dict, numb_dict):

    valid = True
    while valid:
        try:
            year = int(input('Enter a year in the range from 1903 to 2008 to '
                             'know which team won World Series in the year: '))
            if year > 1902 and year < 2008 and year != 1904 and year != 1994:
                print(champ_dict[year], 'won in the year!',numb_dict[champ_dict[year]], 'times')
                valid = False
            elif year == 1904:
                print('World Series Not Played in 1904')
                valid = False
            elif year == 1994:
                print('World Series Not Played in 1994')
                valid = False
        except:
            print('Enter a year in integer.')
    
def main():

    file_object = open_file() 
    champ_dict, numb_dict = make_dict(file_object)
    get_prompt(champ_dict, numb_dict) 

main()