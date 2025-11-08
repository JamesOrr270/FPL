import subprocess
import pandas as pd

players = pd.read_csv("players.csv")

def top_points_players(position=None):

    df = players[['first_name', 'second_name', 'now_cost', 'total_points', 'element_type']]
    
    if position is not None:
        df = df[df['element_type'] == position]
    
    result = df.sort_values(by="total_points", ascending=False)

    return result[['first_name', 'second_name', 'now_cost', 'total_points']]

with pd.ExcelWriter('Results/top_players.xlsx', engine='openpyxl') as writer:
    top_points_players().to_excel(writer, sheet_name='All Players', index=False)
    top_points_players(position=1).to_excel(writer, sheet_name='Goalkeepers', index=False)
    top_points_players(position=2).to_excel(writer, sheet_name='Defenders', index=False)
    top_points_players(position=3).to_excel(writer, sheet_name='Midfielders', index=False)
    top_points_players(position=4).to_excel(writer, sheet_name='Forwards', index=False)

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

subprocess.run(['open','Results/top_players.xlsx'])
