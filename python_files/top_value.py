import pandas as pd
import subprocess
import data_download

data_download.download_FPL_data()

players = pd.read_csv("players.csv")

players['cost_millions'] = players['now_cost'] / 10
players['value'] = players['total_points'] / players['cost_millions']

def top_value_players(position=None):
    df = players[['first_name', 'second_name', 'cost_millions', 'total_points', 'value']]
    
    if position is not None:
        df = df[players['element_type'] == position]
    
    return df.sort_values(by="value", ascending=False)

with pd.ExcelWriter('Results/top_value_players.xlsx', engine='openpyxl') as writer:
    top_value_players().to_excel(writer, sheet_name='All Players', index=False)
    top_value_players(position=1).to_excel(writer, sheet_name='Goalkeepers', index=False)
    top_value_players(position=2).to_excel(writer, sheet_name='Defenders', index=False)
    top_value_players(position=3).to_excel(writer, sheet_name='Midfielders', index=False)
    top_value_players(position=4).to_excel(writer, sheet_name='Forwards', index=False)

    for sheet_name in writer.sheets:
        worksheet = writer.sheets[sheet_name]
        for column in worksheet.columns:
            max_length = 0
            column_letter = column[0].column_letter
            
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            
            adjusted_width = max_length + 2
            worksheet.column_dimensions[column_letter].width = adjusted_width

subprocess.run(['open','Results/top_value_players.xlsx'])