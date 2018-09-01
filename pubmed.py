# INITIAL LIBRARY IMPORT
from Bio import Entrez, Medline
Entrez.email = "vivek.sharath@utexas.edu"

# CSV CREATION
with open("pubmed.csv", "w") as file:
    # Initialize the first row as the column names
    file.write("Country, Unique_Journals, Year, Amount_English,\n")

# POPULATING THE CSV

# Create a List that stores all the Country Names
countries = ['South Korea', 'Colombia', 'Algeria', 'Spain', 'Canada']

# Iterate through the countries
for j in countries:

    # Iterate through the years
    for i in range(2012, 2018):

        # The string that will change based on the year and country search
        temp = j+"[PL] AND "+str(i)+"[Date of Publication]"

        # Define the Handle
        handle = Entrez.esearch(db="pubmed",  # database to search
                                term=temp,    # search term
                                retmax = 500) # set a max per search

        # Read and save the contents into dictionary pmid_list
        record = Entrez.read(handle)
        handle.close()
        pmid_list = record["IdList"]

        # Use Medline to reference and parse the retreived articles
        handle = Entrez.efetch(db="pubmed", id=pmid_list, rettype="medline", retmode="text")
        records = Medline.parse(handle)

        # List that holds unique Journals the country appears in
        journal_unique = []
        # Count that tracks how many of the papers were in english
        english_count = 0

        # Open the CSV that will write the data
        with open("pubmed.csv", "a") as file:

            # Iterate through the contents
            for record in records:

                # Add to the list if the paper was featured in a new journal
                if record['JT'] not in journal_unique:
                    journal_unique.append(record['JT'])

                # Increment if the paper was in english
                if 'eng' in record['LA']:
                    english_count += 1

            # Fill the row with the apropriate fields
            line = str(j)+","+str(len(journal_unique))+","+str(i)+"," +str(english_count)+","+"\n"

            # Write the line to the file
            file.write(line)

        # Close the Handle
        handle.close()
