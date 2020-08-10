# a string
name = "John Young"
occupation = "Astronaut"

# an integer
age = 81

# float
days_in_space = 34.806

# boolean
walked_on_moon = True
snuck_cornedbeef_into_gemini_capsule = True
active_duty = False

# list
missions = ['Gemini 3','Gemini 10','Apollo 10','Apollo 16','STS-1','STS-9']
second_mission = missions[1] # 2nd mission 'Gemini 10'

# dictionary
mission_dates = {
	'Gemini 3' : '23 March 1965',
	'Gemini 10' : '18-21 July 1966',
	'Apollo 10' : '18-26 May 1969',
	'Apollo 16' : '16-27 April 1972 ',
	'STS-1' : '12-14 April 1981',
	'STS-9' : '28 November - 6 December 1983'
}
just_the_mission_names = mission_dates.keys()  # a list of mission name
just_the_mission_dates = mission_dates.values() # a list of mission dates


# tuple
# tuples are weird - you can organize the basic variable types in a comma delimited list
# and retrieve them in that order
military_rank = ("Captain","US Navy")
rank, usforce = military_rank # rank = "Captain" and usforce = "US Navy"

# objects (classes)
# use objects when you have a lot of things with similiar data structure and actions
class Astronaut(object):
	
	# __init__ automatically called when creating an object
	def __init__(self, nameStr = None):
		print "Creating new astronaut:", nameStr
		self.name = nameStr

	def set_name(self, nameStr):
		self.name = nameStr

mr_awesome = Astronaut("J. Young")
mr_awesome.set_name("John Young")
mr_awesome.age = 81 #dynamically set object property/variable

print "This variable is :", type(mr_awesome)
print "Name: %s" % mr_awesome.name


#print "%s is %d years old" % (mr_awesome.name, mr_awesome.age)
print mr_awesome.name, "is", mr_awesome.age, "years old"




