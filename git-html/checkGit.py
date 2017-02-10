from bs4 import BeautifulSoup

def checkGit():
    data = []
    ecj_data = open("git.html", 'r').read()
    soup = BeautifulSoup(ecj_data, 'html.parser')
    #table = soup.findAll("table", {"class": "repositories"})
    table = soup.find('table', attrs={'class': 'repositories'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Get rid of empty values

    for i in data:
        x = len(i) - 2
        a = ["weeks","months"]
        for ai in a:
            if ai in i[x]:
                if ai == "weeks":
                    number = int(i[x].split(" ")[0]) * 7
                    if number > 30:
                        print "repo: " + i[0] + " last updated " + i[x] + " i.e " + str(number) + " days"
                if ai == "months":
                    number = int(i[x].split(" ")[0]) * 30
                    if number > 30:
                        print "repo: " + i[0] + " last updated " + i[x] + " i.e " + str(number) + " days"
def main():
    checkGit()


if __name__ == '__main__':
    main()