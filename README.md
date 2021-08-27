Visiualizing Uncertainty in Cloud Services
============================================

## Introduction

This project aims to visualize recent cloud outage statistics of major cloud services, including Amazons's AWS service, Microsoft's Azure, Salesforce, Netflix and 28 other services. The database used for this project was taken from a [Cloud Outage Study](https://ucare.cs.uchicago.edu/projects/cbs/) conducted by Haryadi S. Mingzhe Hao,
and Riza O. Suminto from the University of Chicago and Agung Laksono, Anang D. Satria,
Jeffry Adityatama, and Kurnia J. Eliazar from Surya Unversity.  

## The Process

The Cloud Outage Study database presented the data for each company in a text file, which contained various bits of information about each outage incident that the company faced. Please look at the [classifications document](classifications.docx) for more detail on each of the fields of data gathered from each incident. 

In order to parse through the data, I plan to format all the data in a JSON file which will allow me to easily parse the data when using python. This is currently in progress.
