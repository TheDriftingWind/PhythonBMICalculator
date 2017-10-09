import matplotlib.pyplot as plt
import cmath

data_file = open(r'C:\Users\Charles\Desktop\Dev\Python\body.dat.txt', "r")

class person(object):
    def __init__(self, BiacromialDiameter, BiiliacDiameter, BitrochantericDiameter,
    ChestDepth, ChestDiameter, ElbowDiameter, WristDiameter, KneeDiameter,
    AnkleDiameter, ShoulderGirth, ChestGirth, WaistGirth, NavelGirth, HipGirth,
    ThighGirth, BicepGirth, ForearmGirth, KneeGirth, CalfMaximumGirth,
    AnkleMinimumGirth, WristMinimumGirth, Age, Weight, Height, Gender):
        self.BiacromialDiameter = BiacromialDiameter
        self.BiiliacDiameter = BiiliacDiameter
        self.BitrochantericDiameter = BitrochantericDiameter
        self.ChestDepth = ChestDepth
        self.ChestDiameter = ChestDiameter
        self.ElbowDiameter = ElbowDiameter
        self.WristDiameter = WristDiameter
        self.KneeDiameter = KneeDiameter
        self.AnkleDiameter = AnkleDiameter
        self.ShoulderGirth = ShoulderGirth
        self.ChestGirth = ChestGirth
        self.WaistGirth = WaistGirth
        self.KneeDiameter = KneeDiameter
        self.AnkleDiameter = AnkleDiameter
        self.ShoulderGirth = ShoulderGirth
        self.ChestGirth = ChestGirth
        self.WaistGirth = WaistGirth
        self.NavelGirth = NavelGirth
        self.HipGirth = HipGirth
        self.ThighGirth = ThighGirth
        self.BicepGirth = BicepGirth
        self.ForearmGirth = ForearmGirth
        self.KneeGirth = KneeGirth
        self.CalfMaximumGirth = CalfMaximumGirth
        self.AnkleMinimumGirth = AnkleMinimumGirth
        self.WristMinimumGirth = WristMinimumGirth
        self.Age = Age
        self.Weight = Weight
        self.Height = Height
        self.Gender = Gender


people = []
#read in data
for i in data_file:
  #read the line and convert into an array
  line = i.split()
  #take the parts of the array and create a person instance out of it
  new_person = person(
  float(line[0]), float(line[1]), float(line[2]), float(line[3]), float(line[4]), float(line[5]), float(line[6]), float(line[7]),
  float(line[8]), float(line[9]), float(line[10]), float(line[11]), float(line[12]), float(line[13]), float(line[14]), float(line[15]),
  float(line[16]), float(line[17]), float(line[18]), float(line[19]), float(line[20]), float(line[21]), float(line[22]),
  float(line[23]), float(line[24])
  )
  #add that person to the array of all the people
  people.append(new_person)

#done reading, close data_file
data_file.close()

#now we should have all of the data in the people array
def calculate_BMI(person_array):
  #weight/height(in m)**2
  BMI_array = []
  for p in person_array:
      #convert to meters(data is in cm)
      height_inMeters = p.Height/100
      #weight already in kg - BMI = weight(kg)/height(m)**2
      BMI = (p.Weight / (height_inMeters**2))
      BMI_array.append(BMI)
  return BMI_array


def calculate_leastSquaresLine(x_set, y_set):
    #x_set and y_set should be equal in length
    n = len(x_set)
    sum_x = sum(x_set)
    sum_y = sum(y_set)
    sum_x2d = 0
    sum_y2d = 0
    sum_xy = 0
    for x in x_set:
        sum_x2d += x**2
    for y in y_set:
        sum_y2d += x**2
    for i in range(len(x_set)):
        sum_xy += (x_set[i] * y_set[i])
    #slope formula
    slope = (n*sum_xy - (sum_x*sum_y)) / (n*sum_x2d - (sum_x)**2)
    intercept = (sum_y - (slope*sum_x)) / n
    result = []
    result.append(slope)
    result.append(intercept)
    # result[0] = slope | result[1] = intercept
    return result



def calculate_correlation(x_set, y_set):
    n = len(x_set)
    sum_x = sum(x_set)
    sum_y = sum(y_set)
    sum_x2d = 0
    sum_y2d = 0
    sum_xy = 0
    for x in x_set:
        sum_x2d += x**2
    for y in y_set:
        sum_y2d += x**2
    for i in range(len(x_set)):
        sum_xy += (x_set[i] * y_set[i])
    #correlation formula
    corr = (n*sum_xy - (sum_x*sum_y)) / cmath.sqrt((n*sum_x2d - (sum_x)**2) * (n*sum_y2d - (sum_y)**2))
    return corr

def get_Ages(people_array):
    Ages = []
    for p in people_array:
        Ages.append(p.Age)
    return Ages

def get_Weights(people_array):
    Weights = []
    for p in people_array:
        Weights.append(p.Weight)
    return Weights

def calculate_PhysAtr(people_array):
    PhysAtr_array = []
    for p in people_array:
        ChestDiameter = p.ChestDiameter
        ChestDepth = p.ChestDepth
        BitrochantericDiameter = p.BitrochantericDiameter
        WristGirth = p.WristMinimumGirth
        AnkleGirth = p.AnkleMinimumGirth
        Height = p.Height
        PhysAtr = (-110 + 1.34 *(ChestDiameter) + 1.54 *(ChestDepth) + 1.20*(BitrochantericDiameter) + 1.11*(WristGirth) + 1.15*(AnkleGirth) + 0.177*(Height))
        PhysAtr_array.append(PhysAtr)
    return PhysAtr_array

#Graph 1  Data
Graph1_BMI = calculate_BMI(people)
print Graph1_BMI
Graph1_Ages = get_Ages(people)
print Graph1_Ages
Graph1_leastSQ = calculate_leastSquaresLine(Graph1_BMI, Graph1_Ages)
print Graph1_leastSQ[0]
print Graph1_leastSQ[1]
Graph1_slopeLine = []
for i in range(int(max(Graph1_BMI))):
    Graph1_slopeLine.append(Graph1_leastSQ[1] + (Graph1_leastSQ[0]*i))

Graph1_correlation = calculate_correlation(Graph1_BMI, Graph1_Ages)
print Graph1_correlation

#Graph 2 Data
Graph2_Weight = get_Weights(people)
print Graph2_Weight
Graph2_PhysAtr = calculate_PhysAtr(people)
print Graph2_PhysAtr
Graph2_leastSQ = calculate_leastSquaresLine(Graph2_Weight, Graph2_PhysAtr)
print Graph2_leastSQ[0]
print Graph2_leastSQ[1]
Graph2_slopeLine = []
for i in range(int(max(Graph2_Weight))):
    Graph2_slopeLine.append(Graph2_leastSQ[1] + (Graph2_leastSQ[0]*i))

Graph2_correlation = calculate_correlation(Graph2_Weight, Graph2_PhysAtr)
print Graph2_correlation

#plot Graph 1
#plot data
plt.plot(Graph1_BMI, Graph1_Ages, '.')
#plot fit line
plt.plot(Graph1_slopeLine)
plt.xlabel('BMI')
plt.ylabel('Age')
plt.text(0, max(Graph1_Ages), 'Slope: ' + str(Graph1_leastSQ[0]), fontdict=None, withdash=False)
plt.text(0, max(Graph1_Ages) - 5, 'Y-intercept: ' + str(Graph1_leastSQ[1]), fontdict=None, withdash=False)
plt.text(0, max(Graph1_Ages) - 10, 'Correlation: ' + str(Graph1_correlation), fontdict=None, withdash=False)

plt.figure()
#plot Graph 2
plt.plot(Graph2_Weight, Graph2_PhysAtr, '.')
#plot fit line
plt.plot(Graph2_slopeLine)
plt.xlabel('Weight')
plt.ylabel('PhysAtr')
plt.text(0, max(Graph2_PhysAtr), 'Slope: ' + str(Graph2_leastSQ[0]), fontdict=None, withdash=False)
plt.text(0, max(Graph2_PhysAtr) - 5, 'Y-intercept: ' + str(Graph2_leastSQ[1]), fontdict=None, withdash=False)
plt.text(0, max(Graph2_PhysAtr) - 10, 'Correlation: ' + str(Graph2_correlation), fontdict=None, withdash=False)

plt.show()
