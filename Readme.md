Here's the updated `README.md` file without the installation process:

---

# City AQI Prediction Using Random Forest

This project predicts the Air Quality Index (AQI) for a selected city based on historical pollution data. The model is built using the Random Forest algorithm and provides insights into air quality levels for various cities.

## Features
- **Data Loading & Cleaning**: 
  - The dataset is loaded from a CSV file (`city_day.csv`) containing daily pollution data for multiple cities.
  - Duplicate rows are removed, and missing values are filled using column means.
  - The 'Date' column is converted to datetime format for easier processing.

- **City Selection**: 
  - The program displays a list of available cities in the dataset.
  - The user selects a city to visualize the AQI and make predictions.

- **Model Training**: 
  - The Random Forest Regressor is trained on the city's data, excluding non-numeric columns like `City`, `Date`, and `AQI_Bucket`.
  - The model predicts AQI values for unseen data and evaluates its performance using Root Mean Squared Error (RMSE) and R-squared (R2) metrics.

- **Accuracy Estimation**: 
  - The code calculates the accuracy for the first test sample and provides a reason based on the accuracy level.

- **AQI Prediction and Categorization**: 
  - A new AQI prediction is made using a sample input from the test set.
  - The predicted AQI is classified into one of the official air quality categories (Good, Moderate, Unhealthy, etc.).

## How to Use

1. **Dataset**: Ensure that the `city_day.csv` file is present in the same directory as the script. The dataset should include columns like `City`, `Date`, `AQI`, and pollution-related measurements.

2. **Running the Code**: Execute the script to begin the AQI prediction process:
    ```bash
    python script_name.py
    ```

3. **City Selection**: After running the script, the user will be prompted to select a city from the list provided.

4. **Results**:
   - After selecting a city, the model will be trained on that city's data.
   - Model performance (RMSE and R2 score) will be displayed.
   - The program will also predict the AQI for a sample input and classify the air quality.

## Output Explanation

- **Model Performance**: 
  - **RMSE (Root Mean Squared Error)**: A lower RMSE indicates better predictions.
  - **R2 Score**: Represents how well the data fits the model, with values closer to 1 indicating better performance.
  
- **Accuracy**: The percentage difference between the predicted and actual AQI for a test sample.

- **AQI Prediction**: The predicted AQI for a sample input and its classification into one of the following categories:
  - `Good`
  - `Moderate`
  - `Unhealthy for Sensitive Groups`
  - `Unhealthy`
  - `Very Unhealthy`
  - `Hazardous`

## Sample Output

```bash
Initial data loaded from 'city_day.csv'.

Data Cleaning Process:
  - Removed 0 duplicate rows.
  - Converted 'Date' column to datetime format.
  - Filled 1000 missing values with column means.

Available cities in the dataset:
1. Delhi
2. Mumbai
3. Kolkata

Enter the number corresponding to the city you want to see data for: 1

You selected: Delhi

Model Performance for Delhi:
  - Root Mean Squared Error (RMSE): 32.10
  - R-squared (R2): 0.85

Accuracy: 92.34%
Reason for Accuracy: High accuracy due to consistent data patterns and low variance in AQI levels for the selected city.

Predicted AQI for a sample input from Delhi: 180.50
Air Quality Category: Unhealthy
```

## License

This project is licensed under the MIT License. You are free to use and modify the code for personal or educational purposes.

## Acknowledgments

- **Dataset**: Ensure the dataset includes valid and consistent air quality measurements.
- **Python Libraries**: The project relies on common machine learning and data manipulation libraries.

Feel free to contribute, open issues, or suggest improvements!

HAPPY CODING!