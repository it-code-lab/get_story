import pandas as pd

def save_results_to_excel(results, output_file):
    """
    Save results to an Excel file.

    Args:
        results (list): List of dictionaries containing video details.
        output_file (str): Path to the output Excel file.
    """
    df = pd.DataFrame(results)
    df.to_excel(output_file, index=False)
