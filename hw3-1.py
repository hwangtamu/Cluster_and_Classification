#from search import searchnews
import k_means, json

news = {}

            
if __name__ == '__main__':
    #target = ['texas aggies', 'texas longhorns', 'duke blue devils', 'dallas cowboys', 'dallas mavericks']
    #for t in target:
    #    searchnews(t, news)

    f = open('./news.json')
    news = json.load(f)
    f.close()

    k = raw_input('input an integer k: ')
    k = int(k)
    k_means.kmeans_optimal(k, news)

