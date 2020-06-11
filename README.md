Project Name: Tip Guesser
Authors: Terry Shih, Narendra Babu Ramisetty

Packages beyond those in SciPy-bundle: h2o

Instructions:
If models are already made:
    1. Open 'PredictionMaker.ipynb' in Jupyter Notebook.
    2. Run all of the cells of PredictionMaker to make a prediction on 'input.csv' with the GBM regressor

If models and data are corrupted/missing:
    If 'green_tripdata_2019-03.csv' is missing from the data folder
        1. Go to 'https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page' and download the .csv file for the Green Taxi data for March of 2019
        2. Place this .csv in the data folder
    3. Open 'TrainMaker.ipynb' in Jupyter Notebook.
    4. Run the cells of TrainMaker to make train.csv and input.csv out of 'green_tripdata_2019-03.csv'
    5. Open 'ModelMaker.ipynb' in Jupyter Notebook.
    6. Run the cells of ModelMaker, optionally skipping the 5th from last to 2nd from last cells, to generate and save the 6 prediction models
    7. Run the instructions from 'If models are already made' to make prediction on 'input.csv'

Note: taxi.html was included for completeness reasons. In its current state, it does not function as intended.

Note: The way our models are currently designed/trained, they can only reasonably predict fares that occur in March.

Note: The metric matrix used to evaluate the models can be found in the final report.
