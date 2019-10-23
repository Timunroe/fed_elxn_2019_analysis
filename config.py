
var = {
    # if not spaces, hyphens in riding names: Hamilton Eastâ\x80\x94Stoney Creek
    'api': 'https://thecanadianpress-a.akamaihd.net/graphics/2019/federal-election/data/full_results.json',
    'party_leaders': [
        # leading riding, won riding, lost riding
        {
            'Name': 'Maxime Bernier',
            'Party': 'PPC',
            'Riding': 'Beauce',
            'Riding_no': 39,
            'Id': 2,
            'Result': 'Lost'
        },
        {
            'Name': 'Yves-François Blanchet',
            'Party': 'BQ',
            'Riding': 'Beloeil-Chambly',
            'Riding_no': 43,
            'Id': 2,
            'Result': 'Elected'
        },
        {
            'Name': 'Elizabeth May',
            'Party': 'GRN',
            'Riding': 'Saanich—Gulf Islands',
            'Riding_no': 320,
            'Id': 3,
            'Result': 'Elected'
        },
        {
            'Name': 'Andrew Scheer',
            'Party': 'CON',
            'Riding': 'Regina—Qu\'Appelle',
            'Riding_no': 253,
            'Id': 6,
            'Result': 'Elected'
        },
        {
            'Name': 'Jagmeet Singh',
            'Party': 'NDP',
            'Riding': 'Burnaby South',
            'Riding_no': 296,
            'Id': 5,
            'Result': 'Elected'
        },
        {
            'Name': 'Justin Trudeau',
            'Party': 'LIB',
            'Riding': 'Papineau',
            'Riding_no': 87,
            'Id': 9,
            'Result': 'Elected'
        },
    ],
    'party_colors': {
        'CON': '#003f73',
        'GRN': '#2e7528',
        'NDP': '#f89921',
        'LIB': '#d71920',
        'PPC': '#442d7b',
        'Others': '#ccc',
        'BQ': '#093c71',
    },
    'sites': {
        'spectator': {
            'tabs': [
                (1, 'Hamilton', 'default'),
                (2, 'Halton', ''),
                (3, 'Grimsby-Brant', '')
            ],
            'template': 'options_all',
            'ridings': [
                [
                    'Hamilton Centre',
                    'Hamilton Mountain',
                    'Hamilton East-Stoney Creek',
                    'Hamilton West-Ancaster-Dundas',
                    'Flamborough-Glanbrook'
                ],
                [
                    'Burlington',
                    'Oakville North-Burlington',
                    'Oakville',
                    'Milton'
                ],
                [
                    'Niagara West',
                    'Haldimand-Norfolk',
                    'Brantford-Brant',
                ]
            ],
        },
        'record': {
            'tabs': [
                (1, 'Waterloo Region', 'default'),
                (2, 'Guelph-Perth-Oxford', ''),
            ],
            'template': 'options_parties_ridings',
            'ridings': [
                [
                    'Kitchener-Conestoga',
                    'Waterloo',
                    'Kitchener Centre',
                    'Kitchener South-Hespeler',
                    'Cambridge',
                ],
                [
                    'Guelph',
                    'Wellington-Halton Hills',
                    'Perth-Wellington',
                    'Oxford'
                ]
            ]
        },
        'examiner': {
            'tabs': [
                (1, 'Peterborough', 'default'),
            ],
            'template': 'options_parties_ridings',
            'ridings': [
                [
                    'Peterborough-Kawartha',
                    'Northumberland-Peterborough South',
                    'Haliburton-Kawartha Lakes-Brock',
                    'Hastings-Lennox and Addington'
                ],
            ],
        },
        'halton': {
            'tabs': [
                (1, 'Halton', 'default'),
            ],
            'template': 'options_parties_ridings',
            'ridings': [
                [
                    'Burlington',
                    'Oakville North-Burlington',
                    'Oakville', 'Milton'
                ],
            ],
        },
        'niagara': {
            'tabs': [
                (1, 'Niagara Region', 'default'),
            ],
            'template': 'options_parties_ridings',
            'ridings': [
                [
                    'Niagara West',
                    'St. Catharines',
                    'Niagara Falls',
                    'Niagara Centre'
                ],
            ],
        },
        'leaders': {
            'tabs': [
                (1, 'Leaders', 'default'),
            ],
            'template': 'options_ridings',
            'ridings': [
                [
                    'Beauce',
                    'Beloeil-Chambly',
                    'Saanich-Gulf Islands',
                    'Burnaby South',
                    'Papineau',
                    "Regina-Qu'Appelle",

                ],
            ],
        },
    }
}
