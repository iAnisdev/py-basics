teamBoston = {
    'name': 'Boston Red Sox',
    'founded': 1901,
}

print(teamBoston['name'])

teamNewYork = {
    'name': 'New York Yankees',
    'founded': 1901,
}

print(teamNewYork['founded'])
print(teamBoston.get('city'))
print(teamBoston.get('owner' , 'No owner found'))
print(teamBoston.get('league' , 'American League'))

teamChicago = {}
teamChicago['name'] = 'Chicago White Sox'
teamChicago['founded'] = 1901

print(teamChicago)
teamChicago.clear()
print(teamChicago)

teamSanFrancisco = dict()

teamSanFrancisco.update({
    'name': 'San Francisco Giants',
    'founded': 1883,
})

print(teamSanFrancisco)

teamLosAngeles ={}

teamLosAngeles.update({
    'name': 'Los Angeles Dodgers',
    'founded': 1883
})

print(teamLosAngeles)

del teamLosAngeles['founded']
print(teamLosAngeles)


teamNewYork.update({
    'wins': [1923, 1927, 1928, 1932, 1936, 1937, 1938, 1939, 1941, 1943, 1947, 1949, 1950, 1951, 1952, 1953, 1956, 1958, 1961, 1962, 1977, 1978, 1996, 1998, 1999, 2000, 2009],
    'owner': {
        'name': 'Yankee Global Enterprises',
        'founded': 2002,
        'website': 'yankees.com'
    }
})

print(teamNewYork)
print(teamNewYork['owner']['name'])
print(teamNewYork['wins'][0])
print(teamNewYork.keys())
print(teamNewYork['owner'].keys())

teamNewYork.update({
    'losses': [1921, 1922, 1926, 1942, 1944, 1963, 1964, 1976, 1977, 1978, 1981, 2001, 2003, 2004, 2010, 2012, 2017]
})

print(teamNewYork.values())
print(teamNewYork['owner'].values())

print(len(teamNewYork))
for key in teamNewYork:
    print(key)

print(teamNewYork.items())
print(teamNewYork['owner'].items())

for key, value in teamNewYork.items():
    print(key, value)


teamWashington = {
    'name': 'Washington Nationals',
    'founded': 1969,
    'wins': [1981],
    'owner': {
        'name': 'Lerner Enterprises',
        'founded': 1952,
        'website': 'nationals.com'
    }
} 

print(teamWashington)
print(teamWashington['owner']['name'])
teamWashington.update({
    'losses': [1981]
})

print(teamWashington)
teamWashington.popitem()
print(teamWashington)