# RandomBiographyGenerator

How to run:
Download project folder
Ensure GeneratedPeople folder exists in project folder.

To Generate and Save a Batch of People:

    run helper script savePocketLink.py

    Dependencies:  datetime, os, pynput, time
    Main script Dependencies: csv, random, string

To generate and print one person in terminal:
    
    Run createPocketLink.py from project directory.

Description:

A python script to generate random answers for popular social media games based on common security questions like pet's name, childhood street.

Pet list name is a deduplicated file based on Seattle pet licensing information. https://catalog.data.gov/dataset/seattle-pet-licenses

Streets name list is pulled from 1k records generated from https://www.name-generator.org.uk/

Surnames list is a combination of most popular surnames in the UK & US. This could do with some more diversity.

Colours list is pulled from Wikipedia and includes hex codes for future exploitation.

First names is pulled randomly from 

Film list is pulled from top grossing films by year and top grossing films of all time, minus problematic films like W B Griffith, Gone With the Wind, Song of the South & HP. Film List also has the entire Criterion Collection.

Pronouns & Gender lists were designed to be inclusive without being too obscure, and can be edited by the end user. One statistical consequence of going from values typically expressed in binary terms to 6-12 options is that the random function currently represents non-binary people at a rate greater than currently shown by public statistics. I chose to leave this as is, as any attempt to weight the function to overcorrect would be computationally difficult and overly heteronormative.

Eventually the goal will be to build out the databases to be larger and allow the user to select their country/region for added personalisation.

Please note: This program is NOT intended to produce answers to security questions for user accounts, as it is not random enough, and the datasets are not large enough.



