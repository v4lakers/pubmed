pubmed
================

### Statistical analysis

``` r
# Upload the Dataset 
pubmed <- read.csv("pubmed.csv", stringsAsFactors = FALSE)

#Create an ANOVA to see how Unique_Journals causes variation in the other variables.
myanova <- aov (Unique_Journals ~ Country + Amount_English, data = pubmed)

#Display the Output 
summary(myanova)
```

    ##                Df Sum Sq Mean Sq F value   Pr(>F)    
    ## Country         3   3741    1247   12.44 0.000238 ***
    ## Amount_English  1   4235    4235   42.26    1e-05 ***
    ## Residuals      15   1503     100                     
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

*From the test, we can see that Country (location) is significant in explaining variation in Unique Journal Count (df = 4, F= 18.63, p &lt; .05). Additionally, we see that Amount\_English (how many papers a country puts out in english) is significant in explaining varaition in Unique Journal Count for a country (df = 1, F= 48.58, p &lt; .05).*

### Plot 1

``` r
# R code for plot 1 goes here

# Use geom_point to make a Scatterplot of Amount_English and Unique_Journals and colors the points by country
ggplot(pubmed, aes(x=Amount_English, y= Unique_Journals, color = Country)) + geom_point() +
  # Add a title
  ggtitle("Scatterplot of Amount of English Papers vs. Unique Journals Appeared In") + 
  # Add axis labels
  xlab("Amount of English Papers") + ylab("Unique Journals Appeared In")
```

<img src="pubmed_files/figure-markdown_github/unnamed-chunk-2-1.png" style="display: block; margin: auto;" />

``` r
# Determine the correlation between Amount_English and Unique_Journals
cor(pubmed$Amount_English, pubmed$Unique_Journals)
```

    ## [1] 0.9106949

*This scatterplot shows a positive relationship between the amount of english papers a country has and how many unique journals the country appears in. This relationship can be further seen in the correlation of .81 between the two variables. In other words, the more papers in english, the better chance a country has to be featured in more medical journals. It is also important to note the outlier in the top right. This point can attest to a high r score, but even without this point, there seems to be a general trend between increasing amounts of english papers leading to more unique journals appeared in. We can see that countries like Algeria and Colmbia have low unique jorunal appeareances and less papers in english. On the other hand, countries like Canada have more papers in english and more appearances in unique journals.*

### Plot 2

``` r
# R code for plot 2 goes here

# Use geom_line to make a Time Series of Unique_Journal count from 2012-2017 for each year
ggplot(pubmed, aes(x=Year, y=Unique_Journals, color = Country))+geom_line() + 
  # Add Country name to the ends of each line
  geom_text(data = pubmed[pubmed$Year == '2017',], aes(label = Country), hjust = 0.7, vjust = -.5) + 
  # Add a Title
  ggtitle("Time Series of Unique Journals a Country Appears in from 2012-2017") + 
  # Add axis labels 
  xlab("Year") + ylab("Unique Journals Appeared In")
```

<img src="pubmed_files/figure-markdown_github/unnamed-chunk-3-1.png" style="display: block; margin: auto;" /> *The time series shows that countries typically have similar amounts of unique journal appearances from year to year with the exception of South Korea. In 2017, South Korea jumped from about 25 unique appearances to 100 which was seen as the outlier point in the previous visualization. We also see that countries like Spain and Canada, which happen to be near medical research giants such as Great Britain and U.S.A respectivley, consistnely have higher Unique Journal Appearances than Colombia and Algeria which are two countries that are quite some ways from the medical research giants mentioned in the Introduction of this project. This is ofcourse speculation, and we do not have enough data to be certain of this claim.*

### Concluding Discussion

*From our data retrieval from NCBI, ANOVA test, scatterplot, and time series, we can conclude that language does affect a country's ability to be pervasive in the medical research world. The Scatterplot showed a positive relationship (r = .81) between the amount of english papers a country has and how many unique journals the country appears in. This could be due to the fact that english is the dominant language in the world and most journals are in english. Countries that have lower amounts of english papers hurt their ability to be featured in more journals and thus have lower pervasiveness in the medical research world. The Time series showed that over the last 5 years, Colombia and Algeria consistnetly had lower unique journals than the other countries. We cannot definitley say that proximity to other medical research giants is causing this, but it is a possibility. Additionally, there may be some interaction between the variables of Country and Amount of English Papers. Different countries have different english literacy rates and future work in this topic can look into this. However, based on the results we have, we can say that for a country to be in the best position possible to be perverse in the medical research world, the country must have plenty of papers in enlglish in order to be included in more unique medical journals. As far as location of a country goes, that needs more data and analysis.*

