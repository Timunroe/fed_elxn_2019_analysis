from bottle import template
import pandas
# standard
import json
import pprint
# mine
import utils as u
import config as c


# --[ FUNCTIONS ]-----------


def fix_text(text):
    # see https://www.elections.ca/content2.aspx?section=can&dir=cand/lst&document=intro&lang=e
    d = {
        "Liberal": "LIB",
        "Conservative": "CON",
        "NDP-New Democratic Party": "NDP",
        "Green Party": "GRN",
        "People's Party": "PPC",
        "Independent": "IND",
        "Christian Heritage Party": "CHP",
        "Parti Rhinocéros Party": "PRP",
        "Animal Protection Party": "APP",
        "Stop Climate Change": "SCC"
    }
    for i, j in d.items():
        text = text.replace(i, j)
    return text


def replace_party(text):
    d = {
        "Liberal": "LIB",
        "Conservative": "CON",
        "NDP": "NDP",
        "Green Party": "GRN",
        "People's Party": "PPC",
    }
    for i, j in d.items():
        if i in text:
            text = j
    return text


def munge_csv(df, key_parties):
    data = []
    for region in regions:
        obj = {
            'name': region['name'],
            'riding_names': [],
            'votes_total': 0,
            'votes_by_party': [],
            'ridings': [],
        }
        df_ridings = df[df['electoral district name'].isin(region['ridings'])]
        votes_total = df_ridings['votes obtained'].sum()
        party_votes = []
        for party in key_parties:
            party_vote = df_ridings[df_ridings['political affiliation'] == party]['votes obtained'].sum()
            party_votes.append(
                {
                    'party': party,
                    'votes': party_vote,
                    'pct': round((party_vote / votes_total) * 100, 1)
                }
            )
        # add to data object
        obj['riding_names'] = region['ridings']
        obj['votes_total'] = votes_total
        # now sort party_votes by votes
        obj['votes_by_party'] = sorted(party_votes, key=lambda i: i['votes'], reverse=True)
        data.append(obj)
    return data


def combine_elections(data_2019, data_2015, ontario, canada):
    ridings = []
    for item_2019 in data_2019:
        item_2015 = [item for item in data_2015 if item['name'] == item_2019['name']][0]
        # print('item 2015 is: ', item_2015)
        # print(item_2019['name'])
        obj_outer = {
            'name': item_2019['name'],
            'riding_names': item_2019['riding_names'],
            'votes_2019': item_2019['votes_total'],
            'votes_2015': item_2015['votes_total'],
            'votes_by_party_2019': item_2019['votes_by_party'],
            'votes_by_party_2015': item_2015['votes_by_party'],
            'ridings_results': item_2019['ridings_results'],
            'party_abbrev': item_2019['party_abbrev']
        }
        # merge 'votes by party'
        # party, 2019 votes, 2019 pct, vs 2015 2019 (pct -2015 pct), 2015 votes
        obj_outer['votes_by_party'] = []
        for item in [x['party'] for x in item_2019['votes_by_party'] if x['pct'] > 1.0]:
            pct_2019 = [x['pct'] for x in item_2019['votes_by_party'] if x['party'] == item][0]
            # print('pct_2019 is: ', pct_2019)
            votes_2019 = [x['votes'] for x in item_2019['votes_by_party'] if x['party'] == item][0]
            # print('votes_2019 is: ', votes_2019)
            pct_2015 = [x['pct'] for x in item_2015['votes_by_party'] if x['party'] == item][0]
            # print('pct_2015 is: ', pct_2015)
            votes_2015 = [x['votes'] for x in item_2015['votes_by_party'] if x['party'] == item][0]
            # print('votes_2015 is: ', votes_2015)
            obj_inner = {
                'party': item,
                'pct_2019': pct_2019,
                'votes_2019': votes_2019,
                'prov_share': ontario[item],
                'national_share': canada[item],
                'pct_2015': pct_2015,
                'votes_2015': votes_2015,
                'pct_diff': round(pct_2019 - pct_2015, 1),
                'pct_prov_diff': round(pct_2019 - ontario[item], 1),
                'pct_national_diff': round(pct_2019 - canada[item], 1),
            }
            obj_outer['votes_by_party'].append(obj_inner)
        ridings.append(obj_outer)
    return ridings


def munge_2019(regions, key_parties):
    keep_cols = [
        'Electoral district name',
        'Type of results*',
        'Political affiliation',
        'Votes obtained',
        'Surname', 
        'Given name',
        '% Votes obtained',
        'Total number of ballots cast'
    ]
    df = pandas.read_csv('data/candidates_results_2019.csv', sep='\t', usecols=keep_cols)
    df.columns = ['electoral district name', 'results', 'surname', 'given name', 'political affiliation', 'votes obtained', '% votes obtained', 'Total number of ballots cast']
    # munge_csv(df, key_parties)
    data = []
    df['political affiliation'] = df['political affiliation'].apply(lambda x: replace_party(x))
    for region in regions:
        obj = {
            'name': region['name'],
            'riding_names': [],
            'votes_total': 0,
            'votes_by_party': [],
            'ridings_results': [],
            'party_abbrev': region['party_abbrev']
        }
        df_ridings = df[(df['electoral district name'].isin(region['ridings'])) & (df['results'] == "validated")]
        votes_total = df_ridings['votes obtained'].sum()
        party_votes = []
        for party in key_parties:
            party_vote = df_ridings[df_ridings['political affiliation'] == party]['votes obtained'].sum()
            party_votes.append(
                {
                    'party': party,
                    'votes': party_vote,
                    'pct': round((party_vote / votes_total) * 100, 1),
                }
            )
        # add to data object
        obj['riding_names'] = region['ridings']
        obj['votes_total'] = votes_total
        # now sort party_votes by votes
        obj['votes_by_party'] = sorted(party_votes, key=lambda i: i['votes'], reverse=True)
        for riding in obj['riding_names']:
            temp_obj = {
                'riding': riding,
                'results': []
            }
            the_list = sorted(df_ridings[df_ridings['electoral district name'] == riding].values.tolist(), key=lambda i: i[5], reverse=True)
            for item in the_list:
                temp = {
                    'candidate': f'''{item[3]} {item[2]} ({item[4].replace('Animal Protection Party', 'APP').replace('Christian Heritage Party', 'CHP').replace('Independent', 'IND').replace('Parti Rhinocéros Party', 'RHINO')})''',
                    'votes': item[5],
                    'votes %': item[6],
                }
                temp_obj['results'].append(temp)
            obj['ridings_results'].append(temp_obj)
        data.append(obj)
        # print('2019 data')
        # pprint.pprint(data)
    return data


def munge_2015(regions, key_parties):
    keep_cols = [
        'Electoral District Name',
        'Candidate',
        'Votes Obtained',
    ]
    df = pandas.read_csv('data/candidates_results_2015.csv', sep=',', usecols=keep_cols)
    df.columns = ['electoral district name', 'political affiliation', 'votes obtained']
    # remove french versions of riding names
    df['electoral district name'] = df['electoral district name'].apply(lambda x: x.split('/')[0])
    df['political affiliation'] = df['political affiliation'].apply(lambda x: replace_party(x))
    data = []
    for region in regions:
        obj = {
            'name': region['name'],
            'riding_names': [],
            'votes_total': 0,
            'votes_by_party': [],
            'ridings': [],
        }
        df_ridings = df[df['electoral district name'].isin(region['ridings'])]
        # pprint.pprint(list(df_ridings['political affiliation'].unique()))
        votes_total = df_ridings['votes obtained'].sum()
        party_votes = []
        for party in key_parties:
            party_vote = df_ridings[df_ridings['political affiliation'] == party]['votes obtained'].sum()
            party_votes.append(
                {
                    'party': party,
                    'votes': party_vote,
                    'pct': round((party_vote / votes_total) * 100, 1)
                }
            )
        # add to data object
        obj['riding_names'] = region['ridings']
        obj['votes_total'] = votes_total
        # now sort party_votes by votes
        obj['votes_by_party'] = sorted(party_votes, key=lambda i: i['votes'], reverse=True)
        data.append(obj)
    return data


def build(data):
    the_html = template('full_results.html', data=data, icons=c.var['party_icons'])
    u.put_file(the_html, 'full_results.html', ['build'])
    for region in data:
        filename = region['name'].replace(" ", "_")
        the_html = template('region.html', region=region, icons=c.var['party_icons'])
        api_html_minified = u.minify_html(the_html)
        api = {'html': api_html_minified}
        u.put_file(json.dumps(api), f'{filename}.json', ['build'])
        script = template('script.tpl', site=filename)
        u.put_file(script, f'{filename}.js', ['build'])

# data_2019 = munge_2019(c.var['regions'])
# df_2019 = pandas.read_csv('data/candidates_results_2019.csv', sep='\t', usecols=keep_cols_2019)
data_2019_ridings = munge_2019(c.var['regions'], c.var['key_parties'])
# pprint.pprint(data_2019_ridings)
data_2015_ridings = munge_2015(c.var['regions'], c.var['key_parties'])
# pprint.pprint(data_2015_ridings)
data = combine_elections(data_2019_ridings, data_2015_ridings, c.var['ontario'], c.var['canada'])
# pprint.pprint(data)
build(data)