# Attempt to use R to analyze Attrition Data
#==============================================================================

# housekeeping
require(readr,dplyr,ggplot2)
source("vaRiables.R")
miDir <- getwd()

# read from csv
inDF <- read.csv('AnalyticsChallenge1-Train.csv')