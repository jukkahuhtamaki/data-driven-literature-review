README.md

# Data-driven literature review #

Rough implementation of data-driven literature review routine. Support only Scopus for now.

Used to implement analysis for the following article:

Still, K., Huhtamäki, J., & Russell, M. G. (2013). [Relational Capital and Social Capital: One or two Fields of Research?](https://www.researchgate.net/publication/260259631_Relational_Capital_and_Social_Capital_One_or_two_Fields_of_Research) In Proceedings of the 10th International Conference on Intellectual Capital, Knowledge Management and Organisational Learning, The George Washington University, Washington, DC, USA, 24-25 October 2013 (pp. 420–428). 

## Running the process ##

1. Export data from Scopus
1. Place the data to data/01-scopus/literature.csv
1. python run.process.rawdata.py
1. run.create.networks

Note that you can alter the code to add several sources of literature. Please contribute to develop the process futher.