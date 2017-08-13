class Variablez():
	'''
	A Class for storing Parameters and Settings
	'''
	def __init__(self):
		'''
		Initialize Parameters and Settings
		'''
		self.inFileString = 'AnalyticsChallenge1-Train.csv'
		self.inYesNoBoo= {
		'Yes':1,
		'No':0
		}
		self.inDFCatCols= [
#		'Attrition',
		'BusinessTravel',
		'Department', 
		'Education',
		'EducationField',
		'EmployeeCount',
		'EmployeeNumber',
		'EnvironmentSatisfaction',
		'Gender',
		'JobInvolvement',
		'JobLevel',
		'JobRole',
		'JobSatisfaction',
		'MaritalStatus',
		'Over18',
		'OverTime'
		]
		self.inDFIntCols=[
		'Age', 
#		'Attrition',
		'DailyRate', 
		'DistanceFromHome', 
		'HourlyRate', 
		'MonthlyIncome', 
		'MonthlyRate', 
		'NumCompaniesWorked',
		'PercentSalaryHike', 
		'PerformanceRating',
		'RelationshipSatisfaction',
		'StandardHours',
		'StockOptionLevel',
		'TotalWorkingYears', 
		'TrainingTimesLastYear', 
		'WorkLifeBalance',
		'YearsAtCompany', 
		'YearsInCurrentRole', 
		'YearsSinceLastPromotion', 
		'YearsWithCurrManager'
		]
		self.inDFnames=[
		'Age', 
		'Attrition', 
		'BusinessTravel', 
		'DailyRate', 
		'Department',
		'DistanceFromHome', 
		'Education', 
		'EducationField', 
		'EmployeeCount',
		'EmployeeNumber', 
		'EnvironmentSatisfaction', 
		'Gender', 
		'HourlyRate',
		'JobInvolvement', 
		'JobLevel', 
		'JobRole', 
		'JobSatisfaction',
		'MaritalStatus', 
		'MonthlyIncome', 
		'MonthlyRate', 
		'NumCompaniesWorked',
		'Over18', 
		'OverTime', 
		'PercentSalaryHike', 
		'PerformanceRating',
		'RelationshipSatisfaction', 
		'StandardHours', 
		'StockOptionLevel',
		'TotalWorkingYears', 
		'TrainingTimesLastYear', 
		'WorkLifeBalance',
		'YearsAtCompany', 
		'YearsInCurrentRole', 
		'YearsSinceLastPromotion',
		'YearsWithCurrManager'
       ]
