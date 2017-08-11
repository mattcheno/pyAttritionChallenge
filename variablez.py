class Variablez():
	'''
	A Class for storing Parameters and Settings
	'''
	def __init__(self):
		'''
		Initialize Parameters and Settings
		'''
		self.inFileString = 'AnalyticsChallenge1-Train.csv'
		'''
		self.inDFColConv= {'Age':int,
                                   'Attrition':categorical,
                                   'BusinessTravel':category,
                                   'DailyRate':int64,
                                   'Department':category,
                                   'DistanceFromHome':int64,
                                   'Education':int64,
                                   'EducationField':category,
                                   'EmployeeCount':category,
                                   'EmployeeNumber':category,
                                   'EnvironmentSatisfaction':category,
                                   'Gender':category,
                                   'HourlyRate':int,
                                   'JobInvolvement':category,
                                   'JobLevel':category,
                                   'JobRole':category,
                                   'JobSatisfaction':category,
                                   'MaritalStatus':category,
                                   'MonthlyIncome':int,
                                   'MonthlyRate':int,
                                   'NumCompaniesWorked':int,
                                   'Over18':category,
                                   'OverTime':category,
                                   'PercentSalaryHike':int,
                                   'PerformanceRating':category,
                                   'RelationshipSatisfaction':category,
                                   'StandardHours':category,
                                   'StockOptionLevel':category,
                                   'TotalWorkingYears':int,
                                   'TrainingTimesLastYear':int,
                                   'WorkLifeBalance':category,
                                   'YearsAtCompany':int,
                                   'YearsInCurrentRole':int,
                                   'YearsSinceLastPromotion':int,
                                   'YearsWithCurrManager':int}
		'''
		self.inDFIntCols={'Age':int,
                                  'HourlyRate':int,
                                  'MonthlyIncome':int,
                                  'MonthlyRate':int,
                                  'NumCompaniesWorked':int,
                                  'PercentSalaryHike':int,
                                  'TotalWorkingYears':int,
                                  'TrainingTimesLastYear':int,
                                  'YearsAtCompany':int,
                                  'YearsInCurrentRole':int,
                                  'YearsSinceLastPromotion':int,
                                  'YearsWithCurrManager':int}
