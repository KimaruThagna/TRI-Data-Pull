import pandas as pd
from glob import glob
from datetime import datetime

from find_parent_company import parent_company


def process_all_files():
    for file in glob("data/*.xlsx"):
        excel_df = pd.read_excel(file)
        air_pollution_data = excel_df.loc[excel_df["Media Type"] == "Air"]
        """generate TRID-> Parent company mapping 
         from unique Facility column to reduce selenium calls
         """
        mapping = {}
        trid_list = air_pollution_data.Facility.unique()
        for facility in trid_list:
            # pick last item due to name inconsistency
            mapping[facility] = parent_company(facility.split("-")[-1])

        # add parent company to df
        air_pollution_data["Parent_Company"] = air_pollution_data["Facility"].apply(
            lambda facility: mapping[facility]
        )
        # record sorting
        air_pollution_data.sort_values(by=["Parent_Company", "Facility"])
        file_name = (file.split(".")[0]).split("/")[1]
        air_pollution_data.to_csv(
            f"final_output/{file_name}_{datetime.now()}.csv", index=False
        )


process_all_files()
