import html
from stats import game_stats
from conf import db_conf

# logFile = "E:/python/log/log.log"
# sc = SparkContext("local","Simple App")
# logData = sc.textFile(logFile).cache()
#
# numAs = logData.filter(lambda s: 'a' in s).count()
# numBs = logData.filter(lambda s: 'b' in s).count()
#
# print("Lines with a: %i, lines with b: %i"%(numAs, numBs))
# output = open('E:/python/log/log.log', 'w+')
if __name__ == '__main__':
    data_dicts = []
    for i in range(1, 39792):
        url = "http://www.stat-nba.com/game/" + str(i) + ".html"

        data = html.get_html(url)
        data_list, name_list = html.get_data(data)

        print(i)
        data_entitys = []
        for data_itr in data_list:
            idx = int(data_itr[2])

            if (idx >= len(data_entitys)):
                stats = game_stats.GameStats()
                stats.name = name_list[idx]
                data_entitys.append(stats)
            else:
                stats = data_entitys[idx]
            stats.build(data_itr)

        for data_itr in data_entitys:
            data_dicts.append(data_itr.__dict__)
        if i % 100 == 0:
            db_conf.collection_game_stats.insert(data_dicts)
            data_dicts = []
    db_conf.collection_game_stats.insert(data_dicts)
