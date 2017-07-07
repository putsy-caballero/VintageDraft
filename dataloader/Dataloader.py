import csv
from entities import db
from entities.Batter import BatterYearStats, BatterCareerStats, FielderPositionStats
from entities.Pitcher import PitcherYearStats, PitcherCareerStats
from entities.entity_enums import Positions

class Dataloader(object):

    @staticmethod
    def update_map_numbers(map, data, fields):
        if map == None:
            map = {}
            for key in fields:
                map[key] = int(data[key] or 0)
        else:
            for key in fields:
                map[key] = map[key] + int(data[key] or 0)
        return map

    @staticmethod
    def calc_era_whip(data):
        ipouts = data['IPouts']
        if ipouts == 0:
            ipouts = 0.01
        era = data['ER'] * 27 / ipouts
        whip = 3 * (data['H'] + data['BB']) / ipouts
        return (era, whip)

    @staticmethod
    def calc_avg_obp_slg(data):
        ab = data['AB']
        if ab == 0:
            ab = 0.00001
        avg = data['H'] / ab
        obp = (data['H'] + data['BB'] + data['HBP']) / (ab + data['BB'] + data['HBP'] + data['SF'])
        slg = (3 * data['HR'] + 2 * data['3B'] + data['2B'] + data['H']) / ab
        return (avg, obp, slg)

    @staticmethod
    def load_pitcher_data():
        pitcher_year_dict = {}
        pitcher_career_dict = {}
        pitcher_data_list = "playerID,yearID,stint,teamID,lgID,W,L,G,GS,CG,SHO,SV,IPouts,H,ER,HR,BB,SO,BAOpp,ERA,IBB,WP,HBP,BK,BFP,GF,R,SH,SF,GIDP".split(",")
        pitcher_number_fields = "W,L,G,GS,CG,SHO,SV,IPouts,H,ER,HR,BB,SO,IBB,WP,HBP,BK,BFP,GF,R,SH,SF,GIDP".split(",")
        with open("C:\\Users\\Mike\\Desktop\\Pitching.csv", "r") as pitchers:
            csvreader = csv.reader(pitchers, delimiter=',')
            next(csvreader)
            for data in csvreader:
                data_map = {}
                for i in range(0, len(pitcher_data_list)):
                    data_map[pitcher_data_list[i]] = data[i]
                id = data_map['playerID']
                year = int(data_map['yearID'])
                if id not in pitcher_year_dict:
                    pitcher_year_dict[data_map['playerID']] = {}
                pitcher_year_dict[id][year] = Dataloader.update_map_numbers(pitcher_year_dict[id].get(year), data_map, pitcher_number_fields)
                pitcher_career_dict[id] = Dataloader.update_map_numbers(pitcher_career_dict.get(id), data_map, pitcher_number_fields)

        for key in pitcher_career_dict:
            for year in pitcher_year_dict[key]:
                calc = Dataloader.calc_era_whip(pitcher_year_dict[key][year])
                pitcher_year_dict[key][year]['ERA'] = calc[0]
                pitcher_year_dict[key][year]['WHIP'] = calc[1]
            calc = Dataloader.calc_era_whip(pitcher_career_dict[key])
            pitcher_career_dict[key]['ERA'] = calc[0]
            pitcher_career_dict[key]['WHIP'] = calc[1]

        return (pitcher_year_dict, pitcher_career_dict)

    @staticmethod
    def load_batter_data():
        batter_year_dict = {}
        batter_career_dict = {}
        batter_data_list = "playerID,yearID,stint,teamID,lgID,G,AB,R,H,2B,3B,HR,RBI,SB,CS,BB,SO,IBB,HBP,SH,SF,GIDP".split(",")
        batter_number_fields = "G,AB,R,H,2B,3B,HR,RBI,SB,CS,BB,SO,IBB,HBP,SH,SF,GIDP".split(",")
        with open("C:\\Users\\Mike\\Desktop\\Batting.csv", "r") as batters:
            csvreader = csv.reader(batters, delimiter=',')
            next(csvreader)
            for data in csvreader:
                data_map = {}
                for i in range(0, len(batter_data_list)):
                    data_map[batter_data_list[i]] = data[i]
                id = data_map['playerID']
                year = int(data_map['yearID'])
                if id not in batter_year_dict:
                    batter_year_dict[data_map['playerID']] = {}
                batter_year_dict[id][year] = Dataloader.update_map_numbers(batter_year_dict[id].get(year), data_map, batter_number_fields)
                batter_career_dict[id] = Dataloader.update_map_numbers(batter_career_dict.get(id), data_map, batter_number_fields)

        for key in batter_career_dict:
            for year in batter_year_dict[key]:
                calc = Dataloader.calc_avg_obp_slg(batter_year_dict[key][year])
                batter_year_dict[key][year]['AVG'] = calc[0]
                batter_year_dict[key][year]['OBP'] = calc[1]
                batter_year_dict[key][year]['SLG'] = calc[2]
            calc = Dataloader.calc_avg_obp_slg(batter_career_dict[key])
            batter_career_dict[key]['AVG'] = calc[0]
            batter_career_dict[key]['OBP'] = calc[1]
            batter_career_dict[key]['SLG'] = calc[2]
        return (batter_year_dict, batter_career_dict)

    @staticmethod
    def load_fielder_data():
        position_map = {
            "C": Positions.catcher,
            "1B": Positions.first_base,
            "2B": Positions.second_base,
            "3B": Positions.third_base,
            "SS": Positions.shortstop,
            "OF": Positions.outfield,
            "P": Positions.pitcher
        }

        fielder_dict = {}
        fielder_data_list = "playerID,yearID,stint,teamID,lgID,POS,G,GS,InnOuts,PO,A,E,DP,PB,WP,SB,CS,ZR".split(",")
        fielder_number_fields = "G,GS,InnOuts".split(",")

        with open("C:\\Users\\Mike\\Desktop\\Fielding.csv", "r") as fielders:
            csvreader = csv.reader(fielders, delimiter=',')
            next(csvreader)
            for data in csvreader:
                data_map = {}
                for i in range(0, len(fielder_data_list)):
                    data_map[fielder_data_list[i]] = data[i]
                id = data_map['playerID']
                pos = position_map[data_map['POS']]
                if id not in fielder_dict:
                    fielder_dict[id] = {}
                fielder_dict[id][pos] = Dataloader.update_map_numbers(fielder_dict[id].get(pos), data_map, fielder_number_fields)
        return fielder_dict

(pitcher_year_dict, pitcher_career_dict) = Dataloader.load_pitcher_data()
(batter_year_dict, batter_career_dict) = Dataloader.load_batter_data()
fielder_dict = Dataloader.load_fielder_data()

db.create_all()

for key in fielder_dict:
    for pos in fielder_dict[key]:
        fielder = FielderPositionStats(key, pos, fielder_dict[key][pos])
        db.session.add(fielder)
db.session.commit()

for key in pitcher_year_dict:
    pitcher_career = PitcherCareerStats(key, pitcher_career_dict[key])
    db.session.add(pitcher_career)
    for year in pitcher_year_dict[key]:
        pitcher = PitcherYearStats(key, year, pitcher_year_dict[key][year])
        db.session.add(pitcher)
db.session.commit()

for key in batter_year_dict:
    batter_career = BatterCareerStats(key, batter_career_dict[key])
    db.session.add(batter_career)
    for year in batter_year_dict[key]:
        batter = BatterYearStats(key, year, batter_year_dict[key][year])
        db.session.add(batter)
db.session.commit()
