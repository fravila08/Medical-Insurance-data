# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']
updated_damages=[]
# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# Update Recorded Damages
updated_damages=[]
# test function by updating damages
def damage_update(damages):
  for i in damages:
    if i.count('Damages')>=1:
      updated_damages.append(i)
    else:
      if i[-1]=='M':
        updated_damages.append(float(i[:-1])*1000000)
      elif i[-1]=='B':
        updated_damages.append(float(i[:-1])*1000000000)
  return updated_damages
# print( damage_update(damages ))

# 2 
# Create a Table
hurricane_table={}
for i in range(len(names)):
  hurricane_table.update({names[i]:{'Name':names[i], "Month":months[i], 'Years':years[i], 'Max Winds':max_sustained_winds[i], 'Affected Areas':areas_affected[i], 'Deaths':deaths[i]}})
# print(hurricane_table)
# 3
# Organizing by Year
year_table={}
for i in range(len(names)):
  year_table.update({years[i]:{'Name':names[i], "Month":months[i], 'Years':years[i], 'Max Winds':max_sustained_winds[i], 'Affected Areas':areas_affected[i], 'Deaths':deaths[i]}})
# print(year_table)
# 4
# Counting Damaged Areas
def pop(area, ltr):
  if area.count(ltr)>0:
    index=area.index(ltr)
    area.pop(index)
    pop(area, ltr)
# 5 
# Calculating Maximum Hurricane Count
result={}
def affected_count():
  all_areas=[]
  for i in areas_affected:
    for j in i:
      all_areas.append(j)
  for a in all_areas:
    result.update({a:all_areas.count(a)})
    pop(all_areas, a)
  return result

affected_count()
def most_hit():
  holder={}
  highest=0
  for i in result:
    if len(holder)==0:
      holder={i:result[i]}
      highest=result[i]
    else:
      if result[i]>highest:
        holder={i:result[i]}
        highest=result[i]
  return holder
most_hit()


# 6
# Calculating the Deadliest Hurricane
def deth_hur():
  counter=0
  for i in deaths:
    if i > counter:
      counter = i
  index=deaths.index(counter)
  return names[index]
print(deth_hur())

# 7
# Rating Hurricanes by Mortality
def mortality_rating():
  answer={}
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  
  for i in deaths:
    index=deaths.index(i)
    lvl=0
    for j in mortality_scale:
      if i > mortality_scale[j]:
        lvl= j
    answer.update({names[index]:lvl})
  return answer
print(mortality_rating())