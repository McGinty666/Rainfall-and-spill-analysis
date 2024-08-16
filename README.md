# Rainfall-and-spill-analysis

The intention of the code developed here is to investigate how the rainfall recorded in a catchment can be related to environmetal spills, as per instrumentation from a Sewage pump station or other analog level sensor at an overflow. 
Tackling this programatically saves time vs manipulating the data in excel and making subjective visual comparisons, with hope the user only needs to change the path of the data files to be studied, you only need to worry about downloading it, pointing to it, specifying date ranges.

A number of machine learning packages are available which could relate positve numbers on the real line (rainfall) to a binary response (spilling or nor spilling in this case).

The first I have tested in logistic regression.

The potential use of this type of analysis could be:

*Understanding if there is any correlation or predictive potential at all, or there are dry spills, indicating operations issues such as blockages or failed pumps etc. 
*Making a before and after comparison of the correlation given an event (following sewer lining works to prevent infiltration, for example). (comparing Anual spill frequencies with varying rainfall can't provide a good like for like comparison)
*In a particularly large catchment, which encompasses a number radar ranfall grids, is there a particularly strong correlation with any of them? (Indicating areas for further investigation for Impermeable area or infiltration surveys).
*The antecedent rainfall is collected over a number of hours to be specified by the user. Sensitivity to a particular duration can give some indication to the mechanism of the rainfall - runoff response in the sewer system. A sharp rise and fall (high correlation for low hours) indicates impermeable area, a slow one (high correlation for higher hours) suggests there could be an issue of infiltration.


