library(ggplot2)
library(reshape)
setwd("/Users/topfpflanze/projectsOther/2048")
getwd()
crazy <- read.csv(file="data/crazyBot20150130.csv", header = TRUE, sep = ";")
simple <- read.csv(file="data/simpleBot20150130.csv", header = TRUE, sep = ";")

df = melt(data.frame(crazy=crazy$max, simple=simple$max),
          variable_name="Bot")

ggplot(df, aes(value, fill=Bot)) + 
  geom_bar(position="stack", binwidth=1) + 
  scale_x_sqrt(breaks =c(2,4,8,16,32,64,128,256,512))
