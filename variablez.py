class Variablez():
	'''
	A Class for storing Parameters and Settings
	'''
	def __init__(self):
		'''
		Initialize Parameters and Settings
		'''
		self.inFileString = 'AnalyticsChallenge1-Train.csv'
		self.inDFCatCols= ['Attrition',
		'BusinessTravel',
		'Department',
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
		'OverTime',
		'PerformanceRating',
		'RelationshipSatisfaction',
		'StandardHours',
		'StockOptionLevel',
		'WorkLifeBalance']
		self.inDFIntCols=['Age', 
		'HourlyRate', 
		'MonthlyIncome', 
		'MonthlyRate', 
		'NumCompaniesWorked',
		'PercentSalaryHike', 
		'TotalWorkingYears', 
		'TrainingTimesLastYear', 
		'YearsAtCompany', 
		'YearsInCurrentRole', 
		'YearsSinceLastPromotion', 
		'YearsWithCurrManager']
